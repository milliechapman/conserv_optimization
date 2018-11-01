PRJ_DIR = $(shell pwd)

BUDGET=5000000


all: knapsack data/data.csv

knapsack: data/data.csv 
	$(PRJ_DIR)/scripts/analysis.py $(BUDGET) $(PRJ_DIR)/data/data.csv

data/data.csv: $(PRJ_DIR)/data/conserv.csv
	$(PRJ_DIR)/scripts/parse_data.py $< $(PRJ_DIR)/data/data.csv

clean:
	rm $(PRJ_DIR)/data/data.csv
	rm $(PRJ_DIR)/decision.csv
