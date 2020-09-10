from distutils.core import setup
setup(
  name = 'homograph',
  packages = ['homograph'],
  version = '1.2',
  license='MIT',
  description = 'IDN Homograph detection tools',
  author = 'Alex Alvarado',
  author_email = 'alex@flowcrypt.com',
  url = 'https://github.com/flowcrypt/idn-homographs-database',
  # Note: The below release doesn't exist until after this code is merged
  download_url = 'https://github.com/flowcrypt/idn-homographs-database/archive/1.2.tar.gz',
  keywords = ['IDN', 'homograph', 'attack', 'security'],
  install_requires = [],
  include_package_data = True,
  package_data={'homograph': ['homographs.json']},
  classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Security',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
