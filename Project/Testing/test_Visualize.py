import unittest
import Project.Visualize as vis
import Project.MinSpanTree as mst
import Project.DistanceSongs as ds
import Project.KMeans as kmeans


class test_Visualize(unittest.TestCase):

    def setup_vis(self):

        # NEED:
        # 	Cluster_dict
        #	mst
        #	scaledvalues

        self.audio_feats = {
            '0lizgQ7Qw35od7CYaoMBZb': [0.41125541125541126, 0.624235006119951, 0.6363636363636364, 0.6701321475543307,
                                       1.0, 0.18845429826396154, 0.04924561820012607, 0.0, 0.5878116343490305,
                                       0.8413295703982439],
            '6osaMSJh9NguagEDQcZaKx': [0.655122655122655, 0.7919216646266829, 1.0, 0.9443226654975887, 1.0,
                                       0.40179878686467263, 0.2836852144441807, 2.0395738203957383e-06,
                                       0.3440443213296399, 0.8425773492212816],
            '3ZCTVFBt2Brf31RLEnCkWJ': [0.6695526695526695, 0.13953488372093023, 0.5454545454545454, 0.22609131333375082,
                                       0.0, 0.15373352855051245, 0.9222286804253682, 1.0, 0.20221606648199447,
                                       0.37165516880944915]
        }

        distances = ds.DistanceSongs()
        adj_dict = distances.find_distances(self.audio_feats)


        vis_kmeans = kmeans.Kmeans()
        vis_kmeans.k_means(self.audio_feats)

        vis_mst = mst.MinSpanTree()
        vis_mst.create_min_span_tree(adj_dict)




        self.vis = vis.Visualize(vis_kmeans.clusters, vis_mst, vis_kmeans.scaled)
