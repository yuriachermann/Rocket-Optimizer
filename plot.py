import numpy as np
import sys
import os
import matplotlib as m
import matplotlib.pyplot as plt


def eggholder2(a, b):
    term1 = -(b+47) * np.sin(np.sqrt(abs(b+a/2+47)))
    term2 = -a * np.sin(np.sqrt(abs(a-(b+47))))
    return term1 + term2


def delete_images():
    folder = 'images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return


def plot_all(pos_n, n):
    ax = plt.figure().add_subplot(projection='3d')

    ax.scatter(pos_n[0], pos_n[1], pos_n[2])
    pnt3d = ax.scatter(pos_n[0], pos_n[1], pos_n[2], c=pos_n[2])

    ax.azim = 120  # isomeric=120 | superior=0
    ax.dist = 10  # standard=10
    ax.elev = 30  # isomeric=30 | superior=90
    ax.set_xlim3d(-0.01, 0.05)
    ax.set_ylim3d(-0.01, 0.1)
    ax.set_zlim3d(1400, 1600)

    plt.savefig('images/iteration_%d' % n)
    return


