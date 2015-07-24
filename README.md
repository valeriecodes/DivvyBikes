# DivvyBikes Data Analysis

This code was written as an assignment for the Foundations of Computational Data Analysis class in the University of Chicago Master's Program in Computer Science. It was, in turn, based on this challenge: https://www.divvybikes.com/datachallenge-2014 to present data on Divvy bike usage in the city in an informative and interesting way.

The script I used to generate the plots can be found at ```DivvyBikesDataVisualization.ipynb```, and the plots can also be found in this repo as images.

I wanted to look at the patterns of travel of the bikes, including what stations got the most use, what station-to-station trips were most popular, and whether there were any interesting patterns with regard to bike checkouts (i.e. stations that had large inbalances of returns vs. checkouts).

I first decided to plot each station with two partially transparent dots, a blue one with its radius proportional to the number of check ins at that station, and a red one with it radius proportional to the number of check outs. This resulted in ```mostused.png```. 

This was helpful in determining which stations got the most use, but I was hoping it would give a better picture of what stations saw a large differential of check outs and check ins, which it didn't really. All the points were basically purple. It is clear that stations in the downtown area got the most use, and that stations near the lakefront got more use than inland stations.

But since I still wanted to look at the differentials, I created another, similar plot, looking at the difference between the number of trips to a station and the number of trips from a station. Stations with more check outs than check ins were marked with a red dot corresponding to the size of the difference, and those with more check ins than check outs were marked with a green dot. This visualization is shown in ```diffs.png```. It was useful illustrating that stations around Millennium Park saw many more check ins than check outs, perhaps due to many trips from elsewhere in downtown terminating there.

Another area I wanted to explore was what the most common trips were, since both the previous plots had looked at each station individually, so I plotted the top 100, with line thicknesses determined by the number of trips. This is shown in ```trips.png```. I chose to limit myself to the top 100 so that the resulting map would still be readable.

Finally, I wanted to look at the length of the trips and the time saved over taking public transit, both in theory and in terms of actual average trip time. I used the Google Maps Directions API to look up the estimated biking and public transit times for the top 100 trips (since the number of API queries was capped, I chose to run on the top 100, as running it on all the trips would not have been possible). I looked at the estimated biking time compared to the estimated public transit time (```bike_vs_transit.png```), the actual average trip time compared to the the estimated biking time (``bike_vs_actual.png```), and the actual average trip time compared to the estimated public transit time (```transit_vs_actual.png```).

In the first plot, I noticed, unsurprisingly, that biking tended to be faster than public transit, but also that all of the estimated times for the most common trips were below Divvy's 30-minute free period for rentals.

In the next two plots, it became clear that many of the most popular trips are in fact round trips to the same or adjacent stations, so there actually turned out to be almost no correlation between the estimated transit times and the actual average trip times, perhaps also muddied by a mix of commuter and leisurely sightseeing traffic. We can see that many of the popular trips had an average length of less than the 30-minute cut-off (the red line on the plots).
