/* This program compares some basic operations with bit hacks 
 * The goal here is to better understand how the compiler opt
 * timization deals with these hacks */

/* Based on MIT's OCW */


#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>

void dummy_swap(int * val_1, int * val_2);
void bit_swap(int * val_1, int * val_2);
int dummy_min(int val_1, int val_2);
int bit_min(int val_1, int val_2);

int main(void){

    int i;
    int x = 1;
    int y = 2;

   /* SWAP TWO INTEGERS */

   /*
    * Testing the dummy swap speed 
    */ 

    printf("\nINTEGER SWAP TEST\n");
    printf("\nValue of x: %d | Value of y: %d\n",x,y);

    clock_t begin = clock();

    for (i = 1; i < 100000000; i++) dummy_swap(&x,&y);

    clock_t end = clock();

    double time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf("\nValue of x: %d | Value of y: %d --> Elapsed dummy time: %f\n",x,y,time);

    /* 
     * Testing the smarter bit hack swap technic
     */

    x = 1;
    y = 2;

    printf("\nValue of x: %d | Value of y: %d\n",x,y);

    begin = clock();

    for (i = 1; i < 100000000; i++) bit_swap(&x,&y);

    end = clock();

    time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf("\nValue of x: %d | Value of y: %d --> Elapsed bit time: %f\n",x,y,time);

   /* FIND THE MINIMUM OF TWO NUMBERS */

    printf("\nINTEGER FIND MIN TEST\n");

    /* dummy min */ 
    x = 1;
    y = 2;

    printf("\nValue of x: %d | Value of y: %d\n",x,y);

    begin = clock();

    for (i = 1; i < 100000000; i++) dummy_min(x,y);

    end = clock();

    time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf("\nMin value: %d --> Elapsed dummy time: %f\n",dummy_min(x,y),time);

    /* bit min */
    x = 1;
    y = 2;

    printf("\nValue of x: %d | Value of y: %d\n",x,y);

    begin = clock();

    for (i = 1; i < 100000000; i++) bit_min(x,y);

    end = clock();

    time = (double)(end-begin)/CLOCKS_PER_SEC;

    printf("\nMin value: %d --> Elapsed bit time: %f\n",bit_min(x,y),time);

    return 0;
}

void dummy_swap(int * val_1, int * val_2){

    int t;

    t = *val_1;
    *val_1 = *val_2;
    *val_2 = t;
}

void bit_swap(int * val_1, int * val_2){
    *val_1 = *val_1 ^ *val_2;
    *val_2 = *val_1 ^ *val_2;
    *val_1 = *val_1 ^ *val_2;
}

int dummy_min(int val_1, int val_2){

    int min;

    if (val_1 < val_2)
        min = val_1;
    else
        min = val_2;

    return min;
}

int bit_min(int val_1, int val_2){

    int min;

    min = val_2 ^ ((val_1 ^ val_2) & -(val_1 < val_2));

    return min;
}
