Core 1
- Used integrate.solve_ivp with RK method to solve the differential equations
- Plotted a graph showing the displacement over time for θ= 0.01 for both the RK method and the theoretical predictions from small angle approximations, which show they are in perfect harmony
-Plotted how the Energy of the system changed with the RK method over 10000 oscillations. This was found to be about a 1% change
- Plotted Period against starting angle. To find the period, a method was created which found the 1st maximum of the cosine wave (ie Period of one oscillation) then found the 2nd then 4th, 8th terminating with the maximum of highest order 2 (Speed of O(logn), to produce an accurate value of T

The period for a starting angle of π/2 is 3.7078978857828337


Core 2

- Added in a function which when you put in q and F returned an updated differential equation.
- Plotted a graph showing amplitude change for a range of values of q, utilising the added method as described above.
- Velocity-time and amplitude-time graphs were plotted for various values of F and q = 0.5
-For the angle graph, for displacements outside of -π to π, the displacement was mapped back onto the required region


Supplementary 1

- Plots were created showing how slightly different starting conditions resulted in the change being propagated through over 100 oscillations in this case.
- What you see that within 20 oscillations that an original Δθ = 0.001 results in a large difference. Small uncertain sharp peak around 40s which is probably due to a rounding error.
- Solutions Diverge

Supplementary 2
- Plotted 9 plots of velocity-angle showing different starting conditions
- Top row had F=q=0 and varied ω and θ outside of small angle approximation. Saw ellipses like shapes for θ = 2 and ω = 2, and for when θ = ω = 2 we had a Gaussian shape graph which indicated that the pendulum rotated round varying speed
- Second row had θ = 2, F = ω = 0 and varied q. The spiral seen for small q light damping is eliminated for q = 2 heavy damping
- Bottom row set F = θ = 0 and q = 1 and let ω = 1,10,100. Really fascinating as for larger ω the simulation breaks down a bit but the line which is curved in low ω is straight and moves in and out of edge of plot (ie rotates from -π to π). So there are discontinuities which are not seen but instead a arbitrary line across the graphs which connect -π to π.
