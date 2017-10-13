#include<stdio.h>
#include<stdlib.h>
#include<time.h>

double *rnd(int size, double max){

    int i;
    double *ptr = NULL;

    ptr = (double*)malloc(size*sizeof(double));

    if (ptr == NULL){
        printf("Allocation failed\n"); exit(1);
    }

    for (i=0; i<size; i++){
        ptr[i] = (double)rand()/(double)(RAND_MAX/max);
    }

    return ptr;
}
