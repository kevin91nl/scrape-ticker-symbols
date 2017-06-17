# Scrape Ticker Symbols

Scrape ticker symbols from an URL. The script is compatible with Python 2 and Python 3.

## Installation

Simply execute the following:

```
pip install scrape-ticker-symbols
```

## Usage examples


### S&P 500 index

Fetch S&P 500 index ticker symbols:

```
from tickersymbols.webscraper import get_symbols_from_url

print(get_symbols_from_url('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'))
```

The output:
```
['MMM', 'ABT', 'ABBV', 'ACN', 'ATVI', 'AYI', 'ADBE', ...]
```

### AEX index


Fetch AEX index ticker symbols:

```
from tickersymbols.webscraper import get_symbols_from_url

print(get_symbols_from_url('https://en.wikipedia.org/wiki/AEX_index'))
```

The output:
```
['AALB', 'ABN', 'AGN', 'ADRNY', 'AKZA', 'ATC', 'MT', ...]
```