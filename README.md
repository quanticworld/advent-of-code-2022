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
|   day1_1   |      71023 |             1.373653 |
|   day1_2   |     206289 |             1.397658 |
|   day2_1   |      12855 |             0.333448 |
|   day2_2   |      13726 |             0.460944 |
|   day3_1   |       7597 |             2.577892 |
|   day3_2   |       2607 |             0.285006 |
|   day4_1   |        584 |             4.151172 |
|   day4_2   |        933 |             4.359657 |
|   day5_1   |  JDTMRWCQJ |             0.818297 |
|   day5_2   |  VHJDDCWRD |              0.56163 |