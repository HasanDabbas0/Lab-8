import os
import time

import cv2


def first(pic='images/variant-10.jpg'):
    img = cv2.imread(pic)
    w, h = img.shape[:2]
    center_w, center_h = w // 2, h // 2
    image_cropped = img[center_w - 200:center_w + 200, center_h - 200:center_h + 200]
    cv2.imshow('New image', image_cropped)
    cv2.imwrite("cat_face.jpg", image_cropped)


def second_third():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.line(frame, (x + w // 2, y), (x + w // 2, y + h), (35, 142, 107), 2)
            cv2.line(frame, (x, y + h // 2), (x + w, y + h // 2), (35, 142, 107), 2)
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(a, b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1
    cap.release()


def extra():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    img_fly = cv2.imread('fly64.png')
    w_fly, h_fly = img_fly.shape[:2]
    i = 0
    counter = 0
    type_pic = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            try:
                frame[(y + h // 2 - h_fly // 2):(y + h // 2 + h_fly // 2),
                (x + w // 2 - w_fly // 2):(x + w // 2 + w_fly // 2)] = img_fly
                counter = 0
            except ValueError:
                counter += 1
                print('Ну удалось поместить изображение')
                if counter == 10:
                    print("Увы, необходимый объект так и не был распознан")
                    exit()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1
    cap.release()


if __name__ == '__main__':
    first('images/variant-8.jpg')
    second_third()
    # extra()

cv2.waitKey(0)
cv2.destroyAllWindows()
