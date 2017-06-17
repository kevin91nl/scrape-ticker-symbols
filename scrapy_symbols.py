from argparse import ArgumentParser
from tickersymbols.webscraper import get_symbols_from_url

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
