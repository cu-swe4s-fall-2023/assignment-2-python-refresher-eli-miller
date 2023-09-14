def get_column(file_name, query_column, query_value, result_column):
    with open (file_name, 'r') as f:
        result = []
        for line in f:
            line = line.strip().split(',')
            if line[query_column] == query_value:
                result.append(line[result_column])
    return result



