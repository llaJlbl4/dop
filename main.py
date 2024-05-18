import face_recognition
import cv2
import os

# Путь к папке с изображениями известных лиц
known_faces_dir = 'faces'

# Загрузка изображений известных лиц и кодирование их признаков
known_face_encodings = []
known_face_names = []
for filename in os.listdir(known_faces_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])

# Включение веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Чтение кадра с веб-камеры
    ret, frame = cap.read()

    # Нахождение лиц на кадре
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Сравнение каждого найденного лица с известными лицами
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Если найдено совпадение, берется имя первого совпадения
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Отрисовка рамки вокруг лица и отображение имени
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Отображение кадра с распознанными лицами
    cv2.imshow('Face Recognition', frame)

    # Выход из цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()