#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>

#include<omp.h>

# define SIZE 100000

void check_answer(double * vec);

int main(){

    int i;

    /* Allocating the vectors */ 
    double * vec_1 = (double*)malloc(SIZE*sizeof(double));
    double * vec_2 = (double*)malloc(SIZE*sizeof(double));
    double * vec_3 = (double*)malloc(SIZE*sizeof(double));

    printf(" \n- Done with vector allocation\n");

    /* Fill the vectors with dummy values */ 
    for (i=0; i<SIZE; i++){
        vec_1[i] = 1.0;
        vec_2[i] = 2.0;
    }

    printf(" \n- Done with vector fill-up\n");

    /* Running vector summation in a dummy way */

    clock_t begin = clock();

    for (i=0; i<SIZE; i++) vec_3[i] = vec_1[i] * vec_2[i];

    clock_t end = clock();

    double t_time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf(" \n- Time elapsed in serial case: %lf\n", t_time);

    check_answer(vec_3);

    /* Running vector summation with openmp */

    begin = clock();

    #pragma omp parallel shared(vec_3) private(i)
    {
    #pragma omp for schedule(static)
    for (i=0; i<SIZE; i++) vec_3[i] = vec_1[i] * vec_2[i];
    }

    end = clock();

    t_time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf(" \n- Time elapsed in parallel case: %lf\n", t_time);

    check_answer(vec_3);

    free(vec_1);
    free(vec_2);
    free(vec_3);

    return 0;
}

void check_answer(double * vec){

    if (vec[1] == vec[SIZE]) 
        printf(" \n++ CORRECT ANSWER ++\n");
    else
        printf(" \n++ WRONG ANSWER ++\n");

}
