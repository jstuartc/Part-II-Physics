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
- A plot showing the variation across this region was produced