
CC = g++
PY = python3

all: gen.cpp
		$(CC) gen.cpp -o gen.out
		./gen.out | $(PY) plot.py

clean:
		rm gen.out