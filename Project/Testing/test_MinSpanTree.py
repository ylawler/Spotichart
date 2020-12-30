import unittest
import Project.MinSpanTree as mst


class test_MinSpanTree(unittest.TestCase):

    def setup_mst(self):
        self.test_mst = mst.MinSpanTree()

        self.adj_dict_5_nodes = {
            ('id1', 'id2'): 1, # -> min edge
            ('id1', 'id3'): 2, # -> min edge
            ('id1', 'id4'): 1, # -> min edge
            ('id1', 'id5'): 5,

            ('id2', 'id3'): 5,
            ('id2', 'id4'): 4,
            ('id2', 'id5'): 3,

            ('id3', 'id4'): 4,
            ('id3', 'id5'): 2,

            ('id4', 'id5'): 1 # -> min edge
        }

        self.adj_dict_3_nodes = {
            ('id1', 'id2'): 1,  # -> min edge
            ('id1', 'id3'): 1,  # -> min edge
            ('id2', 'id3'): 2,
        }


    def edges_into_array(self, edges):
        mst_edges = []
        for mst_edge in edges:
            mst_edges.append(mst_edge)
        return mst_edges

    def test_create_min_span_tree_5_nodes(self):
        # 5 Nodes means a MST with 4 edges
        self.setup_mst()
        self.test_mst.create_min_span_tree(self.adj_dict_5_nodes)
        array_edges = self.edges_into_array(self.test_mst.MST_graph.edges)

        self.assertEqual(array_edges, [('id1','id2'), ('id1','id4'), ('id1','id3'), ('id4','id5')])
        self.assertEqual(len(array_edges),4)

    def test_create_min_span_tree_3_nodes(self):
        # 3 Nodes means a MST with 2 edges
        self.setup_mst()
        self.test_mst.create_min_span_tree(self.adj_dict_3_nodes)
        array_edges = self.edges_into_array(self.test_mst.MST_graph.edges)

        self.assertEqual(array_edges, [('id1','id2'),('id1','id3')])
        self.assertEqual(len(array_edges), 2)


if __name__ == '__main__':
    unittest.main()
