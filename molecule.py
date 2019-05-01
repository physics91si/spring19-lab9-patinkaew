import numpy as np
from particle import Particle

class Molecule:
    def __init__(self, pos1, pos2, mass1, mass2, k, L0):
        self.p1 = Particle(pos1, mass1)
        self.p2 = Particle(pos2, mass2)
        self.k = k
        self.L0 = L0

    def get_displ(self):
        '''return displacement vector between two particles'''
        return np.array(self.p2.pos) - np.array(self.p1.pos)

    def get_force(self):
        '''return force on one particle'''
        dis = self.get_displ()
        force = self.k * (self.L0 - np.linalg.norm(dis))
        angle= np.arctan(dis[1] / dis[0])
        return np.array([force * np.cos(angle), force * np.sin(angle)])
