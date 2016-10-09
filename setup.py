# coding: utf-8
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)

        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(name="Tests Tout-Terrain",
      version="1.0",
      description="Tests Tout-terrain",
      author="Pierre Bousquié",
      author_email="pierre@yaal.fr",
      packages=['TTT'],
      install_requires=["werkzeug"],
      tests_require=['tox'],
      cmdclass= {'test': Tox },
      )

