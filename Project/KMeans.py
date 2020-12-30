import sklearn.preprocessing as skp
import sklearn.cluster as skc
import Project.AudioFeatures as AF
import numpy as np
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import silhouette_score


class Kmeans:

    def __init__(self):
        self.k = 10
        self.clusters = dict()
        self.scaled = None


    def k_means(self, audiofeatures):

        # Extract only the numerical values from the audiofeatures dictionary
        def access_features(values):
            return np.vstack([np.array(values[key]) for key in values])

        # Apply scaler to numerical values in dict
        def transform(scaler, data):
            audiofeatures_transformed = {}
            for key in data:
                audiofeatures_transformed[key] = scaler.transform(np.array(data[key]).reshape(1, -1))
            return audiofeatures_transformed

        #scale data
        scaler = skp.StandardScaler()
        numeric = access_features(audiofeatures)
        scaler.fit(numeric)
        scaled = transform(scaler, audiofeatures)
        self.scaled = scaled

        #fit model and predict clusters
        model = skc.KMeans(n_clusters=self.k)
        model.fit(access_features(scaled))
        classified = [(key, model.predict(scaled[key])[0]) for key in scaled]

        #save clusters in self.clusters dictionary
        for cluster in range(self.k):
            self.clusters[cluster] = []

        for song in classified:
            uri = song[0].split(':')[-1]
            clst = song[-1]
            for key in self.clusters:
                if key == clst:
                    self.clusters[clst].append(uri)

        def Silhouette_method(data):
            cluster_labels = model.fit_predict(data)
            silhouette_value = silhouette_score(data, cluster_labels)
            # return print(silhouette_value)

        Silhouette_method(access_features(scaled))


    def elbow(self, audiofeatures):

        X = np.vstack(np.array(audiofeatures[key]) for key in audiofeatures)

        # Instantiate the clustering model and visualizer
        model = skc.KMeans()
        visualizer = KElbowVisualizer(
            model, k=(4, 25), timings=False
        )
        visualizer.elbow_value_
        visualizer.fit(X)  # Fit the data to the visualizer
        visualizer.show()  # Finalize and render the figure





