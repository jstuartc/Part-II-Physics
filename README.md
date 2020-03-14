#Part II Physics Computing

This repo contains the work done for my Part II Physics Computing work, done in python.

The work is from two stages
  Physics Exercises
  Physics Computing Project (not yet done)
  
##Physics Exercises

In the Physics Exercises folder there are 3 Exercise.

**Exercise 1**  
Investigates Monte Carlo Integration to evaluate an integral and works out the associated error in this method.Also utilises Numerical integration to create the Cornu Spiral and calculating the intensity-phase relation for Fresnel Scattering

![Cornu Spiral](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise1/Cornu-Spiral.png)

![Graph of Errors](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise1/Error-Nloglog.png)


**Exercise 2** 
For this project the behaviour of a swinging pendulum was investigated using the Runge-Kutta Method and making use of the '''integrate.solve_ivp()''' function in scipy. The method was tested against the theoretical predictions of the equation utilising the small angle approximation. And by determining how well the program conserved energy in an non-damped system.

Then various starting conditions were imposed which included damping coefficient *q*, Driving force *F* and staring angle and angular velocity *θ* and *ω*. The results can be seen below

![Plot of Angle vs Time for various F](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise2/Angle-time-Forced.png)

![Plots of various starting conditions](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise2/Velocity-Angle%20Graph%20for%20different%20starting%20Conditions.png)


**Exercise 3A**
This exercise consisted of modelling the the Magnetic field caused from a coil. 
Method for doing this was modelling each coil as a finite number of line elements. Then to find *B* for a position *r* the program would calculate the **dB** for each of the line elements before summing up to find **B**.

The computational result for B was tested against the theoretical value along the the x axis and is shown here.

![Theoretical vs Computational along x axis](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise3A/B%20field%20against%20x%20for%20Theory%20and%20Model.png)

With this confirmed, the project was expanded to investigate B in an 2D plane (z=0). It was shown that the within 2 coils centred at +/- p0.5m the Field is uniform near the origin.

![Uniform Field](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise3A/Fractional%20change%20in%20ModB%20field%20across%20an%20area%20of%20Y%20and%20X%20in%20the%20z%20=%200%20plane.png)

The project then looked at different arrangement of coils and how it was affected with the program able to produce contour plots which depended on the input parameters. With an example below.

![modB detail](file:///Users/James/git/Part-II-Physics/Physics-Part-II-Exercises/src/Exercise3A/modB%20-%20detail%20radius%201,%20N%20=%2010.png)


