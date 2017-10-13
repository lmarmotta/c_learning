CC=gcc
FLAGS=-std=c99 -O0 -g -Wall -Werror -Wextra
LIBS=-fopenmp

all: insertionSort mergeSort heapSort bit_hacks v_mult neat
#
# Random C stuff.
#
bit_hacks:
	$(CC) $(FLAGS) -o bit_hacks bit_hacks.c

v_mult:
	$(CC) $(FLAGS) -o v_mult v_mult.c $(LIBS)

neat:
	$(CC) $(FLAGS) -o neat neat.c
#
# Algorithm and data-structures lessons.
#
insertionSort:
	$(CC) $(FLAGS) -o insertionSort insertionSort.c

mergeSort:
	$(CC) $(FLAGS) -o mergeSort mergeSort.c

heapSort:
	$(CC) $(FLAGS) -o heapSort heapSort.c
#
# Clean command.
#
clean:
	rm -r insertionSort mergeSort heapSort bit_hacks v_mult neat 
