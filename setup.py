import os

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')


if os.path.exists('README.md'):
    with open('README.md') as f:
        long_description = f.read()
else:
    long_description = ''


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]

setup(
    name='carbonplan',
    description='CarbonPlan metapackage',
    long_description=long_description,
    python_requires='>=3.6',
    maintainer='Joe Hamman',
    maintainer_email='joe@carbonplan.org',
    url='https://github.com/carbonplan/carbonplan-python',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    package_dir={'carbonplan': 'carbonplan'},
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
)
