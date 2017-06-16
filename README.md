# Scrape Ticker Symbols

Scrape ticker symbols from an URL. The script is compatible with Python 2 and Python 3.

## Installation

Install the dependencies:

```
pip install -r requirements.txt
```

## Usage examples


### S&P 500 index

Fetch S&P 500 index ticker symbols:

```
python scrape_symbols.py https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
```

The output:
```
MMM
ABT
ABBV
ACN
ATVI
AYI
ADBE
...
```

### AEX index


Fetch AEX index ticker symbols:

```
python scrape_symbols.py https://en.wikipedia.org/wiki/AEX_index
```

The output:
```
AALB
ABN
AGN
ADRNY
AKZA
ATC
MT
...
```