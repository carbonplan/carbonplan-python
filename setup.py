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
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Scientific/Engineering',
]

extras_require = {
    'all': ['carbonplan-data', 'carbonplan-styles', 'carbonplan-forest-risks'],
    'data': ['carbonplan-data'],
    'forest-offsets': ['carbonplan-forest-offsets'],
    'forest-risks': ['carbonplan-forest-risks'],
    'styles': ['carbonplan-styles'],
}

setup(
    name='carbonplan',
    description='CarbonPlan namespace package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    maintainer='Joe Hamman',
    maintainer_email='joe@carbonplan.org',
    url='https://github.com/carbonplan/carbonplan-python',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=CLASSIFIERS,
    use_scm_version={"version_scheme": "post-release", "local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm", "setuptools>=30.3.0", "setuptools_scm_git_archive"],
)
