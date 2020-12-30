import Project.MinSpanTree as MsT
import matplotlib.pyplot as plt
import networkx as nx
import Project.AudioFeatures as af
import Project.DistanceSongs as ds
import Project.KMeans as kms
import pandas as pd
import random
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Visualize:
    def __init__(self, cluster_dict, mst, scaledvalues):
        self.colorlist = ['tomato', 'chartreuse', 'xkcd:lightblue', 'yellow', 'orange', 'pink', 'violet', 'tan',
                          'silver', 'aquamarine']
        self.draw_graph(mst, cluster_dict)
        self.clustered_songs(cluster_dict)
        self.PCA_graphs(cluster_dict, scaledvalues)

    def draw_graph(self, mst, cluster_dict):
        f1 = plt.figure()
        plt.title('Minimum Spanning Tree')

        pos1 = nx.spring_layout(mst, weight='weight')
        for cluster in cluster_dict:
            nx.draw_networkx_nodes(mst, pos= pos1, node_size=50, nodelist=cluster_dict[cluster], node_color=self.colorlist[cluster], label= f"Cluster {cluster}")
            labels = {}
            i = 0
            for song in cluster_dict[cluster]:
                labels[song] = f'{i}'
                i += 1
            nx.draw_networkx_labels(mst, pos= pos1, labels = labels, font_size = 5 )
        nx.draw_networkx_edges(mst, pos1, width = 0.5)

        plt.legend()
        #pdf file name is generated randomly
        r = random.randrange(1, 10**5)
        plt.savefig(f"mstgraph{r}.pdf",bbox_inches ='tight')

        f2 = plt.figure()
        f2.set_tight_layout(False)
        plt.title('Minimum Spanning Tree')
        for cluster in cluster_dict:
            nx.draw_networkx_nodes(mst, pos= pos1, node_size=100, nodelist=cluster_dict[cluster], node_color=self.colorlist[cluster], label= f"Cluster {cluster}")
        nx.draw_networkx_edges(mst, pos1, width = 1)
        plt.legend()
        plt.show()

    def get_names(self, song_ids):
        cid = "5981b769c7664e4fbb62599aafb79173"
        secret = "0ec407bb50aa48aeab9c3b8224e0c6a8"

        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        songs = []
        i = 0
        for id in song_ids:
            name = sp.track(f"spotify:track:{id}")
            songs.append(f"{i} : {name['name']}  -  {name['artists'][0]['name']}   --> http://open.spotify.com/track/{id}")
            i += 1
        return songs

    def clustered_songs(self, cluster_dict):
        artist_song = dict()
        length = []
        for key in cluster_dict:
            artist_song[f"Cluster {key}"] = self.get_names(cluster_dict[key])
            length.append(len(artist_song[f"Cluster {key}"]))

        max_len = max(length)

        for key in artist_song:
            lt = len(artist_song[key])
            if not max_len == length:
                artist_song[key].extend([''] * (max_len - lt))

        clst = pd.DataFrame.from_dict(artist_song)
        pd.set_option('display.max_colwidth', -1)
        pd.set_option("display.colheader_justify", "left")

        print(clst.to_string())

    def PCA_graphs(self,cluster_dict, scaled):
        X = [] #all numerical values of songs
        y = [] #cluster of songs
        for key in scaled:
            X.append(scaled[key][0])
            for cluster in cluster_dict:
                if key in cluster_dict[cluster]:
                    y.append(cluster)

        #do PCA
        pca = decomposition.PCA(n_components=3)
        pca.fit(X)
        X = pca.transform(X)

        #make sure labels of y can be recognized
        y = np.choose(y, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).astype(np.float)

        #plot from 1st angle
        fig1 = plt.figure(1, figsize=(4, 3),dpi=400)
        fig1.set_tight_layout(False)
        plt.clf()
        ax1 = Axes3D(fig1, elev=30, azim=240)  # rect=[0, 0, .95, 1]

        labels = set()
        for i in range(len(X)):

            if int(y[i]) in labels:
                ax1.scatter(X[i, 0], X[i, 1], X[i, 2], c=self.colorlist[int(y[i])],
                       edgecolor='k', s=20)
            else:
                ax1.scatter(X[i, 0], X[i, 1], X[i, 2], c=self.colorlist[int(y[i])],
                            edgecolor='k', s=20, label=f"Cluster {int(y[i])}")
                labels.add(int(y[i]))
        ax1.w_xaxis.set_ticklabels([])
        ax1.w_yaxis.set_ticklabels([])
        ax1.w_zaxis.set_ticklabels([])


        # Get the handles and labels
        handles, labels = ax1.get_legend_handles_labels()
        # sort both labels and handles by labels
        labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
        #ax1.legend(handles, labels)


        # legend on the side
        ax1.legend(handles, labels, loc='center left', frameon=True,
                   fontsize='xx-small')  # , bbox_to_anchor=(1.04, 0.5))


        # legend at the bottom
        #ax1.legend(handles, labels, loc='lower right', mode='expand', ncol=5, frameon=True,
         #           fontsize='xx-small') #, bbox_to_anchor=(1.04, 0.5))

        plt.title('Clusters visualized with PCA 1')
        plt.show()

        #plot from 2nd angle
        fig2 = plt.figure(1, figsize=(4, 3),dpi=400)
        fig2.set_tight_layout(False)
        plt.clf()
        ax2 = Axes3D(fig2, elev=30, azim=120)  # rect=[0, 0, .95, 1]

        for i in range(len(X)):
            ax2.scatter(X[i, 0], X[i, 1], X[i, 2], c=self.colorlist[int(y[i])],
                       edgecolor='k', s=20)  # , cmap=plt.cm.nipy_spectral,
        ax2.w_xaxis.set_ticklabels([])
        ax2.w_yaxis.set_ticklabels([])
        ax2.w_zaxis.set_ticklabels([])
        plt.title('Clusters visualized with PCA 2')
        plt.show()

        #plot from 3d angle
        fig3 = plt.figure(1, figsize=(4, 3), dpi=400)
        fig3.set_tight_layout(False)
        plt.clf()
        ax3 = Axes3D(fig3, elev=30, azim=360)

        for i in range(len(X)):
            ax3.scatter(X[i, 0], X[i, 1], X[i, 2], c=self.colorlist[int(y[i])],
                        edgecolor='k', s=20)
        ax3.w_xaxis.set_ticklabels([])
        ax3.w_yaxis.set_ticklabels([])
        ax3.w_zaxis.set_ticklabels([])
        plt.title('Clusters visualized with PCA 3')
        plt.show()



