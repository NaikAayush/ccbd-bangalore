cat main.csv | ./mapper.py | sort -k1,1 | ./reducer.py
