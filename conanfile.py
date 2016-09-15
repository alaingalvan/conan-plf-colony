#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile

class plfColonyConan(ConanFile):  

    name = 'plf_colony'
    version = '3.61.0.0'
    license = 'zlib'
    url = 'git@github.com:alaingalvan/conan-plf-colony.git'
    settings = ('os', 'compiler', 'build_type', 'arch')
    exports = '*'

    foldername = 'plf_colony'
    builddir = ''

    def source(self):
        self.run('git clone https://github.com/mattreecebentley/plf_colony.git')

    def build(self):
        self.builddir = os.path.join(self.conanfile_directory, self.foldername)

    def package(self):
        self.copy(pattern='*.h', dst='include', src='%s' % self.builddir, keep_path=False)