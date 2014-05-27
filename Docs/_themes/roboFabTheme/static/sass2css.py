# [h] compile sass into css

import os
import subprocess

def compile_sass(sass_path):
    '''Compile a ``.sass`` file (and dependencies) into a single ``.css`` file.'''
    css_path = os.path.splitext(sass_path)[0] + '.css'
    subprocess.call(['sass', sass_path, css_path])

base_folder = os.path.dirname(__file__)

for f in os.listdir(base_folder):
    name, ext = os.path.splitext(f)
    css_file = '%s.%s' % (name, ext)
    css_path = os.path.join(base_folder, css_file)
    if ext == '.sass':
        sass_path = os.path.join(base_folder, f)
        compile_sass(sass_path)
