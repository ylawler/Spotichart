# import Project.UserInterface as ui
# import Project.WebScrapeCharts as wsc
# import Project.AudioFeatures as af
# import Project.DistanceSongs as ds
# import Project.MinSpanTree as mst
# import Project.Visualize as vis
# import Project.KMeans as km

import UserInterface as ui
import WebScrapeCharts as wsc
import AudioFeatures as af
import DistanceSongs as ds
import MinSpanTree as mst
import Visualize as vis
import Project.KMeans as km

import time
testing = False

# -------------------------------- FUNCTIONS FOR GETTING DATA FROM FILES ----------------------------------------------
def check_file(filename):
    print(f'\nchecking file:\t{filename}')

    try:
        with open(filename,'r') as rf:
            lines = rf.readlines()
            counter = len(lines)
            print(f'contains data:\t{counter == 200}')
            return counter == 200
    except:
        print(f'*** No such File exists -> Creating File {filename} ***')
        return False

def get_ids(cc,rc):
    filename = f'test_{cc}_{rc}.txt'

    if check_file(filename):
        # Ids exist in file
        print(f'load from file:\t{filename}\n')
        webscrape.load_ids_from_file(cc, rc)
    else:
        # ids don't exist yet, save them
        print('no ids in file, need to webscrape for ids')
        print(f'saving ids for future testing!\n')
        webscrape.save_for_testing(cc, rc)

    return webscrape.song_ids_array

def get_features(cc,rc, song_ids):
    filename_feat = f'test_{cc}_{rc}_feat.txt'
    # check if features exist
    if check_file(filename_feat):
        # features exist, load them
        print(f'load from file:\t{filename_feat}\n')
        audio.load_features(filename_feat)
    else:
        # Features doesnt exist, save them
        print('no features in file, need to access spotify for features')
        print(f'saving features for future testing!\n')
        audio.save_features(filename_feat, song_ids)
    return audio.features

# ----------------------------------------------- RUN MAIN ------------------------------------------------------------
if __name__ == '__main__':
    # get the start time
    start = time.time()

    # Define the Classes to be used
    user = ui.UserInterface()
    webscrape = wsc.WebScrapeCharts()
    audio = af.AudioFeatures()
    distances = ds.DistanceSongs()


    # If testing is True, load ids and features from saved files to speed up time -> (reduces from 40s to about 1.3s)
    if testing:
        # possible to change the country code (cc) and recurrence (rc), will create new files for given inputs.
        cc = 'nl'
        rc = 'daily'
        # Get the ids and features. It checks if the files contain values. If yes, it loads the files, if not it webscrapes
        # and gets the audio features and then saves them for faster running next time
        song_ids = get_ids(cc,rc)
        song_features = get_features(cc,rc,song_ids)

        # Set the webscrape song id array and audio features
        webscrape.song_ids_array = song_ids
        audio.features = song_features

    else:
        # Get the user input and find the ids and features from that
        page_found = False

        while not page_found:
            user.get_user_input()
            if webscrape.get_charts(user.country_code, user.recurrence):
                page_found = True
            else:
                print('Collecting Chart from spotifycharts.com')
                webscrape.set_default()
                print('Charts dont exist for given country\nPlease enter a different country!')

        print('Retrieving Audio Features')
        audio.get_features(webscrape.song_ids_array)



    # Calculate distances and min spanning tree
    print('Calculating Song Similarity')
    distances.find_distances(audio.features)

    print('Computing Minimum Spanning Tree')
    minspantree = mst.MinSpanTree()
    minspantree.create_min_span_tree(distances.adj_dict)
    #print(minspantree.MST_graph.edges())

    print('Computing Clusters')
    kmeans = km.Kmeans()
    kmeans.k_means(audio.features)

    print('Visualizing')
    vis.Visualize(kmeans.clusters, minspantree.MST_graph, kmeans.scaled)

    # get the end time
    end = time.time()
    print(f'\n...finished running in {round(end - start, 3)} seconds')
