def get_column(file_name, query_column, query_value, result_column=1,
               verbose=False, ):
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
        return None
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

                        return None

                    except Exception as e:
                        print(
                            f'Unknown error in column {result_column}, '
                            f'row {i_line}, {e}'
                        )

                        return None

    except FileNotFoundError:
        print(f'Could not find file {file_name}')
        return None

    return result


def get_country_names(filename):
    """print the country names from a csv file

    input:
        filename (str): name of the csv file

    returns:
        country_names (list): list of country names
    """
    try:
        with open(filename, 'r') as f:
            country_names = []

            for line in f:
                line = line.strip().split(',')
                country_name = line[0]

                if country_name not in country_names:
                    country_names.append(country_name)
    except FileNotFoundError:
        print(f'Could not find file {filename}')
        return None

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


def get_col_means(filename):
    """print the column means from a csv file

    input:
        filename (str): name of the csv file

    returns:
        col_means (list): list of column means
            """

    with open(filename, 'r') as f:
        col_means = []
        for line in f:
            line = line.strip().split(',')
            for i in range(len(line)):
                if i == 0:
                    continue
                else:
                    col_means.append(float(line[i]))
        col_means = np.mean(col_means)
    return col_means


def mean(numbers):
    """Calculate the mean of a list of numbers

    Args:
        numbers (list): List of numbers

    Returns:
        mean (float): Mean of the list of numbers
    """
    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate the median of a list of numbers

    Args:
        numbers (list): List of numbers

    Returns:
        median (float): Median of the list of numbers
            """
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers) / 2)] + numbers[
            int(len(numbers) / 2) - 1]) / 2
    else:
        return numbers[int(len(numbers) / 2)]


def std(numbers):
    """
    Calculate the standard deviation of a list of numbers

    Args:
        numbers (list): List of numbers

    Returns:
        std (float): Standard deviation of the list of numbers
    """

    return mean([(x - mean(numbers)) ** 2 for x in numbers]) ** 0.5


def get_column_index(col_name, filename='Agrofood_co2_emission.csv'):
    '''
    Find which column a given column name is in

    Args:
        col_name (str): Name of the column to search for

    Returns:
        col_index (int): Index of the column
    '''

    col_names = get_col_names(filename)

    for i, name in enumerate(col_names):
        if name == col_name:
            return i



