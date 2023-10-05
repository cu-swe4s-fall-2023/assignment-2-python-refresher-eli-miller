import argparse

import my_utils


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
    parser.add_argument('--operation',
                        type=str,
                        help='Operation to perform on returned list',
                        default=None,
                        required=False
                        )

    args = parser.parse_args()

    country = args.country
    country_column = args.country_column
    result_column = args.result_column
    file_name = args.file_name
    verbose = args.verbose
    operation = args.operation

    fires = my_utils.get_column(file_name, country_column, country,
                                result_column=result_column, verbose=verbose)

    # TODO: rewrite this more compactly with a .apply method
    # Should we be returning or just printing?
    if operation is None:
        print(fires)
    elif operation == 'mean':
        print(my_utils.mean(fires))
    elif operation == 'median':
        print(my_utils.median(fires))
    elif operation == 'std':
        print(my_utils.std(fires))
    else:
        print(
            ' Operation not implemented in my_utils. Available operations are '
            '"mean", "median", "std"')
        exit(1)


if __name__ == '__main__':
    main()
