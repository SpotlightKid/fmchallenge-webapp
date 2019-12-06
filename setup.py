#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# setup.py - Setup file for the fmchallenge-webapp Flask app
#

# Standard library modules
import distutils
import subprocess
from os.path import dirname, join

# Third-party modules
from setuptools import find_packages, setup


install_requires = [line.strip() for line in """\
    Flask
    MarkupSafe
    Werkzeug
    Jinja2
    itsdangerous
    click>=5.0
    Flask-SQLAlchemy
    SQLAlchemy
    Flask-Migrate
    Flask-Mail
    Flask-Misaka
    Flask-PageDown
    Flask-WTF
    WTForms
    gunicorn>=19.1.1
    Flask-Login
    Flask-Bcrypt
    Flask-Caching>=1.0.0
    Flask-DebugToolbar
    environs
    internetarchive
""".splitlines() if line.strip() and not line.strip().startswith('#')]

tests_require = [
    # intentionally left empty, test requirements are declared in tox.ini!
]

classifiers = [c.strip() for c in """\
    Development Status :: 4 - Beta
    Environment :: Web Environment
    Framework :: Flask
    Intended Audience :: Developers
    Intended Audience :: End Users/Desktop
    License :: OSI Approved :: MIT License
    Operating System :: POSIX
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Topic :: Internet :: WWW/HTTP :: WSGI :: Application
    Topic :: Multimedia :: Sound/Audio
""".splitlines() if c.strip() and not c.strip().startswith('#')]


def read(*args):
    return open(join(dirname(__file__), *args)).read()


class ToxTestCommand(distutils.cmd.Command):
    """Distutils command to run tests via tox with 'python setup.py test'.

    Please note that in this configuration tox uses the dependencies in
    `requirements/dev.txt`, the list of dependencies in `tests_require` in
    `setup.py` is ignored!

    See https://docs.python.org/3/distutils/apiref.html#creating-a-new-distutils-command
    for more documentation on custom distutils commands.

    """
    description = "Run tests via 'tox'."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce("Running tests with 'tox'...", level=distutils.log.INFO)
        return subprocess.call(['tox'])


setup(
    name='FMChallenge-WebApp',
    version='0.1.0',
    keywords='webapp,flask,competition,osamc,fm synthesis',
    author='Christopher Arndt',
    author_email='chris@chrisarndt.de',
    url='https://github.com/SpotlightKid/fmchallenge-webapp',
    license='MIT License',
    description='Dynamic part of the web site for the Open Source FM Synthesizer Challenge',
    classifiers=classifiers,
    long_description=read('README.rst'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': ToxTestCommand},
    zip_safe=False
)
