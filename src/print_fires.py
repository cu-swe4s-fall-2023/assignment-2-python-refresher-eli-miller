import argparse

from my_utils import get_column


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--country',
                        type=str,
                        help='Country name',
                        required=True
                        )

    parser.add_argument('--country_column',
                        type=int,
                        help='Column number for county. Used as query column',
                        required=True
                        )

    parser.add_argument('--result_column',
                        type=int,
                        help='Column number for results',
                        required=True
                        )

    parser.add_argument('--file_name',
                        type=str,
                        help='File name',
                        default='Agrofood_co2_emission.csv',
                        required=False
                        )
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Print extra information',
                        default=False,
                        required=False
                        )

    args = parser.parse_args()

    country = args.country
    country_column = args.country_column
    result_column = args.result_column
    file_name = args.file_name
    verbose = args.verbose

    fires = get_column(file_name, country_column, country,
                       result_column=result_column, verbose=verbose)

    print(fires)


if __name__ == '__main__':
    main()
