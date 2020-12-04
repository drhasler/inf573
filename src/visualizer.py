import meshcat
import meshcat.geometry as g
import meshcat.transformations as tf

class Visualizer:
    """ ... """
    
    def __init__(self):
        vis = meshcat.Visualizer(zmq_url="tcp://127.0.0.1:6000")

        vis["robot"].set_object(g.Box([0.15, 0.35, 0.4]))
        vis["robot"]["head"].set_object(g.Box([0.2, 0.2, 0.2]))
        vis["robot"]["arm_l"].set_object(g.Box([0.1, 0.1, 0.3]))
        vis["robot"]["arm_r"].set_object(g.Box([0.1, 0.1, 0.3]))

        vis["robot"]["head"].set_transform(tf.translation_matrix([0, 0, 0.32]))
        vis["robot"]["arm_l"].set_transform(tf.translation_matrix([0, .25, 0]))
        vis["robot"]["arm_r"].set_transform(tf.translation_matrix([0, -.25, 0]))

    def set_pos(self, pos):
        ...
