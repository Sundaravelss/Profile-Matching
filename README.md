# Profile-Matching
Finding Matching Profiles of Facebook and Twitter

To find matching profiles of the same person in two different social media say Facebook and Twitter , three approaches are utilised

1.Face Matching
-------------
    The pretrained face recognition model called Facenet is utilised for matching the faces in the images posted in the social media. 
2.Name and User Description Matching
-------------
    Fuzzy name matching is utilized to match the names and user description.
3.Network Matching
-------------
    The number of similar friends in both social medas is compared to identify the network match.

Each matching score is normalized and consolidated with the weighted average to arrive at the final match score.
