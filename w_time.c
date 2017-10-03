/* Benchmark of time measurement techinics in C. The goal here is to find 
 * an idependent of system condition time measurement technic */

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>

double w_time(struct timespec start, struct timespec stop){
    return (stop.tv_sec - start.tv_sec) + (stop.tv_nsec - start.tv_nsec) / 1.0e9;
}

int main(int *argc, char **argv){

    int variable = 0;
    double result_1,result_2, result_3, result_4;

    struct timespec start_1, stop_1;
    struct timespec start_2, stop_2;
    struct timespec start_3, stop_3;

    clock_gettime(CLOCK_REALTIME, &start_1);
    clock_gettime(CLOCK_MONOTONIC, &start_2);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_3);
    clock_t begin = clock();

    int i;
    for (i = 0; i<100000; i++){
        variable = variable + i;
    }

    clock_gettime(CLOCK_REALTIME , &stop_1);
    clock_gettime(CLOCK_MONOTONIC, &stop_2);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &stop_3);
    clock_t end = clock();

    result_1 = w_time(start_1, stop_1);
    result_2 = (double)(end-begin)/CLOCKS_PER_SEC;
    result_3 = w_time(start_2, stop_2);
    result_4 = w_time(start_3, stop_3);

    /* Gives different results depending on the process being running */
    printf("\nTime elapsed: %lf [s]\n", result_1);

    /* Gives different results depending on the process being running */
    printf("\nTime elapsed: %lf [s]\n", result_2);

    /* Gives different results depending on the process being running */
    printf("\nTime elapsed: %lf [s]\n", result_3);

    /* Gives different results depending on the process being running */
    printf("\nTime elapsed: %lf [s]\n", result_4);

    return 0;
}


    

    

