import face_recognition 
import cv2
import numpy as np


video_capture = cv2.VideoCapture(0)

while True :
    
    ret , frame = video_capture.read()

    if ret :
        cv2.imshow("face detection",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    


# # for known image
# known_image_path = "image/modi.jpg"
# known_image = face_recognition.load_image_file(known_image_path)

# known_image_location = face_recognition.face_locations(known_image)
# known_image_encode = face_recognition.face_encodings(known_image)


# # for unknown image
# image_path = "image/modim.png"
# u_image = face_recognition.load_image_file(image_path)
# u_image_location = face_recognition.face_locations(u_image)
# u_image_encode = face_recognition.face_encodings(u_image)



# if len(known_image_encode)>0 and len(u_image_encode)>0:

#     known_encode = known_image_encode[0]
#     unknown_encode = u_image_encode[0]

#     result = face_recognition.compare_faces([known_encode],unknown_encode,0.6)

#     if result[0]:
#         print("data matched")
    
#     else:
#         print("data not matched")

# else:
#     print("No face found in one or both face")