import os
import gc
import random
import shutil
import tempfile
import orhelper
import numpy as np
# from memory_profiler import profile
import xml.etree.ElementTree as Et
from statistics import mean, stdev
from orhelper import FlightDataType, FlightEvent
# from plot import plot_all, delete_images, make_gif, create_folder


# --- PARTICLES
class Particle:
    def __init__(self, bounds):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.fit_best_i = -1  # best fitness individual
        self.fit_i = -1  # fitness individual

        vel = 0.1

        for i in range(len(bounds)):
            self.velocity_i.append(random.uniform(-vel, vel))
            self.position_i.append(random.random() * (bounds[i][1]-bounds[i][0]) + bounds[i][0])

    # evaluate current fitness
    def evaluate(self, fit_func):
        self.fit_i = fit_func(self.position_i)

        # check to see if the current position is an individual best
        if self.fit_i < self.fit_best_i or self.fit_best_i == -1:
            self.pos_best_i = self.position_i
            self.fit_best_i = self.fit_i

    # update new particle velocity
    def update_velocity(self, pos_best_g, bounds, t, t_max, ii):
        wt_min = 0.01  # constant inertia weight
        wt_max = 0.9  # constant inertia weight
        c1_i = 0.8  # absolute cognitive weight
        c1_f = 0.2  # absolute cognitive weight
        c2_i = 0.2  # absolute social weight
        c2_f = 6  # absolute social weight

        wt_var = wt_min + (wt_max - wt_min) * (t_max - t) / t_max  # constant inertia weight
        c1_var = (c1_f - c1_i) * t / t_max + c1_i  # varying cognitive constant
        c2_var = (c2_f - c2_i) * t / t_max + c2_i  # varying social constant

        # vel_max = 1

        print((round(c1_var, 1), round(c2_var, 1)) if ii == 1 else '', end='')

        for i in range(0, len(bounds)):
            r1 = random.random()*2-1  # -1 a 1 ?
            r2 = random.random()*2-1  # -1 a 1 ?

            vel_cognitive = c1_var * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2_var * r2 * (pos_best_g[i] - self.position_i[i])

            vel_i = 0.2 * (wt_var * self.velocity_i[i] + vel_cognitive + vel_social)

            self.velocity_i[i] = vel_i

            # if -vel_max < vel < vel_max:
            #     self.velocity_i[i] = vel
            # elif vel > vel_max:
            #     self.velocity_i[i] = vel_max
            # else:
            #     self.velocity_i[i] = -vel_max

    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        for i in range(0, len(bounds)):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]
                # self.velocity_i[i] = -self.velocity_i[i]

            # adjust minimum position if necessary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]
                # self.velocity_i[i] = -self.velocity_i[i]


# --- PSO
class PSO:
    def __init__(self, fit_func, bounds, num_particles, max_iter):
        fit_best_g = -1  # best fitness for group
        pos_best_g = []  # best position for group
        dimensions = len(bounds)

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(bounds))

        # create_folder()
        # delete_images()

        # begin optimization loop
        n = 0
        stdv = 1
        while n <= max_iter and stdv > 0.01:

            fit_all = []
            fit_best_n = 0

            # var = np.zeros((dimensions+1, num_particles))

            # cycle through particles in swarm and evaluate fitness
            for i in range(0, num_particles):
                swarm[i].evaluate(fit_func)
                fit_all.append(swarm[i].fit_i)
                # for dim in range(0, dimensions):
                #     var[dim, i] = swarm[i].position_i[dim]
                # var[dimensions, i] = swarm[i].fit_i

                # determine the best of iteration
                if swarm[i].fit_i > fit_best_n:
                    fit_best_n = swarm[i].fit_i
                    # determine if current particle is the best (globally)
                    if fit_best_n > fit_best_g or fit_best_g == -1:
                        pos_best_g = list(swarm[i].position_i)
                        fit_best_g = float(swarm[i].fit_i)

            # cycle through swarm and update velocities and position
            for i in range(0, num_particles):
                swarm[i].update_velocity(pos_best_g, bounds, n, max_iter, i)
                swarm[i].update_position(bounds)

            # mean_pos = [mean(var[dim]) for dim in range(0, dimensions)]
            # stdev_pos = [stdev(var[dim]) for dim in range(0, dimensions)]
            # stdv = sum(stdev_pos)

            # var_plot = [var[0], var[1], var[dimensions]]
            # plot_all(var_plot, n)

            print(" \t\tn:", n,
                  " \t\tavg:", round(mean(fit_all), 1),
                  " \t\tstd:", round(stdev(fit_all), 1),
                  " \t\tbest_g:", round(fit_best_g, 1),
                  " \t\tbest_i:", round(fit_best_n, 1),
                  " \t\t-" if fit_best_n + 0.1 < fit_best_g else "")

            del fit_all, fit_best_n  # , var, var_plot, stdev_pos
            n += 1

        # make_gif(n-1)

        # print final results
        print('\n\nFINAL:')
        print("best position:", [round(num, 2) for num in pos_best_g])
        print("Best fitness:", round(fit_best_g, 2))
        set_fin(pos_best_g[0], pos_best_g[1], pos_best_g[2], pos_best_g[3])


class TEMP(object):

    def __init__(self, original_path):
        self.original_path = original_path

    def __enter__(self):
        temp_dir = tempfile.gettempdir()
        base_path = os.path.basename(self.original_path)
        self.path = os.path.join(temp_dir, base_path)
        shutil.copy2(self.original_path, self.path)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)


# --- EXECUTE
if __name__ == "__main__":
    with orhelper.OpenRocketInstance() as instance, TEMP("teste.ork") as temp_path:
        orh = orhelper.Helper(instance)
        doc = orh.load_doc(temp_path)

        def set_fin(x2, y2, x3, y3):
            tree = Et.parse(temp_path)
            root = tree.getroot()
            fin = root.find('.//finpoints')
            points = fin.findall('.//point')
            point2 = points[1]
            point2.attrib['x'] = str(x2)
            point2.attrib['y'] = str(y2)
            point3 = points[2]
            point3.attrib['x'] = str(x3)
            point3.attrib['y'] = str(y3)
            tree.write(temp_path, encoding='UTF-8', xml_declaration=True)
            del tree, root, fin, points

        # --- FITNESS FUNCTION
        def run_sim(fin):
            set_fin(fin[0], fin[1], fin[2], fin[3])
            # doc = orh.load_doc(temp_path)
            # del doc
            # del doc, sim, dt, events, apg
            gc.collect()
            # return 1500
            sim = doc.getSimulation(0)
            orh.run_simulation(sim)
            dt = orh.get_timeseries(sim, [FlightDataType.TYPE_TIME, FlightDataType.TYPE_ALTITUDE, FlightDataType.TYPE_VELOCITY_Z])
            events = orh.get_events(sim)
            apg = np.interp(events.get(FlightEvent.APOGEE),
                            dt[FlightDataType.TYPE_TIME],
                            dt[FlightDataType.TYPE_ALTITUDE])
            apogee = apg[0]
            return apogee


        random.seed(17201577)
        domains = [(0, 0.06), (0, 0.1), (0.06, 0.12), (0, 0.1)]  # input bounds [(x1_min,x1_max), ...]
        PSO(fit_func=run_sim, bounds=domains, num_particles=20, max_iter=5)

        shutil.copy2(temp_path, "teste.ork")

# TODO: usar profiler
# TODO: encontrar ponto que infla a memória
# TODO: verificar queda abrupta do desvio-padrão
# TODO: computação paralela
