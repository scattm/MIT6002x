from inDictTests import collision_prob, observe_prob

print "Ans 1 is %f" % collision_prob(1000, 50)

print "Ans 2 is %f" % collision_prob(1000, 200)

print "Ans 3 is %f" % observe_prob(1000, 50, 1000)

print "Ans 4 is %f" % observe_prob(1000, 200, 1000)

print "Ans 5 is %f" % collision_prob(365, 30)

print "Ans 5 is %f" % collision_prob(365, 250)

for i in range(0, 250):
    if collision_prob(365, i) >= 0.99:
        print "The maximum class size is %d" % (i - 1)
        break
