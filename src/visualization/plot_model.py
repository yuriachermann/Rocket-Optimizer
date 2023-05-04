import os
import shutil

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def eggholder2(a, b):
    term1 = -(b+47) * np.sin(np.sqrt(abs(b+a/2+47)))
    term2 = -a * np.sin(np.sqrt(abs(a-(b+47))))
    return term1 + term2


def delete_images():
    folder = '../../data/images_model'
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

    # x = np.linspace(-512, 512, 30)
    # y = np.linspace(-512, 512, 30)
    # x, y = np.meshgrid(x, y)
    # z = eggholder2(x, y)
    # ax.contour3D(x, y, z, 200)

    ax.azim = 120  # isomeric=120 | superior=0
    ax.dist = 10  # standard=10
    ax.elev = 30  # isomeric=30 | superior=90
    ax.set_xlim3d(-512, 512)
    ax.set_ylim3d(-512, 512)
    ax.set_zlim3d(-1000, 1500)

    plt.savefig('../../data/images_model/iteration_%d' % n)
    return


def make_gif(n):
    frames = []
    for i in range(n):
        frames.append(Image.open("../../data/images_model/iteration_%s.png" % i))

    frame_one = frames[0]
    frame_one.save("../../report/trial_model/pso.gif", format="GIF", append_images=frames, save_all=True, duration=100, loop=0)

    return
