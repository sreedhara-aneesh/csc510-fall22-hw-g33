# CSC510 HW 1 (Group 33): Write a "good" Github Repo


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7033329.svg)](https://doi.org/10.5281/zenodo.7033329)
[![Build Status](https://app.travis-ci.com/sreedhara-aneesh/csc510-fall22-hw-g33.svg?branch=main)](https://app.travis-ci.com/sreedhara-aneesh/csc510-fall22-hw-g33)
[![GitHub issues](https://img.shields.io/github/issues/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/issues)
[![GitHub forks](https://img.shields.io/github/forks/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/network/members)
[![GitHub stars](https://img.shields.io/github/stars/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/stargazers)
[![GitHub license](https://img.shields.io/github/license/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/blob/main/LICENSE.md)



## Functionality

-  Our project takes a working system (written in LUA) and converted it into python code.

- This code reads a CSV file and generates summaries of columns (medians and standard deviation for numerics; mode and entropy for symbolic columns).

- Csv files we use have `:+-` in their first line and upper and lower case in column names. Thes csv files contain lots of X,Y examples.

    The function `Y=F(X)` computes dependent variables Y from independent variables X. Some variables are `Numeric` (which we denote with a leading upper case letter) and some are `Symbolic`. Some dependent variables need to maximized (denoted with a trailing `-` sign) and other need to be maximized (denoted with a trailing `+`). And `:` denotes a column to skip

    Example csv file is seen [here](https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv)

- Five classes: `Data`, `Cols`, `Sym`, `Num`, `Row`.

- A `cli` function that can update  `the` and a help string that can be displayed with `-h`.


## Code Coverage

Coverage reported in Travis log 

Example:

| Name         | Stmts | Miss | Branch | BrPart | Cover | Missing          |
|--------------|-------|------|--------|--------|-------|------------------|
| src/cols.py  | 18    | 18   | 10     | 0      | 0%    | 1-23             |
| src/data.py  | 29    | 29   | 12     | 0      | 0%    | 6-45             |
| src/num.py   | 37    | 0    | 10     | 1      | 98%   | 33->exit         |
| src/row.py   | 3     | 3    | 2      | 0      | 0%    | 2-4              |
| src/sym.py   | 25    | 0    | 12     | 2      | 95%   | 16->exit, 34->33 |
| src/the.py   | 36    | 36   | 12     | 0      | 0%    | 3-65             |
| src/utils.py | 13    | 13   | 4      | 0      | 0%    | 1-15             |
| TOTAL        | 161   | 99   | 62     | 3      | 36%   |                  |


## Unit tests

Our test engine that automatically runs all files under the test directory with pattern test_* and runs all methods within them with pattern test_* and outputs the results.

## Installation

Please check [INSTALL.md](INSTALL.md) for instructions on how to install this package. 

## Usage

Please check [README.md](test/README.md) in the test folder for instructions on how to run the test cases.

--- 