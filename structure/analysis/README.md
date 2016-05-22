
#Analysis Overview
Analysis done with Frame3DD
[Frame3DD](http://frame3dd.sourceforge.net/).

##Linux Install (Ubuntu 14.04)
1. Download Frame3DD source
2. Go to Frame3DD/src and run make
3. mv frame3dd ../
4. ensure gnuplot is installed
5. run

##Run Analysis Case
frame3dd frame.3dd frame.out

##Post-Processing
After the analysis is complete, and the frame design is satisfactory, the results are post-processed. This is done to obtain the total lengths of the tubing required and to get the frame nodes coordinates to build a CAD object.

./framepost.py
