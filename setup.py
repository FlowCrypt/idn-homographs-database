from distutils.core import setup
setup(
  name = 'homograph',
  packages = ['homograph'],
  version = '0.01',
  license='MIT',
  description = 'IDN Homograph detection tools',
  author = 'Alex Alvarado',
  author_email = 'alex@flowcrypt.com',
  url = 'https://github.com/flowcrypt/idn-homograph-database',
  # Note: The below release doesn't exist yet!
  download_url = 'https://github.com/FlowCrypt/idn-homographs-database/archive/0.01.tar.gz',
  keywords = ['IDN', 'homograph', 'attack', 'security'],
  install_requires=[],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Security',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
