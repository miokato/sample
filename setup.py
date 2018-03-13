from setuptools import setup, find_packages

setup(
    name='sample',
    version='0.0.1',
    description='Sample package',
    long_description='readme',
    author='Mio Kato',
    author_email='test@example.com',
    packages=find_packages(),
    install_requires=['requests'],
    dependency_links=['git+ssh://git@github.com/miokato/sample.git#egg=sample'],
    test_suite='tests',
)