# conserv_optimization

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
