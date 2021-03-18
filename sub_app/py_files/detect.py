import base64
from io import BytesIO

import cv2

import numpy as np
from PIL import Image

# FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SHAPE_PREDICTOR_FILE = os.path.join(FILE_DIR, 'files/shape_predictor_68_face_landmarks.dat')
# predictor = dlib.shape_predictor(SHAPE_PREDICTOR_FILE)



def base64_decode(data):
    # with open('sample.png', 'wb') as f:
    #     f.write(base64.decodestring(data.split(',')[1].encode()))
    out=base64.decodestring(data.split(',')[1].encode())
    return out
     


def base64_encode(data):
    if data:
        return 'data:image/png;base64,' + data


def get_face_detect_data(data):
    nparr = np.fromstring(base64_decode(data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image_data = detectImage(img)
    # print('image_data',image_data)

    return base64_encode(image_data)


def detectImage(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    print('number of faces',len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    output = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # print(output.shape)
    # im = Image.fromarray(output)
    # im.save('test.png')


    buffer = BytesIO()
    img = Image.fromarray(output)
    img.save(buffer, format="png")
    encoded_string = base64.b64encode(buffer.getvalue()).decode('ascii')
    return encoded_string