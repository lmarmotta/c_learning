/* Ways to measure time in C */
/* Just for linux */
/* gcc [this code] -o time */
/* source: https://users.pja.edu.pl/~jms/qnx/help/watcom/clibref/qnx/clock_gettime.html */

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>

double w_time(struct timespec start, struct timespec stop){
    return (stop.tv_sec - start.tv_sec) + (stop.tv_nsec - start.tv_nsec) / 1.0e9;
}

int main(int *argc, char **argv){

    int variable = 0;
    double result;
    struct timespec start, stop;

    clock_gettime(CLOCK_REALTIME, &start);

    int i;
    for (i = 0; i<1000000; i++){
        variable = variable + i;
    }

    clock_gettime(CLOCK_REALTIME, &stop);

    result = w_time(start, stop);

    printf("\nTime elapsed: %lf [s]\n", result);

    return 0;
}


    

    

