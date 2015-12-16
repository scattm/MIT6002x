from clusterCities import *

# points = buildCityPoints('test.txt', False)
# hCluster(points, Cluster.singleLinkageDist, 3, False)
# hCluster(points, Cluster.maxLinkageDist, 3, False)
# hCluster(points, Cluster.averageLinkageDist, 3, False)

# test()

# 3.1
points = buildCityPoints('cityTemps.txt', False)
hCluster(points, Cluster.singleLinkageDist, 10, False)
#  C2:Anchorage
#  C3:Duluth
#  C4:Fairbanks
#  C5:Honolulu
#  C9:Olympia


# 3.2

# points = buildCityPoints('cityTemps.txt', True)
# hCluster(points, Cluster.singleLinkageDist, 5, False)

#  C1:Anchorage
#  C2:Fairbanks
#  C3:Honolulu
#  C4:SanFrancisco

# points = buildCityPoints('cityTemps.txt', False)
# hCluster(points, Cluster.singleLinkageDist, 5, False)

#  C1:Anchorage
#  C2:Fairbanks
#  C3:Honolulu

# 3.3
# True

