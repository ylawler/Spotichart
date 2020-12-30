# Design Plan

#### Design

The main flow and the different classes we will implement are visualised in UML diagrams:

[UML class diagram](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Design%20plan/Design%20diagrams%20and%20visualisations/Class_diagram_v8.png)

[UML activity diagram](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Design%20plan/Design%20diagrams%20and%20visualisations/UML_activity_diagram_version_4.png)

#### Methods and Tools

In the table below, an overview of the different modules used can be seen. 

| Class | Modules |
| ------ | ------ |
| UserInterface | pycountry |
| WebScrapeCharts | BeautifulSoup, requests |
| AudioFeatures | spotipy |
| KMeans | scikit-learn |
| DistanceSongs | math |
| MinSpanTree | networkx |
| Visualize | matplotlib | 

The UserInterface class uses the get_user_input function to ask the user to enter the country and recurrence of the top 200 chart they are interested in. The get_country_code function uses the pycountry module to get the corresponding
country code of the given country. If this fails the user will be asked again to check their input and re-enter a country or recurrence. Once a valid country
code is found, it will be passed along with the given recurrence to the WebScrapeCharts class.

The WebScrapeCharts class finds all the songs in the top 200 Charts of the specific country and recurrence the user entered. The country code and recurrence input from the 
UserInterface class are passed into the get_charts function and calls generate_url which updates the url. Using the requests module it then performs a HTTP request to get the song ID's of all the 200 songs. This request is then
parsed using Beautifulsoup to turn the HTTP request into a string value.

The get_features function in the AudioFeatures class accesses spotify using the spotipy module. It collects the desired features for each song and stores them in a dictionary.

Within the KMeans class, the k_means function follows the K means algorithm, for which it uses the scikit-learn module, in order to determine the different clusters for our songs. 
Our input values for each song will be the audio features, which we will first normalize so every feature has the same weight. We are going to use the 
elbow method to select the optimal amount of clusters (K) the algorithm is going to create. This is explained in the validation section. If it does not take too much computational cost and running time, we want to automatically select the optimal k value every time we run the algorithm. 
However, if it does increase our running time significantly, we will calculate the optimal K for a few charts of different dates, compute the average value and continue to use this value for K.
The k_means function creates clusters based on this information.

In the DistanceSongs class, the find_distances function calculates the euclidian distance, using the math module, between the songs based on the normalized values of their audio features.
The MinSpanTree class uses the networkx module in order to calculate the minimum spanning tree of all the songs and their connectedness. The function
create_min_span_tree takes a dictionary of all the adjacent edges and creates a networkx graph by adding all the edges and their weights to it. Finally, the
minimum spanning tree can be generated from this graph using networkx.algorithms.tree.minimum_spanning_tree

In the Visualize class, the draw_graph function displays the minimum spanning tree and indicates each cluster by a different node color. The visualisation of this can be found [here](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Design%20plan/Design%20diagrams%20and%20visualisations/visualisation_clusters_MST.png). 
In this image the nodes represent the different songs and the colors indicate what cluster they are in. The edges represent the distance between the different songs.
The display_clusters function will show the list of songs in each cluster.

#### Considerations

For our clustering we have chosen to use the K-means method instead of the K-nearest neighbours (KNN), which we first intended to use.
We found that the unsupervised learning method of K-means can cluster unlabeled songs, whereas KNN requires a label for the training data and then classifies songs into these labels, such as genre.
Since our project is about analyzing the connectedness between songs instead of classifying them, we decided K Means would be more suitable.

We also had to select an appropriate module to help us implement the K-Means algorithm. We discovered both tensorflow and scikit learn were good options, so we decided to install and start working with both modules to find which worked best for us. We found we made bigger steps with our scikit implementation, so we decided to continue using the module

#### Validation

To validate our results, we will use the [Silhouette method](https://en.wikipedia.org/wiki/Silhouette_(clustering)). The silhouette value measures how similar an object is to its own cluster. The value ranges from -1 to 1, where value 1 means that the point is far away from its neighbour clusters. 
The value 0 means that the point is on a decision boundary between two clusters and value -1 means that it might be located in the wrong cluster. We want to use this to see whether the clusters are distinct and correct.
Another validation method is the sum of squared errors, where you calculate the sum of the square of residuals, which is the difference between the data and mean of the cluster. If we plot these values for different values of k, we can obtain the ideal k value with the elbow method.

We will also check the similarity of the different songs in the clusters by picking a few song and listening to them to see whether we agree on the clustering. 
The same will be done for songs that are close to each other on the minimum spanning tree and songs that are very far apart. 
We can compare results of the K Means clusters and the minimum spanning tree to see for example how similar songs of different clusters are. 
We will also cluster a list of songs ourselves by listening to them, and give the same list of songs as input to our clustering algorithm. We can then see whether these results are similar. 
