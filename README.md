# Payload-2020-Analysis

This script in its current state takes in inputs in csv format from text files in the "test_data" directory and generates a graph in the "graph" directory.

Enter/Replace the input file name as the "filename" variable on line 7

Input file should have format of:

testStarted
time (in microseconds?) : voltage
time : voltage
...


Due to large file sizes, the program takes a considerable amount of time to run. 
It is not recommended to use "fig.show()" as that often creates an extremely laggy figure. 