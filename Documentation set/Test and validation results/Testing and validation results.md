## Testing

In order to determine whether our classes are correct and return the desired results, it is important to include testing alongside coding. 
For most of the classes, unit testing was applied, and it was made sure that every function in each class was tested. This ensured that the 
line coverage would be as high as possible, and also that our code is accurate. To cover the classes for which we did not write unit tests, we did manual testing.

#### Line Coverages

In the following table the individual line coverages for each class can be seen. Most of them are 100% or very close with 96%, 
which is very good and ensures us the code in those classes is accurate. However, in the case of the Visualize class, only manual testing was done, 
as this class focussed on displaying and visualizing the clusters. It was difficult to have automated tests for validating whether the visualizations were correct. Finally, the KMeans class 
reached a 75% line coverage. Similarly to the Visualize class, the KMeans class also displays certain results in a figure, for which manual testing was 
done. This was for the Elbow method function that tried to determine the optimal k value for the K-means algorithm. The other functions in the 
KMeans class were tested using automated testing.

| Class | Line coverage |
| ------ | ------ |
| UserInterface | 100% |
| WebScrape 	| 100% |
| AudioFeatures | 96% |
| DistanceSongs | 100% |
| KMeans | 75%		|
| MinSpanTree | 100% |
| Visualize |   Manual |




## Validation

To validate the algorithm on how well it clusters, we use multiple ways of validation. We use the elbow- and silhouette method and we are clustering a playlist on our own and then comparing it to the clustering done by the algorithm.
And at last we validate by clustering a random playlist and listening to the songs in its clusters and see what the differences are.

#### Elbow method

In order to determine a correct value for k, we used the elbow method. In this method, clusters are formed for a certain playlist using different predefined values of k. Next, the sum of squared distances from each song to the mean of its cluster is calculated. The values are then plotted, to see after which value of k this distortion score starts to decrease at a slower rate. This value, the elbow value, is automatically determined and then returned.
When we plotted the elbow graph for our top 200 charts, we ended up with elbow values between 8 and 16. However, this value was not consistent for each chart. Every time K means is run on a certain list of songs, different clusters are formed. The elbow value depends on this and turned out to vary with each run. For example, the Dutch daily chart of 5-12-2019 gave an elbow value of 16 in the first run, and 10 in [the second](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Test%20and%20validation%20results/elbow_value_cluster_nl_daily_05-12-2019.jpg). This shows that the division of songs into clusters was not unmistakable, meaning that our songs do not show distinct clusters. 
We first intended to determine the elbow value every time the program was run and then use this value for k. Because the resulting value depended more on each run than a certain playlist, we decided to leave this out, since it would not add more value to our program and would make it harder to evaluate different clusters and compare them. We chose a value of 10 for k, because this was in our interval of occurring values and overall gave us the clearest clusters without overfitting. 


#### Silhouette method

With the silhouette method one measures how similar an object is to its own cluster, as mentioned in the Design Plan. The silhouette value is easy to calculate using a built-in function in scikit-learn.
After the implementation of this method, we found out that the average value of the silhouette method is around 0.14 for the clusters of our charts. This value is close to 0, which means that the songs are not strongly matched to its own cluster. However, since the value was not lower than 0, not many songs were matched to the wrong cluster. This indicates that our clusters were not very distinctive. 
The number did not differ much for different charts and the value of k did not have a consistent influence on it either.



#### Comparing our self made clusters with clusters made by the algorithm

In order to check our algorithm, we decided to manually cluster songs ourselves and see whether or not the results were similar between our clusters and the clusters that the program produces. For this we used the 50 songs from the Dutch daily chart of 19-12-2019, which can be found [here](https://open.spotify.com/playlist/4kQyxPMAfu6D944XpZPKmo?si=P2KJfSWfRE2fs75NpFw1Lw). In [Cluster 1](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Test%20and%20validation%20results/Clusters_1.png) and [Cluster 2](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Test%20and%20validation%20results/Clusters_2.png) you can see our own clusters, as well as the clusters that the algorithm made.  

During the clustering of the songs, we instantly noticed that clustering is harder than we had expected, because of the large variety of features you have to take into account when listening to the songs.  
We noticed that we have a vastly different approach to clustering the songs than the computer does, whereas we listen more to the themes, the danceability of the song as well as the vocals. The program quickly gathers data for each song and mathematically compares the different features to each other resulting in different lists. Because of the association we already had with some of the songs, our way of clustering can be considered biased, whereas the program's method can be seen as factual. This association resulted in us clustering Christmas songs together more frequently, as well as Dutch songs for example. Another sign that clustering was a hard task, is the fact that no one had the same clusters. 

There were some similarities as two group members had one cluster that was identical. This cluster could be found in the algorithm's clusters split up over only two different clusters. However, only 5 songs in total were clustered together by all of the five members. If we also look at songs that were clustered together by 3 or 4 members of the group, we get more information on the results. 


In the table below we have summarized the results for groups of songs that at least 3 out of 4 team members had put in the same cluster. 
The first column shows the number of team members (out of the four that did clustering) that clustered the same songs together in the same cluster. The second shows how many songs this "subcluster" consists of. The third column shows how many of these song could be found in a cluster made by Spotichart. It elaborates on the division our algorithm made of the same songs we clustered together.  
So for example, for the first row we can see four out of four members had the same subgroup of two songs, which were found in two different clusters that were made by using K Means. 

| Team members | Number of songs in subcluster | Songs found together in algorithm's clusters |
| ------ | ------ | ------ |
| 4/4 | 2 | 50 % |
| 4/4 | 3 | 100 % |
| 3/4 | 6 | 83.3 % |
| 3/4 | 3 | 33.3 % |
| 3/4 | 4 | 75 % |
| 3/4 | 3 | 66.7 % |
| 3/4 | 2 | 50 % |
| 3/4 | 2 | 100 % | 
| 3/4 | 2 | 100 % |
| 3/4 | 2 | 100 % | 


In the table we can see the clustering of the algorithm overlaps in some of the cases, but is not always the same as our self made clusters. 
The validation method we have used does gives us information that is hard to interpret. Since the clusters were not labelled, we could not simply compare one 'Cluster 0' to another 'Cluster 0'. We have thoroughly analyzed the results to get some useful information out of it, but cannot derive clear conclusions yet. Therefore, we have mainly used the results of our second validation method, which is described in the following section. 




#### Evaluating clusters made by the algorithm

For the validation of the algorithm four different playlist where used. Because of the smaller size of this playlist (50 instead of 200 songs), the amount of clusters was reduced to 7, instead of the 10 clusters for the top 200.
In the table below the results of one of the validations is shown with their main genre and a description of what stood out in the cluster. The results shown are for the global top 50 of 9-1-2020.



| Cluster | Genre | Description |
| ------ | ------ | ------ |
| 0 | Pop/latin-pop | This cluster contains similar pop songs with the same tempo and danceability. It also contains some latin-pop which has a completely other beat pattern and there is one rap song that is clearly different from the other songs.   | 
| 1 | Hip-hop/rap | Most of the songs in this cluster have the same beat pattern and are up-tempo. This cluster also contains two slightly different verions of the same song, which is remarkable.| 
| 2 | Pop/electro-dance | Although the songs are similar in genre and are all a bit up-tempo, the energy and danceability differs a bit within the cluster and there is one rap track, which sounds very different from the rest.    | 
| 3 | Alternative/indie  | There is just one song in this cluster and it does sound completely different from the rest.   | 
| 4 | Latin-pop/electro-pop/hip-hop | The genres in this cluster are signifficantly different. It contains some up-tempo dance songs and a lot of slower latin-pop songs and there is again a rap song which sounds very different.      | 
| 5 | R&B/pop/alternative/indie/rap | This cluster contains the most genres. Almost every song has a strong and distinctive bass line and they are relatively slow, but it also contains some more up-tempo songs     | 
| 6 | Pop/pop-rock | In this cluster all of the songs are focussed on the vocals and acousticness and have the same genre, but there is one rap song that again isn't in the right cluster.    |


The clustering of the [top 50](https://gitlab.ewi.tudelft.nl/ewi3615tu/2019-2020/data/ewi3615tu-ds10/ewi3615tu-ds10/blob/master/Documentation%20set/Test%20and%20validation%20results/Top50_world.JPG) of the world is accurate to a certain extent. Almost every cluster has a main genre to which the songs belong, but the pop genre is seen more frequently in the different clusters. What stands out in the clusters is that for example cluster 0 contains pop and latin-pop, where latin-pop has a completely different beat pattern, which we would not have put together. Even though we would not put them together ourselves, we could see that SpotiChart has categorized them on tempo and danceability.

Rap songs are also spread over multiple different sounding clusters and we would have expected them in the same cluster. Cluster 1 contains two slightly different versions of the same song, which confirms the clusters are right to some extent. Cluster 4 has the multiple genres and the songs differ the most from each other. There are some up-tempo and some slower latin-pop songs. So we don’t really agree with the similarities in this cluster.
The songs in cluster 6, however, are very much the same. They all have a guitar as a main instrument and the songs are all focused on the vocals. This cluster contains again a rap song that we did not find similar to the rest. 
Another cluster that stands out is cluster 3, which only contains one song. Indeed, this song sounds really different from the other songs in the chart. 

The above evaluation is an example of a playlist we analysed. Different playlists gave in general the same results and somewhat recognizable outliers. What matches between the different validated playlists is that overall they clustere quite well. Songs with more acoustic instrument and vocals and more danceable songs and slower songs are clustered the best. But almost all of them have trouble clustering rap songs. There is always a cluster with a couple of rap songs, but some rap songs end up in other clusters.

We had a playlist in which hardly any outliers could be found, but in which the clusters would have been better had they been split up more. In any case, the number of clusters chosen was a consideration between under and overfitting. We saw in a couple of playlists that we validated that a higher value of k actually did a better clustering job. But this was not true for every playlist so we decided that more than 7 clusters would not add to the algorithm's performance. We also had a playlist containing Christmas songs. Even though we would cluster them all together, Spotichart objectively looked at audio features; this demonstrates that human feeling and perception of music is a difficult thing to model.


In conclusion, the algorithm clusters songs well to a certrain extent. Some clusters could still be split in two, but they were grouped correctly. Additionally, some outliers were found. Even though we would not put these into a cluster together ourselves, the audio features on which the classification was based could be derived from listening to the songs, but the feeling anyone listening to the song gets could in some cases not be detected by the algorithm.