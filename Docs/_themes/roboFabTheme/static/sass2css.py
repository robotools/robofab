# [h] compile sass into css

import os

from nelson.modules.sass import compile_sass

base_folder = os.path.dirname(__file__)

for f in os.listdir(base_folder):
    name, ext = os.path.splitext(f)
    css_file = '%s.%s' % (name, ext)
    css_path = os.path.join(base_folder, css_file)
    if ext == '.sass':
        sass_path = os.path.join(base_folder, f)
        compile_sass(sass_path)
