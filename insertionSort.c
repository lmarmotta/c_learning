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
#include"comm.h"

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
    double *series = NULL;

    series = rnd(size,30.0E+0);

    for (i=0; i<size; i++) printf(" - Vector[%d] = %10.4f\n",i,series[i]);

    /* sort data */
    int_sort(series, size);

    printf("\n");

    for (i=0; i<size; i++) printf(" - Vector[%d] = %10.4f\n",i,series[i]);

    free(series);

    return 0;
}
