#!/bin/bash


set -e
set -u
set -o pipefail


python print_fires.py --country "United States of America" --country_column 0 --result_column 3
python print_fires.py --country "United States of America" --country_column 0 --result_column 3 --operation 'std'


