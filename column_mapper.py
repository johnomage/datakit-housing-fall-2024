import csv


def map_column_names(file_path: str):
    """
        Reads a dictionary.csv file and creates a dictionary where the keys are taken from the first column 
        and the values are from the second column of each row.

        Parameters:
            file_path (str): The path to the CSV file to be read.

        Returns:
            dict: A dictionary where the keys are from the first column and the values from the second column of the CSV.
    """
    column_dict = {}

    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        # skip header
        next(reader)
        # loop all column names
        for row in reader:
            column_dict[row[0]] = row[1] # column name, meaning

    return column_dict


# map_column(os.getenv('data_dictionary_1_CA'))
