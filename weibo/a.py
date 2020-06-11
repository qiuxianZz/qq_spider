from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
def is_face(jpg):
    image = face_recognition.load_image_file("./"+jpg)
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)
    if face_locations != []:
        return ("true")
    else:
        return("false")
# print("I found {} face(s) in this photograph.".format(len(face_locations)))
#
# for face_location in face_locations:
#
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#
#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     print(pil_image)
#     pil_image.show()

def test(n):
    for i in range(n):
        yield i

f1 =test(4)
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
# print('f1:', f1.next())