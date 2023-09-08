
# a. get_column() opens the file named file_name and processes it line by line
# b. for each line
# i. split the line into an array
# ii. check to see if the value in the query_column position of the array matches the value
# stored in the query_value variable
# iii. when the above condition is met, add the value in the result_column position to an
# array
# c. return the array storing the column values

def get_column(file_name, query_column, query_value, result_column):
    with open (file_name, 'r') as f:
        result = []
        for line in f:
            line = line.strip().split(',')
            if line[query_column] == query_value:
                result.append(line[result_column])
    return result



