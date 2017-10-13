CC=gcc
FLAGS=-std=c99 -O0 -g -Wall -Werror -Wextra

all: insertionSort mergeSort heapSort

insertionSort:
	$(CC) $(FLAGS) -o insertionSort insertionSort.c

mergeSort:
	$(CC) $(FLAGS) -o mergeSort mergeSort.c

heapSort:
	$(CC) $(FLAGS) -o heapSort heapSort.c

clean:
	rm -r insertionSort mergeSort heapSort
