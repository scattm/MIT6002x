import random


def do3Draw(bucket):
    for i in range(3):
        if random.random() < float(bucket['green'])/(bucket['red'] + bucket['green']):
            bucket['green'] -= 1
        else:
            bucket['red'] -= 1
    return bucket


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    sameColorDraw = 0.0
    for trial in range(numTrials):
        bucket = {
            'green': 4,
            'red': 4
        }
        do3Draw(bucket)
        if bucket['green'] == 1 or bucket['red'] == 1:
            sameColorDraw += 1

    return sameColorDraw/numTrials

print drawing_without_replacement_sim(1000)