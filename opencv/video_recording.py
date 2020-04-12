import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

video_file = 'video.avi'
frames_per_second = 24.0
video_res = '720p'

# standard video dimension sizes
STD_DIMENSION = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# set resolution
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSION['480p']
    if res in STD_DIMENSION:
        width, height = STD_DIMENSION[res]
    change_res(cap, width, height)
    return width, height


cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=video_res)
out = cv2.VideoWriter(video_file, cv2.VideoWriter.fourcc(*'XVID'), frames_per_second, dims)

while True:

    # capture frame-by-frame
    ret, frame = cap.read()
    out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        # roi_gray = gray[y:y + h, x:x + w]
        # roi_color = frame[y:y + h, x:x + w]

        color = (255, 0, 0)  # in BGR
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
