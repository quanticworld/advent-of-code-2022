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
|   day1_1   |      71023 |              1.53635 |
|   day1_2   |     206289 |             1.478438 |
|   day2_1   |      12855 |             0.315115 |
|   day2_2   |      13726 |             0.412357 |
|   day3_1   |       7597 |             2.605565 |
|   day3_2   |       2607 |             0.313905 |
|   day4_1   |        584 |             4.272664 |
|   day4_2   |        933 |             4.535324 |
|   day5_1   |  JDTMRWCQJ |             0.873501 |
|   day5_2   |  VHJDDCWRD |              0.58585 |
|   day6_1   |       1542 |             1.051908 |
|   day6_2   |       3153 |             2.205417 |
|   day7_1   |    1141028 |             5.441306 |
|   day7_2   |    8278005 |             5.617703 |