"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='gametheory',
    version='1.0p3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'gametheory.audio': ['*.wav']},
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    python_requires='>=3.6',
    install_requires=['cryptography', 'playsound'],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': ['gametheory=gametheory.main:main'],
    }
)
