import meshcat
import meshcat.geometry as g
from meshcat.transformations import (
    rotation_matrix as rm, 
    translation_matrix as tm,
)

class Visualizer:
    """ ... """
    
    def __init__(self):
        vis = meshcat.Visualizer() # zmq_url="tcp://127.0.0.1:6000")

        body = vis["robot"]
        body.set_object(g.Box([0.15, 0.35, 0.4]))
        body["arm_l"].set_object(g.Box([0.1, 0.1, 0.3]))
        body["arm_r"].set_object(g.Box([0.1, 0.1, 0.3]))
        body["arm_l"].set_transform(tm([0, .25, 0]))
        body["arm_r"].set_transform(tm([0, -.25, 0]))

        body["neck"].set_transform(tm([0, 0, 0.32]))
        head = body["neck/head"]
        head.set_object(g.Box([0.18, 0.15, 0.2]))

        self.head = head
        self.body = body

    def set_pos(self, pos):
        self.body.set_transform(tm([0, *pos]))

    def look_towards(self, yaw, pitch, roll):
        self.head.set_transform(
                rm(roll,  [1, 0, 0])
              @ rm(pitch, [0, 1, 0])
              @ rm(yaw,   [0, 0, 1])
                )
