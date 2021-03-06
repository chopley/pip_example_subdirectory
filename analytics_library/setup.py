from setuptools import setup

setup(
    name='py_dir_example',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Charles Copley',
    author_email='charles@cedar.com',
    license='BSD 2-clause',
    packages=['py_dir_example'],
    install_requires=[
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)