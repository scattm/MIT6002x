# 6.00.2x Problem Set 4

import numpy
import random
from matplotlib import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    stepsBeforeTreatment = [300, 150, 75, 0]
    noOfFinalViruses = {}
    treatmentStep = 150

    for noTreatmentSteps in stepsBeforeTreatment:
        noOfFinalViruses[noTreatmentSteps] = []

        for trials in range(numTrials):
            viruses = [ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005) for i in range(100)]
            patient = TreatedPatient(viruses, 1000)

            for step in range(noTreatmentSteps):
                patient.update()

            patient.addPrescription('guttagonol')

            for step in range(treatmentStep):
                patient.update()

            noOfFinalViruses[noTreatmentSteps].append(patient.getTotalPop())

        pylab.hist(noOfFinalViruses[noTreatmentSteps], range(0, 700, 50))

        pylab.title('ResistantVirus simulation with %d step delay' % noTreatmentSteps)
        pylab.xlim([0, 700])
        pylab.xlabel('# Viruses')
        pylab.ylabel('# Trials')
        pylab.show()


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    print 'Initial the parameters'
    noTreatmentSteps = 150
    applyGuttagonolSteps = [300, 150, 75, 0]
    applyGrimpexSteps = 150
    startPop = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    noOfFinalViruses = {}

    print 'Starting the simulation...'
    for guttagonolDelay in applyGuttagonolSteps:
        print '%d steps of guttagonol' % guttagonolDelay
        noOfFinalViruses[guttagonolDelay] = []

        for trial in range(numTrials):
            # print 'Begin trial %d' % trial

            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(startPop)]
            patient = TreatedPatient(viruses, maxPop)

            # print ' %d step of no treatment' % noTreatmentSteps
            for step in range(noTreatmentSteps):
                patient.update()

            # print ' Apply guttagonol for %d step' % guttagonolDelay
            patient.addPrescription('guttagonol')
            for step in range(guttagonolDelay):
                patient.update()

            # print ' Apply grimpex for %d step' % applyGrimpexSteps
            patient.addPrescription('grimpex')
            for step in range(applyGrimpexSteps):
                patient.update()

            # print 'Get final # of viruses'
            noOfFinalViruses[guttagonolDelay].append(patient.getTotalPop())

        pylab.hist(noOfFinalViruses[guttagonolDelay], range(0, 700, 50))
        pylab.title('Apply treatment with %d steps of guttagonol, then %d steps of grimpex' % (
            guttagonolDelay,
            applyGrimpexSteps
        ))
        pylab.xlim([0, 700])
        pylab.xlabel('# Viruses')
        pylab.ylabel('# Trials')
        pylab.show()

        print numpy.var(noOfFinalViruses[guttagonolDelay])
