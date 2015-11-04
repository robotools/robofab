/**
 * Plugin: jquery.markdown.js
 *
 * Requires: jquery.js and showdown.js
 *
 * Author: Frank Hellwig
 */
(function($) {

    // Our Showdown converter.
    var converter = new Showdown.converter();

    /**
     * Resolves the path against the base and loads the Markdown document from
     * the resolved location. The Markdown document is converted to HTML using
     * the Showdown converter. On success, all non-absolute <a href="ref"> and
     * <img src="ref"> references are resolved against the path and then again
     * against the base. This allows for page-relative references in links and
     * images independent of the base directory containing the documents.
     */
    $.fn.markdown = function(base, path) {
        if (path) {
            path = makeRelative(path);
        }
        var url = resolve(base, path);
        var $this = this;
        $.ajax({
            url: url,
            cache: false,
            type: 'GET',
            dataType: 'text',
            beforeSend: forceTextResponse,
            success: function(text, textStatus, xhr) {
                var html = convert(base, path, text, url);
                html = removeResolvedSuffixes(html);
                $this.each(function() {
                    var tagName = this.tagName.toLowerCase();
                    var $this= $(this);
                    if (tagName === 'pre') {
                        $this.text(html);
                    } else {
                        $this.html(html);
                    }
                    $this.trigger('change.markdown', xhr);
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                $this.text(url + ' (' + xhr.status + ' ' + xhr.statusText + ')');
                $this.trigger('change.markdown', xhr);
            }
        });
        return this;
    };

    /**
     * Firefox tries parsing the AJAX response as XML eventhough the dataType
     * is specified as 'text' and then indicates a syntax error because
     * markdown text is not XML. This function makes Firefox interpret the
     * response as text. Credit: <http://stackoverflow.com/questions/335409/
     * jquery-getjson-firefox-3-syntax-error-undefined/633031#633031>
     */
    function forceTextResponse(xhr) {
        if (xhr.overrideMimeType) {
            xhr.overrideMimeType("text/plain");
        }
    }

    //------------------------------------------------------------------------
    // Basic design decision: we convert to HTML first and then resolve
    // references. This allows the Showdown converter to do the heavy lifting
    // of determining what link and image references are real and which ones
    // are in code blocks. If we performed a global search-and-resolve for
    // [text](link) references we would also modify references in code blocks.
    //------------------------------------------------------------------------

    /**
     * Performs the transclusion, conversion, and reference resolution. Note
     * that we replace transclusions before converting to HTML. This is to
     * avoid stand-alone {{ref}} transclude tags from becoming <p>{{ref}}</p>
     * elements only to have the transclusion tag be replaced by a converted
     * Markdown document that would now be within <p> or some other block tag.
     */
    function convert(base, path, text, stack) {
        text = replaceTransclusions(base, path, text, stack);
        text = converter.makeHtml(text);
        text = resolveReferences(base, path, text);
        return text;
    }

    //------------------------------------------------------------------------
    // The following creates a TextBuffer class which is critical to properly
    // handling transclusions. The idea is that you always want to be replacing
    // tags *after* the last replacement. Otherwise, you end up matching tags
    // that were created by transclusions and not the tags that were found in
    // the original text.
    //------------------------------------------------------------------------

    /**
     * Creates a new TextBuffer object initialized with the specified string.
     */
    function TextBuffer(s) {
        // The internal text buffer (an array of string segments).
        this._buf = [s];
    }

    /**
     * Replaces the first occurance of match <m> with replacement <r>. The
     * search for <m> starts after any previous replacements were performed.
     * Returns true if the match was found, false if not.
     */
    TextBuffer.prototype.replace = function(m, r) {
        var cur = this._buf.length - 1; // last index in buffer
        var tmp = this._buf[cur]; // last string in buffer
        var i = tmp.indexOf(m); // find the match in the last string
        if (i < 0) {
            return false; // not found - do nothing and return false
        }
        this._buf[cur++] = tmp.substring(0, i);
        this._buf[cur++] = r;
        this._buf[cur] = tmp.substr(i + m.length);
        return true;
    };

    /**
     * Returns the string representation of this text buffer.
     */
    TextBuffer.prototype.toString = function() {
        return this._buf.join('');
    };

    //------------------------------------------------------------------------
    // The following functions handle transclusions. There are three types of
    // transclusions. Document transclusions, written as {{ref}}, recursively
    // replace the specified tag by converting the specified reference as a
    // Markdown document. Raw transclusions, written as {{!ref}}, simply
    // replace the specified tag with the file specified by the reference.
    // Example transclusions, written as {{%ref}}, are for writing about
    // transclusions. The % is removed and the tag is left in place.
    //
    // The resource specified by the tranclusion tag is read synchronously. Not
    // doing this would be a housekeeping challenge. Since transclusions are
    // performed from an asynchronous call (the original Markdown document
    // access), the user thread in the browser is not blocked.
    //------------------------------------------------------------------------

    // The following regular expressions use the default greedy evaluation and
    // match transclusion strings that do not include curly braces. This is
    // more efficient then using the reluctant quantifier. For further details,
    // see <http://blog.stevenlevithan.com/archives/greedy-lazy-performance>.

    // Finds all transclusion tags enclosed in curly braces.
    // They look like this: {{path}}, {{%path}}, or {{!path}}.
    var TRANSCLUDE_TAGS = /{{[%!]?[^{}]*}}/g;

    // Gets the transclusion reference between the curly braces.
    var TRANSCLUDE_REF = /{{([^{}]+)}}/;

    /**
     * Recursively handles transclusions by finding all {{<ref>}} tags and
     * replacing the tag with the text. Here's the resolution logic:
     *
     * base: content/
     * path: tutorial/javascript.txt
     *  tag: {{example.txt}} (in javascript.txt)
     *  ref: tutorial/example.txt
     *  url: content/tutorial/example.txt
     */
    function replaceTransclusions(base, path, text, urls) {

        var tags = text.match(TRANSCLUDE_TAGS);

        if (tags === null || tags.length === 0) {
            return text; // done - no more tags found
        }

        var buf = new TextBuffer(text);
        var n = tags.length;

        for (var i = 0; i < n; i++) {
            var tag = tags[i];
            var ref = tag.match(TRANSCLUDE_REF)[1]; // gets <ref> from {{<ref>}}

            if (ref.charAt(0) === '%') { // example transclusion
                buf.replace(tag, '{{' + ref.substr(1) + '}}');
                continue;
            }

            var raw = ref.charAt(0) === '!'; // raw text transclusion

            if (raw) {
                ref = ref.substr(1); // use the part after the !
            }

            // Resolve the reference against the page and the base.
            ref = resolve(path, ref);
            ref = makeRelative(ref);
            var url = resolve(base, ref);

            // Have we seen this URL before? If so, then it is a recursive
            // transclusion. We only check this if it is not a raw transclusion
            // since raw transclusions are not transitively transcluded.
            if (!raw && urls.indexOf(url) >= 0) {
                buf.replace(tag, 'RECURSIVE TRANSCLUSION: ' + tag);
                continue;
            }

            var tmp = getTranscludedText(url);

            if (!tmp) {
                buf.replace(tag, 'INVALID TRANSCLUSION: ' + tag);
                continue;
            }

            // Performe transitive transclusion via recursion. We add the URL
            // of the transcluded document to the URLs we've already seen.
            if (!raw) {
                var tmp = convert(base, ref, tmp, urls + url);
            }

            buf.replace(tag, tmp);
        }
        return buf.toString();
    }

    /**
     * Gets transcluded text from the specified URL. This is a synchronous call
     * but it is being called from an asynchronous handler.
     */
    function getTranscludedText(url) {
        var retval = null;
        $.ajax({
            url: url,
            async: false,
            cache: false,
            type: "GET",
            dataType: "text",
            beforeSend: forceTextResponse,
            success: function(text, textStatus, xhr) {
                retval = $.trim(text);
            }
        });
        return retval;
    }

    //------------------------------------------------------------------------
    // The following functions resolve references with respect to a base
    // directory and the document path. This allows for absolute references
    // (references that start with a slash) in Markdown documents that are
    // resolved against a base directory instead of the site root.
    //------------------------------------------------------------------------

    /**
     * Returns the result of resolving the specified reference against the
     * specified base and path.
     */
    function resolveReference(base, path, ref) {
        // Don't modify absolute links.
        if (isAbsolute(ref)) {
            return ref;
        }
        ref = resolve(path, ref);
        ref = makeRelative(ref);
        ref = resolve(base, ref);
        return ref;
    }

    /**
     * Resolves link and image references in the specified text. The tags have
     * the '_resolved' suffix appended to them so that they are not modified
     * multiple times in transclusions. (References in the referring document
     * are modified after the referenced document has been transcluded.) These
     * '_resolved' suffixes are removed before updating the matched set.
     */
    function resolveReferences(base, path, text) {
        text = text.replace(/<a\shref="([^"]+)/g, function(s, href) {
            return '<a_resolved href="' + resolveReference(base, path, href);
        });
        text = text.replace(/<img\ssrc="([^"]+)/g, function(s, src) {
            return '<img_resolved src="' + resolveReference(base, path, src);
        });
        return text;
    }

    /**
     * Removes the '_resolved' suffixes from link and image tags that were
     * added to resolved references.
     */
    function removeResolvedSuffixes(text) {
        text = text.replace(/<a_resolved /g, '<a ');
        text = text.replace(/<img_resolved /g, '<img ');
        return text;
    }

    //------------------------------------------------------------------------
    // Functions that check, modify, and resolve URIs and paths.
    //------------------------------------------------------------------------

    var ABSOLUTE_URI = /^[a-zA-Z][a-zA-Z\d\+\-\.]*:/;

    var ENTITIES_URI = /&#/;

    /**
     * Returns true if the specified value is non-null and begins with a scheme
     * (e.g., http:) or looks like an mangled email address (with entities).
     */
    function isAbsolute(uri) {
        return uri && (ABSOLUTE_URI.test(uri) || ENTITIES_URI.test(uri));
    }

    /**
     * Returns a relative version of the specified path by removing all leading
     * slashes.
     */
    function makeRelative(path) {
        if (!path) {
            return '';
        }
        var a = path.match(/^\/*(.*)/);
        return a[1];
    }

    /**
     * Resolves a path against a base path (RFC 3986 5.2.2). The
     * algorithm used is essentially the one specified in the RFC
     * beginning with the 'if (R.path == "") then' statement except
     * that it does not pay attention to any query components.
     */
    function resolve(base, path) {
        var resolvedPath;
        if (!path) {
            resolvedPath = base;
        } else if (path.charAt(0) === '/') {
            resolvedPath =  removeDotSegments(path);
        } else {
            resolvedPath = mergePaths(base, path);
            resolvedPath = removeDotSegments(resolvedPath);
        }
        return resolvedPath;
    }

    /**
     * Merges a base path and a path (RFC 3986 5.2.3).
     */
    function mergePaths(base, path) {
        // Handle null or undefined arguments.
        if (base == null) {
            base = '';
        }
        if (path == null) {
            path = '';
        }
        // Get everything up to and including the last slash. The following
        // also handles the case when no slash is in the base. (The index will
        // be -1, which, after adding one, will result in an empty substring.)
        base = base.substring(0, base.lastIndexOf('/') + 1);
        // Merge the base and the path.
        return base + path;
    }

    /**
     * Handles . and .. segments in the specified path (RFC 3986 5.2.4).
     */
    function removeDotSegments(path) {
        var ib = path.split(/\/+/); // input buffer (array of segments)
        var ob = []; // output buffer
        var n = ib.length;
        for (var i = 0; i < n; i++) {
            var s = ib[i];
            if (s === '..') {
                // preserve leading slash (ob[0] is empty == false)
                if ((ob.length > 1) || (ob.length > 0 && ob[0])) {
                    ob.pop();
                }
            } else if (s !== '.') {
                ob.push(s);
            }
        }
        return ob.join('/');
    }

})(jQuery);