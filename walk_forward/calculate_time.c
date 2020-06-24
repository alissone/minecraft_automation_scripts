#include "calculate_time.h"
#include <math.h>
double distance(double distance) {
   double distance_result;
   distance_result = distance*(distance*(distance*(2.1259662352625052e-8 - 1.5674534848452648e-10*distance) + 8.8378740654481346e-6) + 0.17705100419700931) - 0.039715926468885276;
   return distance_result;
}
