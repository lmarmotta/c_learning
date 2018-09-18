#include<stdio.h>
#include<stdlib.h>

void mod_m(double ** C){

    int size = 3;

    for (int i = 0; i<size; i++)
        for (int j = 0; j<size; j++)
            C[i][j] = 32.0;

}

int main(){

    int size = 3;

    double ** C = (double**)calloc(size,sizeof(double*));
    for (int i = 0; i<size; i++) C[i] = (double*)calloc(size,sizeof(double));

    for (int i = 0; i<size; i++)
        for (int j = 0; j<size; j++)
            C[i][j] = 0.0;

    mod_m(C);

    for (int i = 0; i<size; i++)
        for (int j = 0; j<size; j++)
            printf("C[%d][%d] = %lf\n",i,j,C[i][j]);

    return 0;
}
