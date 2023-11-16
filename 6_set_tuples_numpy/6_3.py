from scipy import stats
import numpy as np

angles = stats.norm.rvs(loc = 48, scale = 7, size = 6000)
angles = np.reshape(angles, (1000, 6))
velocities = stats.weibull_max.rvs(2, loc=107, scale=4, size=6000)
velocities = np.reshape(velocities, (1000,6))
init_height = 2.0


alpha = np.radians(angles)
mps = velocities/3.6 
horizontal_velocity = mps * np.cos(alpha)
vertical_velocity = mps * np.sin(alpha)

airtime = (vertical_velocity + np.sqrt(vertical_velocity ** 2 + 2 * 9.81 * init_height))/9.81
distance = horizontal_velocity * airtime

alpha = 0.05



distance = np.sort(distance)

distance = np.amax(distance, axis=1)

lower_index = round((1000 * alpha)/2)
upper_index = round(1000*(1-alpha/2))-1


print(f"Lower interval: {distance[:lower_index]}")
print(f"Upper interval: {distance[upper_index:]}")

