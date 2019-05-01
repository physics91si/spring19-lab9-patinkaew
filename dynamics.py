# Physics 91SI
# Spring 2019
# Lab 9

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle
from molecule import Molecule

# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""
    mol = Molecule(np.array([0.2,0.2]), np.array([0.8,0.8]), 1, 2, 1, 0.5)
    return mol


# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    mol.p1.acc = -mol.get_force()/mol.p1.m
    mol.p2.acc = mol.get_force()/mol.p2.m
    mol.p1.vel = mol.p1.vel + mol.p1.acc * dt
    mol.p2.vel = mol.p2.vel + mol.p2.acc * dt
    mol.p1.pos = mol.p1.pos + mol.p1.vel * dt
    mol.p2.pos = mol.p2.pos + mol.p2.vel * dt

#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
