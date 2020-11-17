# USAGE
# python detect_drowsiness.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python detect_drowsiness.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav

# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import VideoStream, FileVideoStream, FPS
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
from numpy_ringbuffer import RingBuffer


def sound_alarm(path):
    # play an alarm sound
    playsound.playsound(path)


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    a = dist.euclidean(eye[1], eye[5])
    b = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    c = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    return (a + b) / (2.0 * c)

def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it
    # to the format (x, y, w, h) as we would normally do
    # with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    # return a tuple of (x, y, w, h)
    return (x, y, w, h)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--shape-predictor", required=True,
                help="path to facial landmark predictor")
ap.add_argument("-a", "--alarm", type=str, default="",
                help="path alarm .WAV file")
ap.add_argument("-m", "--movie", type=str, default="",
                help="movie file")
ap.add_argument("-i", "--image", type=str, default="",
                help="image file")
ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
ap.add_argument("-l", "--log", type=str, default="",
                help="path to logfile")
args = vars(ap.parse_args())

# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold for to set off the
# alarm
EYE_AR_THRESH = 2
EYE_AR_CONSEC_FRAMES = 48

# initialize the frame counter as well as a boolean used to
# indicate if the alarm is going off
COUNTER = 0
ALARM_ON = False

earBuf = RingBuffer(capacity=120, dtype=np.float, allow_overwrite=True)


def calculate_score(value):
    if earBuf.is_full:
        std = np.std(earBuf)
        if std == 0:
            score = 0
        else:
            score = (value - np.mean(earBuf)) / std
    else:
        score = 0
    earBuf.append(value)
    return score


def nothing(x): return 0

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor


print("[INFO] loading facial landmark predictor...")

# hog + svm based face detector
face_detector = dlib.get_frontal_face_detector()


predictor = dlib.shape_predictor(args["shape_predictor"])

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

log_file = None
ear = 0
z_score = 0

cv2.namedWindow("Frame")
cv2.createTrackbar('Threshold', 'Frame', 0, 100, nothing)
cv2.setTrackbarPos('Threshold', 'Frame', EYE_AR_THRESH * 10)

# start the video stream thread
print("[INFO] starting video stream thread...")

MOVIE = 1
IMAGE = 2
WEBCAM = 3

imageSrc = 0
if args["movie"]:
    vs = FileVideoStream(args["movie"])
    imageSrc = MOVIE
elif args["image"]:
    vs = FileVideoStream(args["image"])
    imageSrc = IMAGE
else:
    vs = VideoStream(src=args["webcam"])
    imageSrc = WEBCAM
    time.sleep(1.0)

if args["log"]:
    log_file = open(args["log"], "w")

vs.start()
fps = FPS().start()
log_start = time.time()
frameID = -1
eventID = 0
frame = None
faces = []

# loop over frames from the video stream
while True:
    # grab the frame from the threaded video file stream, resize
    # it, and convert it to grayscale
    # channels)
    frameID += 1

    if imageSrc in [MOVIE,WEBCAM]:
        frame = vs.read()
        #if vs.stopped:
        #    break

    if imageSrc == IMAGE and frameID==0:
        frame = vs.read()

    log_time = time.time() - log_start
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    if frameID % 10 == 0:
        faces = face_detector(gray, 0)

    # loop over the face detections
    for rect in faces:

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the left and right eye coordinates, then use the
        # coordinates to compute the eye aspect ratio for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # compute the convex hull for the left and right eye, then
        # visualize each of the eyes
        # leftEyeHull = cv2.convexHull(leftEye)
        # rightEyeHull = cv2.convexHull(rightEye)
        # cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        # cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        z_score = calculate_score(ear)

        EYE_AR_THRESH = cv2.getTrackbarPos('Threshold', 'Frame') / 10

        #if z_score > 0 and abs(z_score) > EYE_AR_THRESH:
        #    cv2.imwrite(f'log/img-{frameID:d}-wide.jpg', frame)

        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        if z_score < 0 and abs(z_score) > EYE_AR_THRESH:
            if COUNTER == 0: eventID += 1
            COUNTER += 1

            cv2.imwrite(f'snapshots/img-{frameID:d}-closed.jpg', frame)

            # if the eyes were closed for a sufficient number of
            # then sound the alarm
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                # if the alarm is not on, turn it on
                if not ALARM_ON:
                    ALARM_ON = True

                    # check to see if an alarm file was supplied,
                    # and if so, start a thread to have the alarm
                    # sound played in the background
                    if args["alarm"] != "":
                        t = Thread(target=sound_alarm,
                                   args=(args["alarm"],))
                        t.deamon = True
                        t.start()

                # draw an alarm on the frame
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # otherwise, the eye aspect ratio is not below the blink
        # threshold, so reset the counter and alarm
        else:
            COUNTER = 0
            ALARM_ON = False

        # draw the computed eye aspect ratio on the frame to help
        # with debugging and setting the correct eye aspect ratio
        # thresholds and frame counters
        cv2.putText(frame, f"EAR: {np.mean(earBuf):.3f} {eventID:3d} {COUNTER:3d}",
                    (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    fps.update()

    # if the `q` or escape key was pressed, break from the loop
    if key in [ord("q"), 27]:
        break

    if log_file:
        log_file.write(f'{frameID:9d}, {log_time:12.3f}, {ear:.3f}, {z_score:6.3f}, {eventID:3d}, {COUNTER:3d}, {int(ALARM_ON):d}\n')

# do a bit of cleanup
cv2.destroyAllWindows()
fps.stop()
vs.stop()

print(f"Fps:{fps.fps():.2f} elapsed:{fps.elapsed():.2f}")

if log_file:
    log_file.close()
