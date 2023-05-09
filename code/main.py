''' Task # 2: 
Choose one of the two algorithms, SARSA and Q-learning, run it for various values of α and compare the two in terms of:
- computational efficiency, i.e., the time taken to converge;
- maximizing reward: Run the learned policies for each α value for various starting states and calculate the average reward to see 
which α value results in the most average reward

Choosen Algorithm: Q-Learning '''

import gym
import numpy as np
import matplotlib.pyplot as plt
import random
from IPython.display import clear_output
from time import sleep
from matplotlib import animation

"""Initialize and validate the environment"""
env = gym.make("Taxi-v3", render_mode="rgb_array").env
state, _ = env.reset()

# Print dimensions of state and action space
print("State space: {}".format(env.observation_space))
print("Action space: {}".format(env.action_space))

# Sample random action
action = env.action_space.sample(env.action_mask(state))
next_state, reward, done, _, _ = env.step(action)

# Print output
print("State: {}".format(state))
print("Action: {}".format(action))
print("Action mask: {}".format(env.action_mask(state)))
print("Reward: {}".format(reward))

# Render and plot an environment frame
frame = env.render()
plt.imshow(frame)
plt.axis("off")
plt.show()
