
#include<stdio.h>
#include<stdlib.h>
#include<time.h>


#define MAX_POLY_TERMS 20
#define TRUE 1
#define FALSE 0

double coefficients[MAX_POLY_TERMS];  // coefficients of a polynomial
int numberOfTerms;
double Xmin = -270.0;   // default value
double Xmax = 0.0;  // default value

// 
static double compute(double x) {
    int index;
    double y = 0.0;

    // Do sum in reverse order
    for (index=numberOfTerms-1; index>=0; index--) {
        y = coefficients[index] + y * x;
    }
    return y;
}


void init(double min, double max) {
    coefficients[0] = 0.000000000000E+00;
    coefficients[1] = 0.586655087080E-01;
    coefficients[2] = 0.454109771240E-04;
    coefficients[3] = -0.779980486860E-06;
    coefficients[4] = -0.258001608430E-07;
    coefficients[5] = -0.594525830570E-09;
    coefficients[6] = -0.932140586670E-11;
    coefficients[7] = -0.102876055340E-12;
    coefficients[8] = -0.803701236210E-15;
    coefficients[9] = -0.439794973910E-17;
    coefficients[10] = -0.164147763550E-19;
    coefficients[11] = -0.396736195160E-22;
    coefficients[12] = -0.558273287210E-25;
    coefficients[13] = -0.346578420130E-28;
    numberOfTerms = 14;
  
    if (min<max) {
        Xmin = min;
        Xmax = max;
    }
}


int checkTime(int samplePoints, char* logFilename) {
    int saveLog;
    FILE* fLog;

    init(-270.0, 0.0);  // same as default value

    if (logFilename!=0) saveLog = TRUE;
    else saveLog = FALSE;

    printf("Time test of pure computation in C %s\n", (saveLog ? " with log" : " without log"));

    clock_t startTime = clock();

    if (saveLog) {
        fLog = fopen(logFilename, "w");
    }

    double delta = (Xmax-Xmin) / (samplePoints-1);
    for (int point=0; point<samplePoints; point++) {
        double X = Xmin + point*delta;
        double Y = compute(X);

        if (saveLog) { 
            fprintf(fLog, "%f %f\n", X, Y);
        }
    }

    if (saveLog) fclose(fLog);

    clock_t endTime = clock();
    float timeUse = ((float)endTime - (float)startTime) / CLOCKS_PER_SEC  * 1000;
    printf("time for %i computations is %f msec\n", samplePoints, timeUse);

    return TRUE;
}

int main(int argc, char** argv) {

    checkTime(1000, 0);
    checkTime(100000, 0);
    checkTime(10000000, 0);
    
    checkTime(1000, "clog-1000.txt");
    checkTime(100000, "clog-100000.txt");
    checkTime(10000000, "clog-10000000.txt");
    
    return 0;
}

