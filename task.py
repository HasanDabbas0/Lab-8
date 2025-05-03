import cv2
import time

# Загрузка и обрезка изображения
image_path = r'C:\Users\Hasan-Dabbas\Downloads\variant-8.jpg'
img = cv2.imread(image_path)

if img is None:
    print("Ошибка: изображение не найдено.")
else:
    h, w = img.shape[:2]
    center_h, center_w = h // 2, w // 2
    cropped = img[center_h - 200:center_h + 200, center_w - 200:center_w + 200]
    cv2.imshow("Обрезанное изображение", cropped)
    cv2.imwrite("cat_face.jpg", cropped)

# Работа с веб-камерой
cap = cv2.VideoCapture(0)
frame_size = (640, 480)
i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, frame_size)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.line(frame, (x + w // 2, y), (x + w // 2, y + h), (0, 255, 0), 2)
        cv2.line(frame, (x, y + h // 2), (x + w, y + h // 2), (0, 255, 0), 2)

        if i % 5 == 0:
            print(x + w // 2, y + h // 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)
    i += 1

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
