import random
from matplotlib import pyplot, pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    rabbit_birth_p = 1 - (float(CURRENTRABBITPOP)/MAXRABBITPOP)

    new_rabbit_pop = CURRENTRABBITPOP
    for i in range(CURRENTRABBITPOP):
        if random.random() <= rabbit_birth_p:
            new_rabbit_pop += 1

    CURRENTRABBITPOP = new_rabbit_pop


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    if CURRENTFOXPOP < 10:
        return

    fox_eat_rabbit_p = float(CURRENTRABBITPOP)/MAXRABBITPOP

    new_fox_pop = CURRENTFOXPOP
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
        if random.random() <= fox_eat_rabbit_p:
            if random.randint(0, 2) == 0:
                new_fox_pop += 1
        else:
            if random.random() <= 0.9 and new_fox_pop > 10:
                new_fox_pop -= 1

    CURRENTFOXPOP = new_fox_pop


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    ret_rabbit = [CURRENTRABBITPOP]
    ret_fox = [CURRENTFOXPOP]
    for i in range(numSteps):
        if CURRENTFOXPOP >= 10 and CURRENTRABBITPOP >= 10:
            rabbitGrowth()
            foxGrowth()
        ret_rabbit.append(CURRENTRABBITPOP)
        ret_fox.append(CURRENTFOXPOP)

    return ret_rabbit, ret_fox

rp, fp = runSimulation(200)

rl, = pyplot.plot(rp, label="Rabbit population")
fl, = pyplot.plot(fp, label="Fox population")
pyplot.legend(handles=[rl, fl])
pyplot.show()

rcoeff = pylab.polyfit(range(len(rp)), rp, 2)
rcl, = pyplot.plot(pylab.polyval(rcoeff, range(len(rp))), label="Rabbit Coefficients")
fcoeff = pylab.polyfit(range(len(fp)), fp, 2)
fcl, = pyplot.plot(pylab.polyval(fcoeff, range(len(fp))), label="Fox Coefficients")
pyplot.legend(handles=[rcl, fcl])
pyplot.show()
