# Best Practices
V1.0: The goal of this assignment is to become familiar with Python best practices including PEP8 styling, handling input parameters with argparse, using main functions, handling exceptions, documenting code, and writing an effective README.md. 

V2.0: The goal of this assignment is to add unit and functional testing to the code in V1.0. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following packages were used during the development of this code. Other versions may be supported, but cannot be guaranteed.

- python (version 3.7.0)
- pycodestyle (version 2.5.0)
- ssshtest 

### Installation

The following steps will help you set up the proper environment on your machine. All example commands are entered directly into terminal.

**Installing conda:**

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

**Creating conda environment:**

```
conda create --yes -n <your_environment>
conda install --yes python=3.7
```

**Activating conda environment:**

```
conda activate <your_environment>
```

**Installing pycodestyle:**

pycodestyle is used to ensure that all .py files adhere to the PEP8 style guidelines.

```
conda install -y pycodestyle
```

**Installiing ssshtest**

sshtest is a library developed by Ryan Layer that provides a simple framework for testing command-line programs in a bash script

```
test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest. ssshtest
```

### Examples
get_column_stats.py calculates the mean and standard deviation for elements in the column of a data file.

```
python get_column_stats.py --file_name <your_file.txt> --col_num <your_column_number>
```

basic_test.py runs several unit tests on the mean and standard deviation functions in get_column_stats.py to test both accuracy and proper error handling.

```
python basic_test.py
```

Updated: basics_test.sh is a test script that uses the ssshtest libary to run functional tests on get_column_stats.py over several inputs to demonstrate functionality and error handling. It also checks style.py and get_column_stats.py for adherence to PEP8 style guidelines. 

```
bash basics_test.sh
```

## Authors

**Michael W. Chifala** - University of Colorado, Boulder, CSCI 7000: Software Engineering for Scientists


## Acknowledgments

* Ryan Layer's "Development Environment" document
* ssshtest: https://github.com/ryanlayer/ssshtest
* PEP8 Style Guidelines: https://www.python.org/dev/peps/pep-0008/
* Github: PurpleBooth/README-Template.md
* Stack Overflow: https://stackoverflow.com/questions/15101343/standard-deviation-of-an-arbitrary-number-of-numbers-using-bc-or-other-standard
