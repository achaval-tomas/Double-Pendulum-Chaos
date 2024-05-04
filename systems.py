from physics import System
from math import pi

# first system with default values
# (g)ravity=1
# first ball mass (m1)=50
# second ball mass (m2)=75 
# first rod length (r1)=100
# second rod length (r2)=250 
# first rod angle (a1)=3*pi/4
# second rod angle (a2)=3*pi/4
# system's (color)="goldenrod1"
system1 = System()

# default values except for minimal difference in angle1
system2 = System(a1=3*pi/4.0001, color="mediumpurple3")

# default values except for minimal difference in angle2
system3 = System(a2=3*pi/3.9999, color="indianred2")

## you can add more systems here (and then add them to systems[] below)

systems = [system1, system2, system3]