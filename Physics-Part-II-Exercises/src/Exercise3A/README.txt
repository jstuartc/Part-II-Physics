Core 1
- Created a method which produces a ring (Coil) of straight lines at the desired point
- To find B field at a point a method was created which took a 3d position and a list of line elements (Coil in this case but could be anything), then the method calculated dB for each dl and summed dB to find the B vector at that point
- Plotted Bx against x along the x axis with the simulation and theory and found there was no difference.
-For this task since I plotted Bx it was independent of the number of elements I split the ring into
-Though if I plotted mod B it shouldn't matter since all the other bits would cancel out leaving only Bx. This I could see by looking at my values of By and Bz at points along the line.
- For the later parts of the code the amount of points drastically changed my results and I found the best results came with and odd number of elements and adjusting to avoid zero errors

Core 2
- For this code mod B was calculated over an area of of rectangle in z plane (or volume of cylinder) with dimensions of diameter 0.1 and length 0.1 centred at the origin.
- In the vicinity there are two coils facing the same x direction of same radius at x = +/- 0.5m is the centre of the coils.
- The difference with this was just adding together the B fields of 2 coils.
- The number of line elements made a difference here with larger the number produced clearer images but computational time is O(logN)
The maximum percentage difference in the area was 0.0099% showing the uniformity of B across this region
- A plot showing the B field across this region was produced

Supplementary
- To make a system with N coils, a method was created which returned a list of Coils.
- A class was implemented in order to contain the information of the coils so that the system was a list of length N individual coils instead of an array of 3 dimensions with one dimension being N. Did this in order to keep the code vectorised instead of bringing in for loops
- In all systems the diameter = 10* Radius
- Plotted a graph showing what happens when your sweep area is larger than the coil. All the B field contours are at the edge of the wires itself. Some of them don't appear since the sweeping of the points don't get close enough
-Plotted a graph showing what happens to the B field at the open ends of the coil. It shows the uniformity within compared to a metre outside
-Plotted the same setup but within the coil completely. The graph is not symmetrical and this is due to the coils being comprised of a limited number of elements 30 in this case.
-Plotted the same conditions as above except with N= 10. From the plot you can clearly see that the field within the coil is not as uniform compared to N = 20. The graph is also not symmetric
- Repeated but with 100 line elements in the coil. Much longer computation. The graph is pretty much symmetric along x and y axis. This indicates that better modelling of the coils produces better results
