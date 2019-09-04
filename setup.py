from distutils.core import setup
setup(
  name = 'KSTLogger',
  packages = ['KSTLogger'], 
  version = '0.1.0',
  author = 'Patrick Burrus',
  author_email = 'Patrick.burrus@kochind.com',
  install_requires=[
        'kmt_logging @ git+https://bJAQDrHxT8G2nNGjW3xa@kochsource.io/kmt-frameworks/logging-frameworks/kmt-logging.git@0.2.108.1'
    ]
)