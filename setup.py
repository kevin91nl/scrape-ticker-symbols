from distutils.core import setup

setup(
    name='scrape-ticker-symbols',
    packages=['tickersymbols'],
    install_requires=[
        'beautifulsoup4==4.6.0',
        'lxml==3.8.0',
        'requests==2.18.1'
    ],
    version='0.5',
    description='Scrape all ticker symbols from a given URL.',
    author='Kevin Jacobs',
    author_email='mail@kevinjacobs.nl',
    url='https://github.com/kevin91nl/scrape-ticker-symbols',
    download_url='https://github.com/kevin91nl/scrape-ticker-symbols/archive/0.5.tar.gz',
    keywords=['ticker symbol', 'ticker', 'symbol', 'stock market', 'stock', 'scrape'],
    classifiers=[],
)
