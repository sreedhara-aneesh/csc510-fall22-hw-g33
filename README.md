# CSC510 HW 1 (Group 33): Write a "good" Github Repo


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7127619.svg)](https://doi.org/10.5281/zenodo.7127619)
[![Unit test](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/actions/workflows/unit-test.yml/badge.svg)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/actions/workflows/unit-test.yml)
[![GitHub issues](https://img.shields.io/github/issues/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/issues)
[![GitHub forks](https://img.shields.io/github/forks/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/network/members)
[![GitHub stars](https://img.shields.io/github/stars/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/stargazers)
[![GitHub license](https://img.shields.io/github/license/sreedhara-aneesh/csc510-fall22-hw-g33)](https://github.com/sreedhara-aneesh/csc510-fall22-hw-g33/blob/main/LICENSE.md)
[![Docs](https://img.shields.io/badge/Read_Documentation-blue.svg)](https://sreedhara-aneesh.github.io/csc510-fall22-hw-g33/src.html)

## Functionality

-  Our project takes a working system (written in LUA) and converted it into python code.

- This code reads a CSV file and generates summaries of columns (medians and standard deviation for numerics; mode and entropy for symbolic columns).

- Csv files we use have `:+-` in their first line and upper and lower case in column names. Thes csv files contain lots of X,Y examples.

    The function `Y=F(X)` computes dependent variables Y from independent variables X. Some variables are `Numeric` (which we denote with a leading upper case letter) and some are `Symbolic`. Some dependent variables need to maximized (denoted with a trailing `-` sign) and other need to be maximized (denoted with a trailing `+`). And `:` denotes a column to skip

    Example csv file is seen [here](https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv)

- Five classes: `Data`, `Cols`, `Sym`, `Num`, `Row`.

- A `cli` function that can update  `the` and a help string that can be displayed with `-h`.


## Code Coverage

Coverage reported in Github Actions log 


```py
Name               Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------
src/__init__.py        0      0      0      0   100%
src/cols.py           29      2     13      1    93%   34, 37
src/dataclass.py      65     13     36      7    74%   40-48, 75->71, 82, 83->79, 91, 94, 101, 112-113, 116
src/num.py            38      0     10      1    98%   33->exit
src/row.py             7      1      2      0    89%   16
src/sym.py            26      0     12      2    95%   16->exit, 35->34
src/the.py            87     21     32      2    67%   97, 99->exit, 113-133
src/utils.py          13      0      4      0   100%
--------------------------------------------------------------
TOTAL                265     37    109     13    81%
```

## Unit tests

Our test engine that automatically runs all files under the test directory with pattern test_* and runs all methods within them with pattern test_* and outputs the results.

## Installation

Please check [INSTALL.md](INSTALL.md) for instructions on how to install this package. 

## Usage

Please check [README.md](test/README.md) in the test folder for instructions on how to run the test cases.

## Test case output 
```py
test_num.py/test_bignum
[528.0, 877.0, 711.0, 919.0, 983.0, 6.0, 7.0, 593.0, 784.0, 10.0, 870.0, 12.0, 692.0, 543.0, 15.0, 762.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 949.0, 26.0, 521.0, 628.0, 601.0, 520.0, 31.0, 929.0, 33.0, 34.0, 976.0, 883.0, 37.0, 878.0, 39.0, 957.0, 41.0, 42.0, 43.0, 953.0, 677.0, 894.0, 47.0, 913.0, 859.0, 845.0, 51.0, 680.0, 53.0, 524.0, 55.0, 968.0, 57.0, 795.0, 59.0, 60.0, 566.0, 62.0, 821.0, 64.0, 65.0, 66.0, 67.0, 952.0, 710.0, 70.0, 71.0, 942.0, 992.0, 584.0, 75.0, 896.0, 560.0, 78.0, 79.0, 558.0, 81.0, 82.0, 987.0, 84.0, 85.0, 666.0, 816.0, 695.0, 89.0, 652.0, 998.0, 517.0, 93.0, 94.0, 898.0, 96.0, 753.0, 98.0, 731.0, 100.0, 101.0, 102.0, 103.0, 104.0, 955.0, 106.0, 107.0, 108.0, 943.0, 110.0, 111.0, 112.0, 113.0, 587.0, 874.0, 715.0, 117.0, 774.0, 119.0, 120.0, 121.0, 941.0, 123.0, 124.0, 759.0, 126.0, 127.0, 128.0, 129.0, 130.0, 675.0, 132.0, 948.0, 134.0, 592.0, 809.0, 137.0, 138.0, 996.0, 608.0, 141.0, 604.0, 143.0, 144.0, 145.0, 146.0, 986.0, 674.0, 782.0, 972.0, 966.0, 152.0, 833.0, 758.0, 155.0, 763.0, 872.0, 158.0, 159.0, 861.0, 161.0, 162.0, 572.0, 951.0, 165.0, 166.0, 167.0, 766.0, 542.0, 581.0, 171.0, 172.0, 173.0, 174.0, 667.0, 770.0, 818.0, 960.0, 179.0, 180.0, 181.0, 182.0, 183.0, 988.0, 185.0, 186.0, 187.0, 626.0, 189.0, 190.0, 191.0, 964.0, 868.0, 194.0, 912.0, 196.0, 527.0, 525.0, 975.0, 200.0, 772.0, 202.0, 203.0, 204.0, 681.0, 950.0, 834.0, 518.0, 209.0, 210.0, 211.0, 212.0, 901.0, 214.0, 215.0, 664.0, 217.0, 937.0, 219.0, 682.0, 221.0, 620.0, 223.0, 669.0, 225.0, 900.0, 227.0, 532.0, 657.0, 850.0, 961.0, 924.0, 958.0, 807.0, 573.0, 514.0, 237.0, 238.0, 590.0, 240.0, 241.0, 596.0, 243.0, 564.0, 245.0, 246.0, 247.0, 745.0, 709.0, 250.0, 251.0, 252.0, 649.0, 537.0, 653.0, 256.0, 723.0, 258.0, 259.0, 260.0, 926.0, 777.0, 263.0, 713.0, 812.0, 717.0, 605.0, 817.0, 269.0, 991.0, 271.0, 936.0, 273.0, 743.0, 798.0, 276.0, 277.0, 974.0, 897.0, 619.0, 281.0, 282.0, 857.0, 790.0, 285.0, 902.0, 287.0, 288.0, 289.0, 290.0, 291.0, 513.0, 865.0, 294.0, 295.0, 296.0, 887.0, 298.0, 698.0, 610.0, 301.0, 630.0, 885.0, 740.0, 305.0, 306.0, 576.0, 873.0, 309.0, 310.0, 631.0, 312.0, 735.0, 523.0, 315.0, 931.0, 598.0, 567.0, 319.0, 844.0, 321.0, 322.0, 323.0, 324.0, 909.0, 701.0, 661.0, 989.0, 329.0, 330.0, 331.0, 545.0, 333.0, 978.0, 944.0, 336.0, 820.0, 884.0, 339.0, 822.0, 341.0, 342.0, 343.0, 984.0, 641.0, 645.0, 722.0, 679.0, 819.0, 350.0, 915.0, 352.0, 353.0, 769.0, 888.0, 356.0, 357.0, 358.0, 359.0, 739.0, 361.0, 775.0, 726.0, 617.0, 946.0, 366.0, 367.0, 552.0, 881.0, 803.0, 982.0, 761.0, 993.0, 928.0, 538.0, 685.0, 377.0, 905.0, 379.0, 380.0, 381.0, 382.0, 815.0, 843.0, 385.0, 871.0, 387.0, 589.0, 911.0, 660.0, 632.0, 930.0, 393.0, 394.0, 733.0, 869.0, 639.0, 398.0, 724.0, 400.0, 401.0, 402.0, 403.0, 892.0, 650.0, 575.0, 407.0, 408.0, 699.0, 662.0, 411.0, 412.0, 413.0, 414.0, 415.0, 811.0, 417.0, 418.0, 751.0, 420.0, 421.0, 422.0, 423.0, 424.0, 746.0, 426.0, 427.0, 428.0, 515.0, 430.0, 431.0, 890.0, 433.0, 434.0, 687.0, 773.0, 940.0, 658.0, 917.0, 625.0, 985.0, 591.0, 443.0, 444.0, 445.0, 446.0, 981.0, 448.0, 449.0, 450.0, 704.0, 824.0, 453.0, 781.0, 455.0, 456.0, 754.0, 891.0, 893.0, 460.0, 461.0, 462.0, 463.0, 725.0, 465.0, 466.0, 467.0, 468.0, 771.0, 470.0, 945.0, 551.0, 804.0, 522.0, 475.0, 476.0, 477.0, 565.0, 856.0, 480.0, 481.0, 980.0, 965.0, 484.0, 485.0, 534.0, 487.0, 668.0, 489.0, 603.0, 553.0, 492.0, 918.0, 655.0, 696.0, 496.0, 875.0, 899.0, 734.0, 659.0, 799.0, 502.0, 503.0, 504.0, 606.0, 676.0, 643.0, 508.0, 509.0, 706.0, 556.0, 848.0]
PASS
----------------------------------------------------
----------------------------------------------------
test_num.py/test_num
51.0 31.007751937984494
PASS
----------------------------------------------------
----------------------------------------------------
test_sym.py/test
{:div 1.379 :mid a}
PASS
----------------------------------------------------
----------------------------------------------------
test_the.py/test
{:dump False :eg nothing :filename ./data/auto93.csv :help False :nums 512 :seed 10019 :seperator ,}
PASS
----------------------------------------------------
----------------------------------------------------
test_stats.py/test
{'Clndrs': 4.0, 'Volume': 151.0, 'Model': 76.0, 'origin': '1'}
xmid None
{'Clndrs': 1.55, 'Volume': 100.775, 'Model': 3.876, 'origin': 1.327}
xdiv None
{'Lbs-': 2807.0, 'Acc+': 15.5, 'Mpg+': 20.0}
ymid None
{'Lbs-': 886.822, 'Acc+': 2.713, 'Mpg+': 7.752}
ydiv None
PASS
----------------------------------------------------
----------------------------------------------------
test_data.py/test
{:at 4 :hi 5140.0 :isSorted False :lo 1613.0 :n 398 :name Lbs- :w -1}
{:at 5 :hi 24.8 :isSorted False :lo 8.0 :n 398 :name Acc+ :w 1}
{:at 8 :hi 50.0 :isSorted False :lo 10.0 :n 398 :name Mpg+ :w 1}
PASS
----------------------------------------------------
----------------------------------------------------
test_csv.py/test
{Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
{8 304.0 193 4732 18.5 70 1 10}
{8 360 215 4615 14 70 1 10}
{8 307 200 4376 15 70 1 10}
{8 318 210 4382 13.5 70 1 10}
{8 429 208 4633 11 72 1 10}
{8 400 150 4997 14 73 1 10}
{8 350 180 3664 11 73 1 10}
{8 383 180 4955 11.5 71 1 10}
{8 350 160 4456 13.5 72 1 10}
PASS
----------------------------------------------------
----------------------------------------------------
PASSED: 7
FAILED: 0
----------------------------------------------------
```

--- 
