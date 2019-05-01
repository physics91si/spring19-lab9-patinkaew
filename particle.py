# Physics 91SI
# Spring 2019
# Lab 9

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""

    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))
