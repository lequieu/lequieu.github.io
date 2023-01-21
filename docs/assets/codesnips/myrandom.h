#include "math.h"

void myrandom_set_seed(int seed){
    srand(seed);
}

double myrandom_double(){
    //returns double between 0-1
    return (double) rand() / RAND_MAX;
}

double myrandom_gauss(double sigma)
  {
      //Method to get gaussian random numbers with mean 0, stdev of sigma
      double ran1,ran2,ransq,v;
      do  
      {   
        ran1=2.0*myrandom_double()-1.0;  //rand# in range [-1 1]
        ran2=2.0*myrandom_double()-1.0;
        ransq=ran1*ran1+ran2*ran2;
      }   
      while(ransq >= 1.0);
  
      v=sqrt(sigma)*ran1*sqrt(-2.0*log(ransq)/ransq);
      return v;
  }



