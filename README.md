# conserv_optimization
Todo:
- associate selected cells with data frame, save as solution csv

- test small cases and confirm results

- test for complete data set

- improve interface, add ability to plot map coordinates

- create virtualenv and requirements.txt to automate and pin package deps 

- add ability to maximize for other params, not just area, difficult as 
  knapsack only works with integer, some for of normalization scheme will 
  have to preprocess data, or maybe knapsack alg can run with index'd lists 
  ..notsure

- add ability to set MAX_CELLS from the make file in 'scripts/analyze.py
  for any given budget, so the default will be to analyze all the cells

Requirements:
	python3.5
	pip3 install numpy
	pip3 install pandas
	pip3 install progress

To Run:
The defaults of number of cells
to analyze and total budget are set to minimize
computation time by default, before the code is 
fully tested. These may be overridden at run time
from the shell as such:

$ make all NUM_CELLS=20 BUDGET=100000   

$ make knapsack NUM_CELLS=400 BUDGET=1000000

To run with the defaults
$ make all


To clean:
$ make clean
