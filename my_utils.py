def get_column(file_name, query_column, query_value, result_column=1,
               verbose=False):
    """Get a column from a csv file based on a query value in another column

    Args:
        file_name (str): Name of the csv file
        query_column (int): Column number for the query
        query_value (str): Value to query for
        result_column (int): Column number for the result

    Returns:
        result (list): List of integer results
    """
    # Check if the provided country is in the file
    country_names = get_country_names(file_name)
    if query_value not in country_names:
        print(f'{query_value} not in {file_name}.')
        exit(1)
    # Catch file not found errors
    try:
        with open(file_name, 'r') as f:

            result = []

            if verbose:
                # Print an overview of the file to the user
                header = f.readline().strip().split(',')
                print(
                    f'Getting {header[result_column]} '
                    f'from {file_name} '
                    f'where {header[query_column]} '
                    f'is {query_value}'
                )

            for i_line, line in enumerate(f):
                line = line.strip().split(',')
                if line[query_column] == query_value:
                    return_val = line[result_column]

                    # If the result is a number, convert it to an int. Catch
                    # errors
                    try:
                        return_val = round(float(return_val))
                        result.append(return_val)

                    except ValueError as e:

                        print(
                            f'Could not convert {return_val} '
                            f'to int in column {result_column}, '
                            f'row {i_line}, {e}'
                        )

                        exit(1)

                    except Exception as e:
                        print(
                            f'Unknown error in column {result_column}, '
                            f'row {i_line}, {e}'
                        )

                        exit(1)

    except FileNotFoundError:
        print(f'Could not find file {file_name}')
        exit(1)

    return result


def get_country_names(filename):
    """print the country names from a csv file

    input:
        filename (str): name of the csv file

    returns:
        country_names (list): list of country names
    """

    with open(filename, 'r') as f:
        country_names = []

        for line in f:
            line = line.strip().split(',')
            country_name = line[0]

            if country_name not in country_names:
                country_names.append(country_name)

    return country_names


def get_col_names(filename):
    """print the column names from a csv file

    input:
        filename (str): name of the csv file

    returns:
        col_names (list): list of column names

    """

    with open(filename, 'r') as f:
        col_names = f.readline().strip().split(',')

    return col_names
