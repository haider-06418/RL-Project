# CS 352 - Introduction to Reinforcement Learning
## Course Project 
**Team Members:**
1. Mohammed Haider Abbas - 06418
2. Muhammad Ahsan - 06371

## About the Project

Implemented Q-learning algorithm on the Taxi learning problem from OpenAI's Gym Toy Text Taxi environment. Analyzed it for various values of α (Learning rate) in terms of: 
- Computational efficiency, i.e., the time taken to converge
- Maximizing reward: Running the learned policies for each α value for various starting states and calculating the average reward to see which α value results in the most average reward

More information about OpenAI's GYM Toy Text Taxi environment can be found here:
[GYM Toy Text](https://www.gymlibrary.dev/environments/toy_text/)
[Taxi Environment](https://www.gymlibrary.dev/environments/toy_text/taxi/)

## The Taxi Problem:

The Taxi Problem is a classical problem in Reinforcement Learning. In this problem, the agent (taxi) needs to pick up the passenger from one of the four colored place and deliver the passenger to the destination (also one of the four colored place). The game is in 5 by 5 grid world. There are six actions that are available to the agent in this game: LEFT, RIGHT, UP, DOWN, PICKUP and PUTDOWN. The first four action will make the agent move 1 step forward according to the direction of the action, but won't have effect when the agent hits the wall or boundaries. At each step, the agent will receive a reward of -1. However, when the delivery is achieved, it will receive a reward of 20. In some conditions, several actions are illegal. This includes but not limited to take PUTDOWN action when there is no passenger in the taxi or it is not the destination spot, PICKUP a passenger where there is no passenger and so on. All these illegal action will cause a reward of -10 and change nothing. Thus, without any state abstraction, there are totally 500 states, including 25 position of the taxi, 4 possible location of the destination, and 5 possible location of the passenger (four colors and taxi). 