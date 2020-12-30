
import Project.AudioFeatures as af
import Project.DistanceSongs as ds
import Project.MinSpanTree as mst
import Project.Visualize as vis
import Project.KMeans as km

x = []
with open('Testing/test_manual_clustering.txt') as f:
    lines = f.readlines()
    for line in lines:
        x.append(line.strip())
print(x)

audio = af.AudioFeatures()
audio.get_features(x)

dist = ds.DistanceSongs()
dist.find_distances(audio.features)

minspantree = mst.MinSpanTree()
minspantree.create_min_span_tree(dist.adj_dict)

kmeans = km.Kmeans()
kmeans.k = 7
kmeans.k_means(audio.features)

vis.Visualize(kmeans.clusters, minspantree.MST_graph, kmeans.scaled)


