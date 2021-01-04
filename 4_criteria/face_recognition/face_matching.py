import face_recognition
import os
import cv2


KNOWN_FACES_DIR= '/vagrant/face_recognition/twitter/friends'
DIR_TO_MATCH = '/vagrant/face_recognition/facebook/friends/prasanth.anbalagan.9'
TOLERANCE = 0.6
MODEL = 'cnn'   


# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

print('Loading known faces...')
known_faces = []
known_profile = []


#for name in os.listdir(KNOWN_FACES_DIR):
name='prasanth'
for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

    # Load an image
    image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

    # Get 128-dimension face encoding
    # Always returns a list of found faces, for this purpose we take first face only 
    if face_recognition.face_encodings(image):
        encoding = face_recognition.face_encodings(image)[0]

        # Append encodings and name
        known_faces.append(encoding)
        print(known_faces)
        known_profile.append(name)
        print(known_profile)


print('Searching the directory to match profile...')
#loop over the faces in the directory to match the known profile
for filename in os.listdir(DIR_TO_MATCH):

    # Load image
    print(f'Filename {filename}', end='')
    image = face_recognition.load_image_file(f'{DIR_TO_MATCH}/{filename}')

    # face locations to draw boxes
    locations = face_recognition.face_locations(image, model=MODEL)

    # get face encodings of all faces in the image
    encodings = face_recognition.face_encodings(image, locations)

    #RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # number of faces found in the image
    print(f', found {len(encodings)} face(s)')
    for face_encoding, face_location in zip(encodings, locations):

        # We use compare_faces (but might use face_distance as well)
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        print(results)
        # Since order is being preserved, we check if any face was found then grab index
        # then label (name) of first matching known face withing a tolerance
        match = None
        if all(results):  # If at least one is true, get a name of first of found labels
            match = known_profile[results.index(True)]
            print(f' - {match} from {results}')

            # Each location contains positions in order: top, right, bottom, left
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            # Get color by name using our fancy function
            color = name_to_color(match)

            # draw frame with thickness 3
            cv2.rectangle(image, top_left, bottom_right, color, 3)

            # Now we need smaller, filled grame below for a name
            # This time we use bottom in both corners - to start from bottom and move 50 pixels down
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)

            # Paint frame
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

            # label the name with thickness 2
            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 2)
            
            if not os.path.exists(f'{DIR_TO_MATCH}/{match}'):
                    os.mkdir(f'{DIR_TO_MATCH}/{match}')
            cv2.imwrite(f'{DIR_TO_MATCH}/{match}/{face_location}.png',image)
    # Show image
    #cv2.imshow(filename, image)
    #cv2.waitKey(0)
    #cv2.destroyWindow(filename)