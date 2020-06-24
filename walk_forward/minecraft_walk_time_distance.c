#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "calculate_time.h"


int main(int argc, char **argv)
{
    double dist = (double) atof(argv[1]);
    printf("%lf", distance(dist));    
}
