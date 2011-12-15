./csv_util -h file
./csv_util --help

./csv_util -l file.csv
./csv_util --list file.csv f1,f2
./csv_util --list file.csv f1,bad_f2
./csv_util --list bad_file.csv f1,f2
./csv_util -l

./csv_util -f
./csv_util -f file.csv
./csv_util --fields file.csv
./csv_util -f bad_file.csv

./csv_util -c file.csv
./csv_util --count file.csv
./csv_util --count file.csv --filter f1=r1,f2=r2
./csv_util --count file.csv --filter 
./csv_util --count file.csv --unique
./csv_util --count file.csv --unique f1,f2

./csv_util -a file.csv units 
./csv_util --aggregate file.csv units by f1,f2

./csv_util -g file.csv units by f1
./csv_util --graph

./csv_util -b
./csv_util --bad_flags
./csv_util
./csv_util no_flags

