from setuptools import setup, find_packages

setup(
    name='awesomecure',
    version='1.0.0',
    url='https://github.com/protontypes/sustainbeat.git',
    description='Analyze and cure awesome lists by mining data from listed Git projects',
    packages=find_packages(),
    install_requires=['termcolor', 'beautifulsoup4', 'markdown', 'pygithub', 'python-dotenv'],
)
