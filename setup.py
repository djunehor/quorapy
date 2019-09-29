try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r', encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='quorapy',
    version='0.1.0',
    description='Fetches and parses data from Quora.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zacchaeus Bolaji',
    author_email='djunehor@gmail.com',
    url='https://github.com/djunehor/quorapy',
    packages=['quorapy'],
    install_requires=[
        "beautifulsoup4",
        "feedparser",
        "dateparser",
        "selenium",
        "lxml"
    ]
)
