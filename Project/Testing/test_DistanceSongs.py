# -------------------------------------- TESTING ------------------------------------------
import unittest
import numpy as np
import Project.DistanceSongs as ds


class test_DistanceSongs(unittest.TestCase):

    def setup_DistanceSongs(self):
        self.ds = ds.DistanceSongs()

    def test_find_distances(self):
        self.setup_DistanceSongs()

        id1 = 'id1'
        id2 = 'id2'
        id3 = 'id3'
        id4 = 'id4'
        id5 = 'id5'

        feat1 = np.array([3, 4, 5, 6, 7])
        feat2 = np.array([1, 2, 2, 1, 4])
        feat3 = np.array([4, 5, 8, 3, 2])
        feat4 = np.array([2, 6, 2, 3, 5])
        feat5 = np.array([5, 1, 6, 2, 3])

        features_to_test = {id1:feat1,
                            id2: feat2,
                            id3: feat3,
                            id4: feat4,
                            id5: feat5,
        }

        ans_adj_dict = {('id1', 'id2'): np.sqrt(np.sum(np.square(feat1 - feat2))),
                        ('id1', 'id3'): np.sqrt(np.sum(np.square(feat1 - feat3))),
                        ('id1', 'id4'): np.sqrt(np.sum(np.square(feat1 - feat4))),
                        ('id1', 'id5'): np.sqrt(np.sum(np.square(feat1 - feat5))),
                        ('id2', 'id3'): np.sqrt(np.sum(np.square(feat2 - feat3))),
                        ('id2', 'id4'): np.sqrt(np.sum(np.square(feat2 - feat4))),
                        ('id2', 'id5'): np.sqrt(np.sum(np.square(feat2 - feat5))),
                        ('id3', 'id4'): np.sqrt(np.sum(np.square(feat3 - feat4))),
                        ('id3', 'id5'): np.sqrt(np.sum(np.square(feat3 - feat5))),
                        ('id4', 'id5'): np.sqrt(np.sum(np.square(feat4 - feat5)))

                        }

        # answers = [math.sqrt(135.0), math.sqrt(26.0), math.sqrt(118.0), math.sqrt(122.0), math.sqrt(75.0)]
        self.ds.find_distances(features_to_test)
        self.assertEqual(self.ds.adj_dict, ans_adj_dict)

if __name__ == '__main__':
    unittest.main()

        # x = DistanceSongs()
        # x.find_distances({'2FRnf9qhLbvw8fu4IBXx78': [0.7142857142857142, 0.44920440636474906, 0.18181818181818182, 0.35022233356297366, 1.0, 0.007111482953357039, 0.19261090599494077, 3.7747336377473363e-06, 0.9822714681440443, 0.2911440367931431], '7M9w4C8WenlvWfNRAulZOX': [0.7344877344877344, 0.6817625458996328, 0.9090909090909091, 0.7578129892904114, 0.0, 0.07299728090357666, 0.03737525889662964, 0.0004140030441400304, 0.33850415512465376, 0.2932214905403993]})
        # print(x.adj_dict)
