pycodestyle style.py

pycodestyle get_column_stats.py

# Test for random inputs
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
python get_column_stats.py --file_name data.txt --col_num 2

# Test for static input
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt
python get_column_stats.py --file_name data.txt --col_num 2

# Test error handling for non-existent column
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
python get_column_stats.py --file_name data.txt --col_num 666

# Test error handling for invalid column input
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\tA";
done )> data.txt
python get_column_stats.py --file_name data.txt --col_num 2

# Test error handling for bad file path
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
python get_column_stats.py --file_name bad_file.txt --col_num 2

# Test error handling for zero division
(for i in `seq 1 0`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
python get_column_stats.py --file_name data.txt --col_num 2
