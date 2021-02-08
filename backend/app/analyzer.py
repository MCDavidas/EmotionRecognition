import asyncio
import logging
import tensorflow as tf
import cv2
import numpy as np
import os
from PIL import Image


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

EMOTION_DICT = {0: "Angry", 1: "Disgust", 2: "Fear",
                3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}

MODEL = tf.keras.models.load_model(os.path.join(DATA_PATH, 'model.h5'))

logging.warning(f'Devices available: ' \
                f'{tf.config.experimental.list_physical_devices()}')


async def analyze_image(img):
    logging.info('Starting image analyse')

    image_ndarray = np.asarray(img)

    try:
        gray = cv2.cvtColor(image_ndarray, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        logging.error('OpenCV error')
        return img, None

    logging.debug(str(type(image_ndarray)))

    face_cascade = cv2.CascadeClassifier(
                   os.path.join(DATA_PATH,
                                'haarcascade_frontface_default.xml'))

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    logging.debug('faces count: ' + str(len(faces)))

    emotion = 'None'
    for (x, y, w, h) in faces:
        cv2.rectangle(image_ndarray, (x, y), (x + w, y + h), (0, 255, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(
            np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)

        cv2.normalize(cropped_img,
                      cropped_img,
                      alpha=0,
                      beta=1,
                      norm_type=cv2.NORM_L2,
                      dtype=cv2.CV_32F)

        prediction = MODEL.predict(cropped_img)
        emotion = EMOTION_DICT[int(np.argmax(prediction))]

        logging.info('Prediction is ' + emotion)

        cv2.putText(image_ndarray,
                    emotion,
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA)

    answer_img = Image.fromarray(image_ndarray)
    answer_img.format = img.format

    return answer_img, emotion


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    result_img = asyncio.run(analyze_image(Image.open('images/test.jpg')))
    logging.info('Saving image')
    result_img.save('images/result.jpg')
    logging.info('Done')
