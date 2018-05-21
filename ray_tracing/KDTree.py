from ray_tracing.KDNode import KDNode
import numpy


class KDTree:
    def __init__(self, box_triangles, depth):
        self.node = KDNode(None, None, numpy.asarray(), box_triangles)

    def build(self):
        if self.node.box_triangles == 0:
            return self.node
