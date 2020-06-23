#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double distance(double distance) {
   double distance_result;
   return distance*(distance*(distance*(4.5364011804949552e-6 - 2.5689607228491486e-8*distance) - 0.0002051901833335847) + 0.1805750734251993) - 0.046861895459978369;
}

int main(int argc, char **argv)
{
    double dist = (double) atof(argv[1]);
    printf("%lf",distance(dist));
}
