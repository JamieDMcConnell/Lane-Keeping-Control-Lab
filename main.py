#Modules imported
import numpy as np
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Class 'Car' created
class Car:

    # Constructor defines and initialises attributes of the 'Car' class
    def __init__(self,
                 length=2.3,
                 velocity=5,
                 x_pos_init=0, y_pos_init=0.3, pose_init=np.deg2rad(5)):
        self.__length = length
        self.__velocity = velocity
        self.__x = x_pos_init
        self.__y = y_pos_init
        self.__pose = pose_init
        self.__trajectory = None

    # 'y' method returns position on y axis
    def y(self):
        return self.__y
    # method 'move' takes steering angle argument and dt argument
    def move(self, steering_angle, dt):


        def bicycle_model(_t, z):

            theta = z[2]
            return [self.__velocity * np.cos(theta),
                    self.__velocity * np.sin(theta),
                    self.__velocity * np.tan(steering_angle) / self.__length]

        sol = spi.solve_ivp(bicycle_model,
                            [0, dt],
                            [self.__x, self.__y, self.__pose],
                            t_eval=np.linspace(0, dt, 2))

        new_state = sol.y[:, -1]
        self.__x = new_state[0]
        self.__y = new_state[1]
        self.__pose = new_state[2]

    def velocity(self):
        return self.__velocity

    def statex(self):
        return [self.__x]

    def statey(self):
        return [self.__y]

#Object 'car' created of class 'Car'
car = Car()

#Appropriate number of samples, 'N', chosen for length of time, 't_max', with sampling frequency 'h'
N = 50
t_max = 2
h = t_max / N

#Blank zero element array created of  which will be filled with trajectory data
states_cachex = np.zeros(shape=(N, 1))
states_cachey = np.zeros(shape=(N, 1))
#Constant steering action declared and defined. Negative value ('-2') corresponds to clockwise steering of 2 degrees.
#   This is converted to radians for use in calculations
u = np.deg2rad(-2)

#'for' loop logs x position data in numpy array
for i in range(N):
    car.move(steering_angle=u, dt=h)
    states_cachex[i, :] = car.statex()

#'for' loop logs y position data in numpy array
for i in range(N):
    car.move(steering_angle=u, dt=h)
    states_cachey[i, :] = car.statey()

#data is plotted
plt.rcParams['font.size'] = '14'
plt.plot(states_cachex, states_cachey)
plt.xlabel("x position")
plt.ylabel("y position")
plt.grid()
plt.show()




