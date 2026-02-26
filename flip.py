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

import os


def flip_file(filepath: str):

    fileStr = open(filepath).read()
    faces = fileStr.splitlines()

    flippedFaces = [flip_face(face) for face in faces]

    # combinedFaces = combine_faces(faces, flippedFaces)

    return flippedFaces


def flip_face(face: str):

    faceList = list(face)
    parenFliplist = list(map(flip_paren, faceList))
    # print(face_list)
    faceListRev = parenFliplist[::-1]
    # finalFaceList = [i if (i == '(' or i == ')') else j for i, j in zip(faceList, faceListRev)]
    # print("".join(faceList), "", "".join(faceListRev))
    flipFace ="".join(faceListRev)
    # add () flips
    return flipFace

def flip_paren(char: str):
    if char == '(':
        return ')'
    elif char == ')':
        return '('
    else:
        return char
    

def combine_faces(faces, flippedFaces):
    max_len = len(max(faces))
    pad_len = 10
    print(max_len)
    return [face + str(len(face))+" "*(max_len-len(face)+pad_len) + "|" + " "*pad_len + flip for face, flip in zip(faces, flippedFaces)]


if __name__ == "__main__":
    print(0)

    # Command line ask for file name
    filepath = "faces.txt"
    flippedFile = flip_file(filepath)

    print("\n".join(flippedFile))
    with open('output.txt', 'w') as file:
        file.write("\n".join(flippedFile))
    

    