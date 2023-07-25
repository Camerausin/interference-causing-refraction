# import numpy as np
from mpmath import mp, sin, cos, sqrt, acos, asin, degrees, radians

# import numpy as np

# start with finding the distance of the slits to the incident light
# all is measured in meters

wavelength = mp.mpf(500e-9)
angleToTheSlits = radians(0)
# print("the angle of the incident light to the slits is {}".format(angleToTheSlits))
distanceToMiddleOfSlitsFromSlit = mp.mpf(1e-3)
distanceToMiddleOfSlitsFromLight = 1
distanceBetweenSlits = mp.mpf(2e-3)

adjacentToLight = cos(angleToTheSlits)
print("distance of x for incident light {} m".format(adjacentToLight))
oppositeToLight = sin(angleToTheSlits)
print("distance of y for incident light {} m".format(oppositeToLight))
# find the sides, so we can use the pythagorean theorem to find the length of hypotenuse
heightOfOPPToFirstSlit = mp.mpf(oppositeToLight - distanceToMiddleOfSlitsFromSlit)
heightOfOPPToSecondSlit = mp.mpf(oppositeToLight + distanceToMiddleOfSlitsFromSlit)
# pythagorean theorem
hypotenuseToTheFirstSlit = sqrt((adjacentToLight ** 2) + (heightOfOPPToFirstSlit ** 2))
hypotenuseToTheSecondSlit = sqrt((adjacentToLight ** 2) + (heightOfOPPToSecondSlit ** 2))
print("Length of hypotenuse to the first slit {} m".format(hypotenuseToTheFirstSlit))
print("Length of hypotenuse to the second slit {} m".format(hypotenuseToTheSecondSlit))

# we now have the distance to the slits we need to change that to the phase by taking the modulo
# to get the modulo we are going to take the phase portion of the standard wave equation which is
# sin((2pi/wavelength) * distance)... inside the () is the phase portion of the wave equation.
# we will take the phase portion and divide by the mod number which is 2 so that leaves us with
# distance / wavelength. we then need to get rid of the part before the decimal by % 1 which leaves
# us with just the decimal portion. then we multipy by the mod number which is 2
decimalOfCyclesInHypotenuseToFirstSlit = (hypotenuseToTheFirstSlit / wavelength) % 1
initialPhaseAtFirstSlit = decimalOfCyclesInHypotenuseToFirstSlit * 2
print("phase of light at the first slit is {} pi".format(initialPhaseAtFirstSlit))

# now the second
decimalOfCyclesInHypotenuseToSecondSlit = (hypotenuseToTheSecondSlit / wavelength) % 1
initialPhaseAtSecondSlit = decimalOfCyclesInHypotenuseToSecondSlit * 2
print("phase of light at the second slit is {} pi".format(initialPhaseAtSecondSlit))

# We have the phases at either slit, so now we need to find the distance that the to waves will interact
# To start I need to find the distance that wave would be able to travel while the beam is still in
# transit to slit b
# This means I need to find the difference between distances to the slits and find the time it will take
# to get through that distance. the distance will be the same in air, but I still want to do the time
# because when I do the math for a different medium all I will have to do Is the changed speed of light
# multiplied by the time to give me meters.
speedOfLightBeforeSlits = mp.mpf(299792258)
speedOfLightAfterSlits = mp.mpf(299792258)
distanceBetweenHypotenuse = mp.mpf(hypotenuseToTheSecondSlit - hypotenuseToTheFirstSlit)
print("distance between the hypotenuse {}".format(distanceBetweenHypotenuse))
# find the distances based on the speed of light because when we add a denser medium that will change the distance
timeLightGoHalfDistanceBetween = mp.mpf(distanceBetweenHypotenuse / speedOfLightBeforeSlits)
print("Time light takes to travel that distance {}".format(timeLightGoHalfDistanceBetween))
initialDistanceOfAAfterSlits = mp.mpf(timeLightGoHalfDistanceBetween * speedOfLightAfterSlits)
print("distance light goes in that time after it enters the slits {}".format(
    initialDistanceOfAAfterSlits))

# now to find the distance light needs to travel for the first possible interaction between the two waves
# after the slits.

halfTotalDistanceToFirstPossibleInteraction = mp.mpf((distanceBetweenSlits - initialDistanceOfAAfterSlits) / 2)
print("half the total distance to the first possible interaction {} m".format(
    halfTotalDistanceToFirstPossibleInteraction))
# I am going to find the phase at wave b then go up to the next instance of 2 pi so when I then find the \
# distance to the wave of A, I can be sure I won't run into the problem of scaling down A so much that
# b wave won't reach it.
# phase of wave b
cyclesInDistance = mp.mpf(halfTotalDistanceToFirstPossibleInteraction / wavelength)
print("Cycles in distance {}".format(cyclesInDistance))
phaseOfBWave = mp.mpf((cyclesInDistance % 1) * 2)
print("phase of wave b at distance the two waves would first interact {}".format(phaseOfBWave))
if phaseOfBWave + initialPhaseAtSecondSlit < 2:
    phaseOfBWavePlusInitialPhase = mp.mpf(phaseOfBWave + initialPhaseAtSecondSlit)
else:
    phaseOfBWavePlusInitialPhase = mp.mpf(phaseOfBWave + initialPhaseAtSecondSlit - 2)
print("phase of wave b + initial phase at b {}".format(phaseOfBWavePlusInitialPhase))
bWaveDistanceTo2pi = mp.mpf(((2 - phaseOfBWavePlusInitialPhase) / 2) * wavelength)  # divide by 2 to get it within the
# range
# of 0-2pi
print("distance from b wave phase to 2pi {}".format(bWaveDistanceTo2pi))
# up to the next 2pi
bWaveAt2piPlusWavelength = mp.mpf(halfTotalDistanceToFirstPossibleInteraction + bWaveDistanceTo2pi + wavelength)
# adding distance to 2pi because we are going up to the next 2pi
print("total distance of b wave up to next 2pi {}".format(bWaveAt2piPlusWavelength))
# We know that wave a will move the same amount as wave b, so we just need to add it
AWaveTotalDistance = mp.mpf(bWaveAt2piPlusWavelength + initialDistanceOfAAfterSlits)
print("total distance of wave a when b wave is at second 2pi {}".format(AWaveTotalDistance))
# now to find the phase of wave A
waveAPhase = mp.mpf((((AWaveTotalDistance / wavelength) % 1) * 2) + initialPhaseAtFirstSlit)

# if above 2 subtract 2. maybe I should do mod 2
if waveAPhase >= 2:
    waveAPhase = mp.mpf(waveAPhase - 2)
print("phase A wave at total length {}".format(waveAPhase))
# find the distance light propagates in the distance to the 2pi before
distanceOfPhaseA = mp.mpf((waveAPhase / 2) * wavelength)
print("distance to phase of A wave {}".format(distanceOfPhaseA))
# find the length of wave A at 2pi
AWaveAt2pi = mp.mpf(AWaveTotalDistance - distanceOfPhaseA)
print("the last instance of 2pi on wave a {}".format(AWaveAt2pi))
# now to use the law of cosines to find the angles where the lengths will meet
angleC1 = mp.mpf(acos((AWaveAt2pi ** 2 + bWaveAt2piPlusWavelength ** 2 - distanceBetweenSlits ** 2) / (
        2 * AWaveAt2pi * bWaveAt2piPlusWavelength)))
print("angle C of point 1 {}".format(degrees(angleC1)))
angleA1 = mp.mpf(acos((bWaveAt2piPlusWavelength ** 2 + distanceBetweenSlits ** 2 - AWaveAt2pi ** 2) / (
        2 * bWaveAt2piPlusWavelength * distanceBetweenSlits)))
print("angle A of point 1 {}".format(degrees(angleA1)))
angleB1 = mp.mpf(acos((distanceBetweenSlits ** 2 + AWaveAt2pi ** 2 - bWaveAt2piPlusWavelength ** 2) / (
        2 * distanceBetweenSlits * AWaveAt2pi)))
print("angle B of point 1 {}".format(degrees(angleB1)))
# find the angles of the next point
waveADistance2 = mp.mpf(AWaveAt2pi + (wavelength * 1000))
print("distance of wave a + wavelength {}".format(waveADistance2))
bDistance2 = mp.mpf(bWaveAt2piPlusWavelength + (wavelength * 1000))
print("distance of wave b + wavelength {}".format(bDistance2))
# next set of law of cosines
angleC2 = mp.mpf(acos((waveADistance2 ** 2 + bDistance2 ** 2 - distanceBetweenSlits ** 2) / (
        2 * waveADistance2 * bDistance2)))
print("angle C of point 2 {}".format(degrees(angleC2)))
angleA2 = mp.mpf(acos((bDistance2 ** 2 + distanceBetweenSlits ** 2 - waveADistance2 ** 2) / (
        2 * bDistance2 * distanceBetweenSlits)))
print("angle A of point 2 {}".format(degrees(angleA2)))
angleB2 = mp.mpf(acos((distanceBetweenSlits ** 2 + waveADistance2 ** 2 - bDistance2 ** 2) / (
        2 * distanceBetweenSlits * waveADistance2)))
print("angle B of point 2 {}".format(degrees(angleB2)))
# now that I have the angles I can find the x and y of each point
y1 = mp.mpf(AWaveAt2pi * sin(angleB1))
print("y value of spot 1 {}".format(y1))
y2 = mp.mpf(waveADistance2 * sin(angleB2))
print("y value of spot 2 {}".format(y2))
x1 = mp.mpf(AWaveAt2pi * cos(angleB1))
print("x value of spot 1 {}".format(x1))
x2 = mp.mpf(waveADistance2 * cos(angleB2))
print("x value of spot 2 {}".format(x2))
# we have all the spots now to find the distance and angle
x = mp.mpf(x2 - x1)
print("x {}".format(x))
y = mp.mpf(y2 - y1)
print("y {}".format(y))
d = mp.mpf(sqrt(x ** 2 + y ** 2))
print("d {}".format(d))
# angle sin(theta) = y / d
# I mixed up the x and y values so the y value corresponds to the value adjacent to the normal line
# which means the x value is the distance away from the normal line
angleOfPoints = mp.mpf(asin(x / d))
print("angle of the triangle made by the points is {}".format(degrees(angleOfPoints)))

# comparing my results to snell's law
