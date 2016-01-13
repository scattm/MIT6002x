from clusterCities import *

points = buildCityPoints('fepoint.txt', False)

# hCluster(points, Cluster.singleLinkageDist, 4, False)
# hCluster(points, Cluster.maxLinkageDist, 4, False)
# hCluster(points, Cluster.averageLinkageDist, 4, False)
# hCluster(points, Cluster.mysteryLinkageDist, 4, False)

hCluster(points, Cluster.mysteryLinkageDist, 3, False)
