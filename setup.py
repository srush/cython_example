from distutils.core import setup
from distutils.extension import Extension
import os.path
from Cython.Distutils import build_ext

ext_modules = [ ]
cmdclass = {}


ext_modules = [Extension("example.test",
                         ["example/test.pyx",
                          "src/test.cpp"],
                         language='c++',
                         include_dirs=[r'src/', ".", "../decoding/src/"],
                         #extra_compile_args=["-O2","-ggdb"], #'-O2',
                         )]

cmdclass = {'build_ext': build_ext}

setup(
  name = 'example',
  cmdclass = cmdclass,
  packages=['example'],
  package_dir={'example': 'example/'},
  ext_modules = ext_modules,
  requires=[],
  version = '0.1',
  description = 'A test cython',
  author = '',
  author_email = '',
  keywords = ['nlp'], # arbitrary keywords
  classifiers = []
)
