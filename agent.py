"""
Name: Agent class

Project: UAV Obstacle Avoidance Using Q-Learning Techniques

Authors: Katherine Glasheen, Marc Gonzalez, Shayon Gupta, 
Travis Hainsworth, Ramya Kanlapuli
	
Description: This class extends the uav object to create
the agent in the simulation including Q-score and learning model.
"""

from uav import *

class agent(uav):
	
	# Intializer function
	def __init__(self, location):
		# Initialize uav super-class
		super.__init__(location)
		self.Q = #Q matrix, initialized as 3D matrix
		self.R = #initialize R matrix
		# Initialize learning model
		self.model = None
		
	# Function which gathers observations based on current position. Should return a matrix with the 
	def observe(self):
	    #Update Q matrix here, appendable dictionary?
	    
		pass

	# Function to generate rewards using observations and lookup table (create reward dict inside fxn?)
	def getRewards(self):
		pass
	
	# Function which takes in observations, rewards, and former Q-matrix and outputs the action that yields maximum Q using the standard method
	# main loop make location and rewards random and test
	# Haven't defined proper variable names, in development
	def predict_standard(self):
	
	    for i in range(horizon) #horizon is 4
	    
	    Q[location[0],location[1],action] = (1-alpha)*Q[location[0],location[1],action] + alpha*[Reward[location[0],location[1],action]] + gamma*max(Q[location_new[0],location_new[1],:]) 
	    
	    a = Q.index(max(Q[location[0],location[1],:])) 
	    
	    if a ==1 
	        command = "up"
	    elif a==2
	        command = "down"
	    elif a==3
	        command = "left"
	    elif a==4
	        command = "right"
	    
		return command	
		
	# Function which predicts next movement based on neural network learning model
	def predict_NN(self):
		return command
		
