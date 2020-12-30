# Development Plan

#### Project objectives, context, prioritized requirements and constraints

Our goal is to create a tool that indicates how connected and similar popular songs in the daily and/or weekly spotify charts are. For this, a clustering algorithm will be used, which will be specified in the next section.
We have defined a prioritized list of the requirements of our tool:

Must have:
* Include at least 50 of the most popular songs from [the spotify 200 chart](https://spotifycharts.com/regional) . 
* Generate clusters of similar songs using a clustering algorithm and give a list of the songs in each cluster as output.

Should have:
* Let a user select what region they want to look up the chart for, whether they want to see the weekly or daily chart and what date’s chart he or she wants to use.  
* Automatically generate a graph showing the connectedness of the songs selected from the chart. 

Could have:
* Let a user select two songs from the chart and return a value for how connected the two chosen songs are. 
* Gather user input to enhance the functioning of the clustering algorithm. 

Won’t have:
* Generate a playlist based on a song the user can select, that includes the songs that are most similar to the chosen song. 

#### Project approach, resources, results optimizations

During the project we will use some principles of the Scrum method to evaluate and plan our progress. Every week we will do a small sprint planning to clarify who is going to work on which part. 
We are going to use an online Kanban board to help us with this. Every week, we want to at least attend the Tuesday and Thursday lab sessions and if possible work the rest of the Thursday on the project as well. Besides these hours, we also expect to work a few hours at home by ourselves every week. 
Although we are using Scrum principles, we clearly want to define our plans and strategies before we start implementing, so we prevent making unnecessary mistakes. 



#### Design objectives, design strategy, critical features, risk factors, ‘to-avoids’

We want to find the connectedness of songs based on audio features available on spotify by determining the difference between characteristic values and calculating the distance between songs. 
We are going to use web scraping to collect the name, artist and song id for all of the songs in the chart and then use the spotipy module to access their audio features.
The features we are going to use, are:

'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'valence' and 'tempo'. (https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

'Liveness' is another feature available on spotify, but we decided not to use it as it is an indication of the probability a song was recorded with an audience present. We do not expect a lot of songs in the chart to be recorded live, so we do not regard it as a distinguishing feature. 

We are going to generate clusters by using the k-means algorithm and determining the euclidean distance between the songs based on the values of the audio features. We then display lists of songs categorized by the clusters.

If we have time left after implementing this, we would also like to create a minimum spanning tree using the euclidean distances as edge weights and applying the Kruskal algorithm, to visualize the connectedness and see whether songs in the same cluster are close to eachother on the graph. 

Factors that can cause a risk for our project are:
* Our tool strongly depends on the song characteristics from spotify, so a risk is that we cannot get access to the spotify library.
* We think getting familiar with machine learning and getting our k-means neighbor algorithm to work can be difficult, so we face a risk in spending a lot of time on this.
* We think a difficult part of the optional implementation of the minimum spanning tree will be determining positions of nodes in the graph. The positions of the different song nodes should depend on the connectedness between the songs, so the graph will be user friendly and can be read intuitively.


#### Design documentation set layout, managed

Before we start planning our implementation, we are first going to record some high level decisions. We are going to create a class diagram to clarify what classes are responsible for which functions and how the different classes relate to one another. 
We think this will help us to achieve high modularity in order to make our code more testable and easier to extend in the future. We are also going to make an activity diagram to visualize the flow of our application. 


#### Design validation, managed

We are going to use our requirements during the design phase to make sure our tool includes all of the features that we want to be in there. 
When our design plan is complete we will discuss it again and go over it together to make sure it is the best strategy for our project.


#### Implementation planning, managed

We are going to make use of GitLab to work on code together and keep track of the changes.
We want to work in different files to separate different features and make our code more manageable, which we will specify in our Design plan. 


#### Testing approach, test planning, validation reporting

We want to do Continuous Testing to make sure during every stage of the project that our tool works accordingly and to prevent not having enough time for testing in the end.
This means we will start writing tests from the start. We are going to make use of unit tests to cover our different functions and do regression testing when any changes are made.  

To verify whether our analysis was successful, we will be doing manual testing. We want to listen to the songs that have been found connected through our programme to give feedback to the systems’ clustering. As songs might be found connected even though they sound nothing alike, manual testing is crucial in our case. As an extra feature, we would want to implement a user input function so that more users could give feedback to the system to make it more accurate in its categorisation.

In the end, a coverage report will be delivered to clarify what parts of our code were examined through manual and automatic testing. During our presentation we will include audio fragments to show our results. 



#### Evaluation

We are going to use some principles of the Scrum method to evaluate our progress and plan what will be done each week.





