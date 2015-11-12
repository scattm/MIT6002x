import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    noOfSameColor = 0.0
    for trial in range(numTrials):
        bucket = {
            'red' : 3,
            'green' : 3
        }

        for i in range(3):
            bucket = takeBall(bucket)

        if bucket['red'] == 0 or bucket['green'] == 0:
            noOfSameColor += 1

    return noOfSameColor/numTrials

def takeBall(bucket):
    if random.random() < float(bucket['red'])/(bucket['red']+bucket['green']):
        bucket['red'] -= 1
    else:
        bucket['green'] -= 1
    return bucket

if __name__ == '__main__':
    numTrails = 1000000
    for i in range(5):
        print "Fraction of taking 3 same color ball in %d trial is %f" % (
            numTrails,
            noReplacementSimulation(numTrials=numTrails)
        )
