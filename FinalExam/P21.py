import numpy

a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*numpy.array(yVals)
xVals = numpy.array(xVals)
try:
    a, b, c, d = numpy.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'