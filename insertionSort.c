/* 
 * INSERTION-SORT ALGORITHM IMPLEMENTATION
 * This program implements the Cormen's insertion sort algorihm. Note that
 * although the book is pretty clear about the while controling statment being
 * set to i>0, in C, due to 0 counting convention, this is not coorect. You
 * need to include the '=' in order to sort the first element of the vector. 
 *
 * Complexity: - Worst case: O(n^2)
 *             - Best  case: O(n)
 */

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

void int_sort(double *series, int s_size){

    int j;

    for (j=1; j<s_size; j++){

        int i;
        double key;

        key = series[j];
        i = j-1;

        while (i>=0 && series[i]>key){
            series[i+1] = series[i];
            i = i-1;
        }
        series[i+1] = key;
    }
}

int main(void){

    int i;
    int size = 10;
    double *my_data  = NULL;
    double *old_data = NULL;

    my_data = rnd(size,30.0E+0);

    old_data = (double*)malloc(size*sizeof(double));

    /* Copy vector for comparasion. */
    for (i=0; i<size; i++){
        old_data[i] = my_data[i];
    }

    /* sort data */
    int_sort(my_data, size);

    for (i=0; i<size; i++){
        printf(" - Old Position[%d]: %10.4lf | New position[%d]: %10.4lf\n",
                i,old_data[i],i,my_data[i]);
    }

    free(my_data);

    return 0;
}
