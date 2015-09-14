try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'archive, backup and exchange in a parseable and human readable format, using simple tools',
    'author': 'Pieterjan Montens',
    'url': '',
    'download_url': '',
    'version': '0.1.dev',
    'install_requires': ['nose'],
    'packages': ['abe-h'],
    'scripts': [],
    'name': 'abe+h'
}

setup(**config)
