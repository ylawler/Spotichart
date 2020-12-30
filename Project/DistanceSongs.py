from scipy.spatial import distance

class DistanceSongs:

    def __init__(self):
        self.adj_dict = dict()

    def find_distances(self, features):
        for song1 in features:
            for song2 in features:
                if song1 != song2:
                    weight = distance.euclidean(features[song1], features[song2])
                    edge = (song1, song2)
                    edge_swap = (song2, song1)
                    if not edge_swap in self.adj_dict.keys():
                        self.adj_dict[edge] = weight



