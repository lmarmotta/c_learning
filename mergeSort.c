#include<stdio.h>
#include<stdlib.h>
#include<time.h>

/* Cormens implementation of the merge sort algorithm.
 * I hate recursion with all my heart.
 * Best case scenario: O(n log n)
 * Worst case scenario: O(n log n)
 * Stable: Yes. */

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

void merge(double *series, int p, int q, int r){

    /* series: Unsorted array.
     * p     : A[p...q]
     * q     : A[p...q] 
     * r     : Last element to be sorted */

    int n1 = q - p + 1;
    int n2 = r - q;

    double L[n1];
    double R[n2];

    int i; 

    for (i=0; i<n1; ++i){
        L[i] = series[p+i];
    }

    int j;

    for (j=0; j<n2; ++j){
        R[j] = series[q+1+j];
    }

    /* Cormen recomendation to clean the implementation */
    L[n1] = 100.0;
    R[n2] = 100.0;

    int k = 0;

    i = 0; j = 0;

    for (k=p; k<=r; ++k){
        if (L[i]<=R[j]){
            series[k] = L[i];
            ++i;
        } else if (L[i] > R[j]){
            series[k] = R[j];
            ++j;
        }
    }
}

void mergeSort(double *series, int p, int r){

    int q;

    if (p<r) {
        q = (p + r) / 2;
        mergeSort(series,p,q);
        mergeSort(series,q+1,r);
        merge(series,p,q,r);
    }

}

int main(void){

    int i;
    int size = 10;
    double max = 30.0E+0;
    double *series = NULL;

    series = rnd(size, max);

    for (i=0; i<size; i++) printf(" - Vector[%d] = %lf\n",i,series[i]);

    mergeSort(series,0,size-1);

    printf("\n");

    for (i=0; i<size; i++) printf(" - Vector[%d] = %lf\n",i,series[i]);

    free(series);

    return 0;
}
