import face_recognition
import cv2
image = face_recognition.load_image_file("face_detect_demo.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)


cv2.rectangle(image, (face_locations[0][1], face_locations[0][0]), (face_locations[0][3], face_locations[0][2]), (0,123,234), 2)
cv2.rectangle(image, (face_locations[1][1], face_locations[1][0]), (face_locations[1][3], face_locations[1][2]), (0,123,234), 2)
cv2.imshow('face_detect_demo',image)
cv2.imwrite('detected_faces.png',image)
cv2.waitKey(0)