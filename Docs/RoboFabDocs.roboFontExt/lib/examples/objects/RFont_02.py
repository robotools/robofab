# cache the kerning object for speed

from robofab.world import CurrentFont

f = CurrentFont()

cachedKerning = f.kerning
# continue to use cachedKerning, not f.kerning.