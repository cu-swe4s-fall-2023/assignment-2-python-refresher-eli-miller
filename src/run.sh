#!/bin/bash


set -e
set -u
set -o pipefail


python print_fires.py --country "United States of America" --country_column 0 --result_column 3

set +e
# Stuff that I want to run even if there are errors
python print_fires.py --country "United States" --country_column 0 --result_column 3
python print_fires.py --country "United States of America" --country_column 0 --result_column 3 --file_name "data/forestfires.csv"

set -e

### Check pycodestyle
