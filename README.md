# Advent of code

## Approach

* Learn python, that I don't know much about
* Have a quite reduced code
* Don't care about cognitive complexity
* Make formal syntax my first choice, instead of verbose code

:bulb: set manipulation seems to often be the key to ease second part resolution.
The drawback being performance, but we don't care about it, as the data sets are quite small.

## Performance bench

/usr/bin/python3.10 /home/quantic/github/advent-of-code-2022/execute_all.py 

|    part    |     result |  avg (ms) / 100 iter |
| ---------- | ---------- | -------------------- |
|   day1_1   |      71023 |             2.943223 |
|   day1_2   |     206289 |             1.388149 |
|   day2_1   |      12855 |               0.3121 |
|   day2_2   |      13726 |             0.402381 |
|   day3_1   |       7597 |             2.468305 |
|   day3_2   |       2607 |             0.298106 |
|   day4_1   |        584 |             4.354257 |
|   day4_2   |        933 |             4.613293 |