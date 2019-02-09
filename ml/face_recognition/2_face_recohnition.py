import face_recognition
import cv2

known_image = face_recognition.load_image_file("Jay_Chou.jpeg")
unknown_image = face_recognition.load_image_file("test_face_recognition.jpeg")
# unknown_image = face_recognition.load_image_file("unknown.jpg")


Jay_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([Jay_encoding], unknown_encoding)
print(results)