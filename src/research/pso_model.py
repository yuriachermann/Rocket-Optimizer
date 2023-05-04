from __future__ import division
from statistics import mean, stdev
import numpy as np
import random
from src.visualization.plot_model import plot_all, delete_images, make_gif


# --- COST FUNCTION
#  we are attempting to optimize (minimize)
def eggholder(x):  # f(x*) = -959.6407, at x* = (512, 404.2319)
    a = x[0]
    b = x[1]
    return - (b+47) * np.sin(np.sqrt(abs(b+a/2+47))) - a * np.sin(np.sqrt(abs(a-(b+47))))


# --- MAIN
class Particle:
    def __init__(self, bounds):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        vel = 1

        for i in range(len(bounds)):
            self.velocity_i.append(random.uniform(-vel, vel))
            self.position_i.append(random.random() * (bounds[i][1]-bounds[i][0]) + bounds[i][0])

    # evaluate current fitness
    def evaluate(self, cost_func):
        self.err_i = cost_func(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g, bounds, n, max_iter, ii):
        w_i = 0.9  # constant inertia weight
        w_f = 0.01  # constant inertia weight
        c1_i = 0.8  # absolute cognitive weight
        c1_f = 0.2  # absolute cognitive weight
        c2_i = 0.1  # absolute social weight
        c2_f = 5  # absolute social weight

        w_var = w_f + (w_f - w_i) * n / max_iter + w_i  # constant inertia weight
        c1_var = (c1_f - c1_i) * n / max_iter + c1_i  # varying cognitive constant
        c2_var = (c2_f - c2_i) * n / max_iter + c2_i  # varying social constant

        vel_max = 1

        print((round(c1_var, 1), round(c2_var, 1)) if ii == 1 else '', end='')

        for i in range(0, len(bounds)):
            r1 = random.random()*2-1  # -1 a 1 ???????????
            r2 = random.random()*2-1  # -1 a 1 ???????????

            vel_cognitive = c1_var * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2_var * r2 * (pos_best_g[i] - self.position_i[i])

            vel = 0.2 * (w_var * self.velocity_i[i] + vel_cognitive + vel_social)

            self.velocity_i[i] = vel

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


class PSO:
    def __init__(self, cost_func, bounds, num_particles, max_iter):
        fit_best_g = -1  # best error for group
        pos_best_g = []  # best position for group

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(bounds))

        delete_images()

        # begin optimization loop
        n = 0
        stdv = 1
        while n < max_iter and stdv > 0.01:

            x = []
            y = []
            pos_n = []
            fit_all = []
            fit_best_n = 0

            # cycle through particles in swarm and evaluate fitness
            for i in range(0, num_particles):
                swarm[i].evaluate(cost_func)
                fit_all.append(swarm[i].err_i)
                x.append(swarm[i].position_i[0])
                y.append(swarm[i].position_i[1])
                pos_n.append([swarm[i].position_i[0], swarm[i].position_i[1], swarm[i].err_i])

                # determine if current particle is the best (globally)
                if swarm[i].err_i < fit_best_g or fit_best_g == -1:
                    pos_best_g = list(swarm[i].position_i)
                    fit_best_g = float(swarm[i].err_i)

                # determine the best of iteration
                if swarm[i].err_i < fit_best_n:
                    fit_best_n = swarm[i].err_i

            # cycle through swarm and update velocities and position
            for i in range(0, num_particles):
                swarm[i].update_velocity(pos_best_g, bounds, n, max_iter, i)
                swarm[i].update_position(bounds)

            mean_pos = [mean(x), mean(y)]
            stdev_pos = [stdev(x), stdev(y)]
            stdv = stdev_pos[0] + stdev_pos[1]

            pos_n = np.transpose(pos_n)

            plot_all(pos_n, n)

            print(n, " avg: ", round(mean(fit_all), 2), " std: ", round(stdev(fit_all), 2), " best_g: ",
                  round(fit_best_g, 2), " best_i: ", round(fit_best_n, 2), '-' if fit_best_n != fit_best_g else '')

            n += 1

        make_gif(n-1)

        # print final results
        print('FINAL:')
        print("best position:", [round(num, 2) for num in pos_best_g])
        print("Best fitness:", round(fit_best_g, 2))

# --- EXECUTE


print("melhor global até então | melhor global da iteração | média do fitness da iteração | desvio-padrão")


def run_pso():
    domains = [(-512, 512), (-512, 512)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
    PSO(eggholder, domains, num_particles=100, max_iter=400)
    return


if __name__ == "__main__":
    random.seed(17201571)
    run_pso()

# TODO: observar a otimização das aletas
# TODO: gerar um video
# TODO: limitar velocidade das partículas
# TODO: inverter velocidade quando atingir fim do domínio
