#include<stdio.h>
#include<stdlib.h>

typedef struct p_data{
    double rho;
    double jac[3][3];
    double *q_con;
    double *q_pri;
} p_data;

void rhoOverField(p_data *da, int s_domain){
    int i;
    for(i=0;i< s_domain;i++) da[i].rho = 1.225;
}

void fillJacobian(p_data *da, int s_domain){

    int i;
    for(i=0;i<s_domain;i++){
        da[i].jac[0][0] = 0.0E+0;
        da[i].jac[1][0] = 1.0E+0;
        da[i].jac[2][0] = 2.0E+0;

        da[i].jac[0][1] = 0.1E+0;
        da[i].jac[1][1] = 1.1E+0;
        da[i].jac[2][1] = 2.1E+0;

        da[i].jac[0][2] = 0.2E+0;
        da[i].jac[1][2] = 1.2E+0;
        da[i].jac[2][2] = 2.2E+0;
    }
}

void fillPrimitives(p_data *da, int s_domain){

    int i;
    for(i=0;i<s_domain;i++){
        da[i].q_con[0] = 0.0;
        da[i].q_con[1] = 1.0;
        da[i].q_con[2] = 2.0;
        da[i].q_con[3] = 3.0;
        da[i].q_con[4] = 4.0;
        da[i].q_con[5] = 5.0;
    }

    for(i=0;i<s_domain;i++){
        da[i].q_pri[0] = 0.0;
        da[i].q_pri[1] = 1.0;
        da[i].q_pri[2] = 2.0;
        da[i].q_pri[3] = 3.0;
        da[i].q_pri[4] = 4.0;
        da[i].q_pri[5] = 5.0;
    }
}

p_data *allocateDomain(int n_eq, int s_domain){

    int i;

    /* First, allocate the array of structs */
    p_data * da = (p_data*)malloc(s_domain*sizeof(p_data));

    /* Now, allocate the necessary number of prim and con vars. */
    for(i=0;i<s_domain;i++) da[i].q_con = (double*)malloc(n_eq*sizeof(double));
    for(i=0;i<s_domain;i++) da[i].q_pri = (double*)malloc(n_eq*sizeof(double));
    
    return da;

}

void freeDomain(p_data *da, int s_domain){

    int i;

    for (i=0;i<s_domain;i++) free(da[i].q_con);
    free(da);
}

void dumpDomain(p_data *da){

    printf("da[3].rho = %lf\n",da[3].rho);
    printf("da[3].jac[1][1] = %lf\n",da[3].jac[1][1]);
    printf("da[3].q_con[2] = %lf\n",da[3].q_con[2]);
    printf("da[3].q_pri[2] = %lf\n",da[3].q_pri[2]);
}

int main(){

    int s_domain = 100;

    p_data * pd = allocateDomain(6,s_domain);

    /* If I stop here, I'll have the correct field of rho. */
    rhoOverField(pd,s_domain);

    /* Now, rho is does not have the correct value. */
    fillJacobian(pd,s_domain);

    /* Now, initialize the primitives. */
    fillPrimitives(pd,s_domain);

    /* Print out baby */
    dumpDomain(pd);

    /* Free the domain */
    freeDomain(pd,s_domain);

    return 0;
}
