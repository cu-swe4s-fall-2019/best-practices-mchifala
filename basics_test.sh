test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

pycodestyle basic_test.py
pycodestyle get_column_stats.py

# Generate static input
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

# Test for static input
run test_static python get_column_stats.py --file_name data.txt --col_num 2
assert_in_stdout "mean: 1"
assert_in_stdout "stdev: 0"
assert_no_stderr
assert_exit_code 0

# Test error handling for non-existent column
run test_no_column python get_column_stats.py --file_name data.txt --col_num 666
assert_exit_code 1
assert_in_stdout "Column number does not exist in data file."

# Test error handling for bad file path
run test_bad_file python get_column_stats.py --file_name bad_file.txt --col_num 2
assert_exit_code 1
assert_in_stdout "Data file not found. Please check file name and directory."

# Generate invalid column input
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\tA";
done )> data.txt

# Test error handling for invalid column input
run test_invalid_input python get_column_stats.py --file_name data.txt --col_num 2
assert_exit_code 1
assert_in_stdout "Data file contains a value with invalid input type."

# Generate empty input
rm data.txt
touch data.txt

# Test error handling for empty column input
run test_empty_input python get_column_stats.py --file_name data.txt --col_num 2
assert_exit_code 1
assert_in_stdout "Column is empty. Cannot perform calculations"

#Test for random inputs
for i in {1..100}
do
    for i in {1..1000} 
    do 
        echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM"; done > data.txt
    mean=$(awk '{ total += $1 } END { print total/NR }' data.txt)
    std=$(awk '{sum += $1; sumsq += $1*$1} END {print sqrt(sumsq/NR - (sum/NR)*(sum/NR))}' data.txt)
    run test_random python get_column_stats.py --file_name data.txt --col_num 0
    assert_exit_code 0
    assert_in_stdout $mean
    assert_no_stderr
    assert_in_stdout $std
    done
done