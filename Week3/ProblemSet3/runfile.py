from ps3b import *
import random

random.seed(0)
simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
