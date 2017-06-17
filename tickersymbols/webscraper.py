"""
Script for scraping ticker symbols from a given URL.

@author     K.M.J. Jacobs
@date       2017-06-16
@url        https://www.data-blogger.com/
"""

from argparse import ArgumentParser
import requests
import re
from bs4 import BeautifulSoup


def get_symbols_from_url(url, treshold_ratio_uppercase=0.9, treshold_ratio_digit=0.0):
    """
    Given an URL, return a list of symbols found in table columns containing only ticker symbols.

    :param url: URL to find the ticker symbols in.
    :param treshold_ratio_uppercase: Minimum ratio of uppercased strings in a ticker symbol column.
    :param treshold_ratio_digit: Maximum ratio of strings containing digits in a ticker symbol column.
    :return: List of ticker symbols.
    """
    # Fetch the HTML
    response = requests.get(url)
    html = response.content

    # Parse the HTML
    return get_symbols_from_html(html, treshold_ratio_uppercase, treshold_ratio_digit)


def get_symbols_from_html(html, treshold_ratio_uppercase=0.9, treshold_ratio_digit=0.0):
    """
    Given HTML, return a list of symbols found in table columns which contain only ticker symbols (here defined as
    uppercased strings containing no digits).

    :param html: The HTML to find the symbols in.
    :param treshold_ratio_uppercase: Minimum ratio of uppercased strings in a ticker symbol column.
    :param treshold_ratio_digit: Maximum ratio of strings containing digits in a ticker symbol column.
    :return: List of ticker symbols.
    """
    soup = BeautifulSoup(html, 'lxml')
    symbols = []

    # Loop through all tables
    for table in soup.find_all('table'):
        column_data = []
        column_metadata = []

        # Loop through all rows
        for tr in table.find_all('tr'):

            # And now loop through all cells
            for cell_count, td in enumerate(tr.find_all('td')):
                # Add new column if the column is encountered for the first time
                if len(column_data) <= cell_count:
                    column_data.append([])
                    column_metadata.append({
                        'num_rows': 0,  # Number of rows
                        'num_uppercased': 0,  # Number of rows containing uppercased strings
                        'num_digit': 0,  # Number of rows containing digits
                    })

                # Strip whitespace
                contents = td.text.strip()
                column_data[cell_count].append(contents)

                # Increment the counts
                column_metadata[cell_count]['num_rows'] += 1
                column_metadata[cell_count]['num_uppercased'] += 1 if contents == contents.upper() else 0
                column_metadata[cell_count]['num_digit'] += 1 if re.match(r'[0-9]+', contents) else 0

        # Now loop through all the data and meta data
        for data, metadata in zip(column_data, column_metadata):
            # Compute the ratio of rows containing uppercased strings
            ratio_uppercased = float(metadata['num_uppercased']) / float(metadata['num_rows'])
            # Compute the ratio of rows containing digits
            ratio_digit = float(metadata['num_digit']) / float(metadata['num_rows'])

            # If there are many uppercased strings and almost no strings with digits, then we possibly found a ticker
            # symbol column
            if ratio_uppercased > treshold_ratio_uppercase and ratio_digit <= treshold_ratio_digit:
                # Loop through all the items in the column
                for raw_item in data:
                    # Ensure a correct encoding for the ticker symbol
                    item = raw_item if isinstance(raw_item, str) else raw_item.encode('utf-8')

                    # Only add uppercased strings and make sure that there are no duplicates
                    if item not in symbols and item.upper() == item:
                        symbols.append(item)

    # Give back the results
    return symbols


if __name__ == '__main__':
    # Fetch the arguments
    parser = ArgumentParser(description='Scrape all ticker symbols from a given URL.')
    parser.add_argument('url', help='The URL to scrape.')
    parser.add_argument('--separator', help='The separator between symbols.', default=',')
    parser.add_argument('--treshold-uppercase',
                        help='Minimum ratio of uppercased strings in a ticker symbol column.',
                        type=float,
                        default=0.9)
    parser.add_argument('--treshold-digit',
                        help='Maximum ratio of strings containing digits in a ticker symbol column.',
                        type=float,
                        default=0.0)
    args = parser.parse_args()

    # Print out the found symbols
    print(args.separator.join(get_symbols_from_url(args.url, args.treshold_uppercase, args.treshold_digit)))
