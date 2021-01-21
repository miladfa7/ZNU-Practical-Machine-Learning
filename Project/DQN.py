import time
import sys
import random
import numpy as np
import tensorflow
from Environment import Env
from collections import deque
from tensorflow.keras.layers import Dense, Conv2D, Reshape, MaxPool2D, Activation ,Flatten
from tensorflow.keras.optimizers import Adam, RMSprop ,SGD
from tensorflow.keras.models import Sequential


EPISODES = 5000
STATE_SZIE = 225


class DQNAgent:
    def __init__(self):

        self.render = False
        self.load = False
        self.save_loc = './DQN'
        self.action_size = 4
        self.discount_factor = 0.99
        self.learning_rate = 0.01
        self.epsilon = 1.0
        self.epsilon_decay = 0.99997
        self.epsilon_min = 0.01
        self.batch_size = 128
        self.train_start = 500
        self.memory = deque(maxlen=2000)
        self.state_size = STATE_SZIE
        self.model = self.build_model()
        self.target_model = self.build_model()
        self.update_target_model()

        # if self.load:
        #     self.load_model('model.h5')

    
    def build_model(self):
        # Neural Network for Deep Q-learning

        return model

    def select_action(self, state):
        
        # select action using epsilon-greedy
        pass

    def MEMORY(self, state, action, reward, next_state, goal):
        # save <s,a,r,s'> to the memory
        pass


    def update_target_model(self):
        # update target model
        pass

    def train_replay(self):
        # pick samples randomly from replay memory (with batch_size)
        # max Q value among next state's actions
        # DQN chooses the max Q value among next actions
        # selection and evaluation of action is 
        # on the target Q Network
        # Q_max = max_a' Q_target(s', a')
        # Q_max = reward + gamma * Q_max

        for i in range(self.batch_size):
            # like Q Learning, get maximum Q value at s'
            # But from target model
            
            # the key point of DQN
            # selection of action is from model
            # update is from target model

            # make minibatch which includes target q value and predicted q value
            # and do the model fit
            pass



    # save the model which is under training
    def save_model(self):
        self.model.save_weights('model.h5')

    # load the saved model
    def load_model(self):
        self.model.load_weights('model.h5')

if __name__ == "__main__":

    # create environment
    env = Env()
    agent = DQNAgent()
   


    # code



    for e in range(EPISODES):
        state = env.reset()
        

        # code


        while (not goal) and (not wumpus):
            if agent.render:
                env.render()
            


            # code


            if goal == True:

               # code
               pass

            elif wumpus == True:
               
               # code
                print("episode: {:3}   score: {:8.6}    epsilon {:.3}"
                      .format(e, float(score), float(agent.epsilon)))




        # save the model every 100 episodes
        if e % 100 == 0:
            agent.save_model()
