from setuptools import setup, find_packages

setup(
    name='sample',
    version='0.0.1',
    description='Sample package',
    long_description='readme',
    author='Mio Kato',
    author_email='test@example.com',
    packages = find_packages(),
    test_suite='tests',
)