import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# For webcam input:
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def process(image):
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return [image], results

G = None
def details(ims, res):
    global G
    pl = res.pose_landmarks.landmark
    PL = mp_pose.PoseLandmark
    G = PL # for debugging
    print(pl[PL.NOSE], pl[PL.LEFT_EAR], pl[PL.RIGHT_EAR])
    # Z seems pretty bad, can we work only with x,y ?

if __name__ == "__main__":
    from loop import webcam
    webcam(process, {'d': details})
    pose.close()