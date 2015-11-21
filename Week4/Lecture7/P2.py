import random
from matplotlib import pylab

def testErrors(ntrials=100000,npts=100):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.uniform(-1,1)
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Uniform (100,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

testErrors()
pylab.show()