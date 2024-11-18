import os
import codecs
from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            # __version__ = "1.x.x"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def _fetch_requirements(path: str) -> list:
    requirements = []
    with open(path) as f:
        for r in f:
            r = r.strip()
            if r.startswith('-r'):
                assert len(r.split()) == 2
                requirements.extend(_fetch_requirements(r.split()[-1]))
            else:
                requirements.append(r)
    return requirements


setup(
    name='airtest-openwsgr',
    version=get_version("airtest/utils/version.py"),
    author='Netease Games',
    author_email='rockywhisper@163.com',
    description='UI Test Automation Framework for Games and Apps on Android/iOS/Windows/Linux',
    long_description='UI Test Automation Framework for Games and Apps on Android/iOS/Windows, present by NetEase Games',
    url='https://github.com/AirtestProject/Airtest',
    license='Apache License 2.0',
    keywords=['automation', 'automated-test', 'game', 'android', 'ios', 'windows', 'linux'],
    packages=find_packages(exclude=['cover', 'playground', 'tests', 'dist']),
    package_data={
        'android_deps': ["*.apk", "airtest/core/android/static"],
        'html_statics': ["airtest/report"],
        'ios_deps': ["airtest/core/ios/iproxy"],
    },
    include_package_data=True,
    install_requires=_fetch_requirements('requirements.txt'),
    extras_require={
        'tests': [
            'nose',
        ],
        'docs': [
            'sphinx',
            'recommonmark',
            'sphinx_rtd_theme',
            'mock',
        ]},
    entry_points="""
    [console_scripts]
    airtest = airtest.cli.__main__:main
    """,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
