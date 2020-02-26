Core1

Method
-Created a vector of 25xN which in each element contained the sum of 8 uniformly random values between 0 and pi/8.
-Passed this vector through a sin function for each element, then collapsed the the vector into a vector of width 25 and multiplied by the total volume and 10**6.
-With this vector the mean and sdv was found

- This was done for a range of N (in powers of 2) and the mean vs N and error vs N were plotted which can be seen

Integrating over a value of N = 2**23 averaging of 25 things gives a value of 537.1841246485706 +/- 0.01905842576508154
Time taken was less than half a minute