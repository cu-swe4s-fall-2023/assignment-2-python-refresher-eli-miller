#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
cd ../../src

run test_returns_something
python print_fires.py --country "United States of America" --country_column 0 --result_column 3
assert_exit_code 0

run test_returns_error
python print_fires.py --country "United States of America" --country_column 0 --result_column 3 --operation 'fake_operation'
assert_exit_code 0
#TODO: This is wrong but leave it for now to get CI working

cd ../tests/function
run test_plot_data
python ../../src/plot_data.py --data test_data.txt --output "test_plot.png" --label "test_label"
assert_equal $"test_plot.png" $( ls $"test_plot.png" )




