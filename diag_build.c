#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

/* Allocate a double matrix. */

double ** alloc_dmatrix(int imax, int jmax){

    double ** out = NULL;

    out = (double**)calloc(imax,sizeof(double*));

    if (out == NULL) {printf("ERROR: double matrix allocation.\n"); exit(1);}

    for (int i = 0; i<imax; i++){
        out[i] = (double*)calloc(jmax,sizeof(double));
        if (out[i] == NULL) {printf("ERROR: double matrix allocation.\n"); exit(1);}
    }

    /* Initialize the matrix. */

    for (int i = 0; i<imax; i++)
        for (int j = 0; j<jmax; j++) out[i][j] = 0.0;

    return out;
}

/* Free double matrix. */

void free_dmatrix(double ** matrix, int imax){

    for (int i = 0; i<imax; i++)
        free(matrix[i]);

    free(matrix);
}


/* Build the diagonal matrix. */

void diag(double ** matrix, double * main, double * lower, double * upper, int size){

    for (int i = 0; i<size  ; i++) matrix[i][i]   = main[i];
    for (int i = 1; i<size  ; i++) matrix[i][i-1] = lower[i];
    for (int i = 0; i<size-1; i++) matrix[i][i+1] = upper[i];

}

int main(){

    /* Build a diagonal matrix. */

    double ** matrix = alloc_dmatrix(5,5);

    double * main = (double*)malloc(5*sizeof(double));
    double * lowe = (double*)malloc(5*sizeof(double));
    double * uppe = (double*)malloc(5*sizeof(double));

    main[0] = 1.0; lowe[0] = 2.0; uppe[0] = 3.0;
    main[1] = 1.0; lowe[1] = 2.0; uppe[1] = 3.0;
    main[2] = 1.0; lowe[2] = 2.0; uppe[2] = 3.0;
    main[3] = 1.0; lowe[3] = 2.0; uppe[3] = 3.0;
    main[4] = 1.0; lowe[4] = 2.0; uppe[4] = 3.0;

    diag(matrix, main, lowe, uppe, 5);

    for (int i = 0; i<5 ; i++){
        for (int j = 0; j<5; j++){
            printf("%lf ",matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}

