[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)

_Functionality to read in the AGRO Food dataset and extract information_

This should demonstrate one successful and two unsuccessful runs of the script.


## Installation Instructions
1. Clone the repository

```git clone https://github.com/cu-swe4s-fall-2023/assignment-2-python-refresher-eli-miller```

2. Get the `Agrofood_co2_emissions.csv` from Google Drive and place it in the `src/` directory
3. Navigate into the source directory

```cd src```
4. Run the script using the bash file

```run.sh```



## Usage
`print_fires` takes a target country and column number and returns integer rounded values of the annual 
CO<sub>2</sub> emissions from fires in that country.

Command line arguments:
* `--country_column`  - The column number of the country column
* `--country` - The country to query
* `--result_column` - The column number of the column to return values from
* `--file_name` - The path to the dataset file. 
  * This script will run from /src/ so ensure to use relative paths to get to the dataset.
* `--verbose` (optional) - Print out what the function is doing to the user

Examples:
```bash
python print_fires.py --country "United States of America" --country_column 0 --result_column 3
```

## Helper Functions
`get_country_names` returns a list of all country names in the dataset. Helpful for debugging.

`get_col_names` returns a list of the column names in the dataset. The position of the column name in the list is 
the input parameter for `get_column`.



