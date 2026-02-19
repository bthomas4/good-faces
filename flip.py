# Flip the script
# Input: file of face characters
# Output: File of 'flipped' faces

# Import file
# Create list of faces
# Apply flip function to each face
    # Iterate through lines, flipping each and adding to result
# (Write to file) result

# Algorithmically
# Linked list, then reverse, but keep in place paranthesis
# Or construct reverse string in place

from os import read


def flip_file(filepath: str):

    fileStr = open(filepath).read()
    faces = fileStr.splitlines()

    flippedFaces = [flip_face(face) for face in faces]

    combinedFaces = combine_faces(faces, flippedFaces)

    return 


def flip_face(face: str):

    face_list = list(face)
    # print(face_list)
    face_list_rev = face_list[::-1]
    print("".join(face_list), "", ("".join(face_list_rev)))
    # add () flips
    return

def combine_faces(faces, flippedFaces):
    max_len = len(max(faces))
    pad_len = 5
    return [faces + ""*(max_len-len(face)+pad_len) + "|" + ""*pad_len + flip for face, flip in (faces, flippedFaces)]


if __name__ == "main":
    print(0)

    # Command line ask for file name
    filepath = "faces.txt"
    flip_file(filepath)

    