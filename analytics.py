from scipy.spatial import distance
import random
#For plotting
import matplotlib.pyplot as plt
#for matrix math
import numpy as np
#for normalization + probability density function computation
from scipy import stats
#for plotting
import seaborn as sns
sns.set_style("white")




class episode_per_distance:
    def __init__(self,target,end_effector):
        #target is an array of 3 numbers [x,y,z]
        #end_effect is an array of  numbers [x,y,z]
        self.target=target
        self.end_effector=end_effector
        self.dis=distance.euclidean(self.target,self.end_effector)
        #dis is the distance calculated for each episode


episode_array=[] # empty array initialization of arraylist
episode_distance=[] # # empty array initialization of arraylist
for episode in range(1,5):# range of episodes,put the code below in the loop when calculating observations for each episode
    target=random.sample(range(1, 10),3) # random value of target
    end_effector=random.sample(range(1, 10),3) # random value of end_effector
    # print(episode_distance(target,end_effector).dis)
    episode_distance.append(episode_per_distance(target,end_effector).dis) # arraylist appending distance for episode
    episode_array.append(episode) # arraylist appending episodes
#

plt.figure(1)
plt.scatter(episode_distance,episode_array) # plot to scatter points
plt.figure(2)
sns.distplot(episode_distance, bins=50, kde=False) # plot of the histogram ,bins defines how fine you want the range to be
# plt.figure(3)
# sns.distplot(episode_distance, fit=stats.norm, bins=50, kde=False,) # Use to be fir gaussian on your plot,wouldn't look good have to go with gaussain mixture model if you really want to fit gaussians
