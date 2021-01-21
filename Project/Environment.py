import time
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
# pixels
UNIT = 60
# grid h*w
HEIGHT = 15
WIDTH = 15


class Env(tk.Tk):
    def __init__(self):
        super(Env, self).__init__()
        self.action = ['up', 'down', 'left', 'right']
        self.action_size = len(self.action)
        self.observation_size = (HEIGHT, WIDTH)
        self.title(' Wumpus DQN ')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, WIDTH * UNIT))
        self.images = self.load_images()
        self.canvas = self.build_canvas()
        self.rewards = []
        self.goal = []
        self.set_rewards()


    def build_canvas(self):

        canvas = tk.Canvas(self, bg='white',
                           height=HEIGHT * UNIT,
                           width=WIDTH * UNIT)

        for c in range(0, WIDTH * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, HEIGHT * UNIT
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, HEIGHT * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, HEIGHT * UNIT, r
            canvas.create_line(x0, y0, x1, y1)

        self.agent = canvas.create_image((UNIT*np.random.choice(HEIGHT)) + UNIT/2,
                                              (UNIT*np.random.choice(WIDTH))+UNIT/2, image=self.images[0])
        canvas.pack()
        return canvas


    def load_images(self):

        agent = PhotoImage(
            Image.open("img/agent3.png").resize((50, 50)))

        wumpus = PhotoImage(
            Image.open("img/wumpus1.png").resize((55, 55)))

        goal = PhotoImage(
            Image.open("img/gold.png").resize((50, 50)))

        hole = PhotoImage(
            Image.open("img/hole2.jpg").resize((55, 55)))

        wall = PhotoImage(
            Image.open("img/wall.png").resize((50, 50)))

        return agent, wumpus, goal ,hole ,wall


    def set_reward(self, state, reward):
        x = state[0]
        y = state[1]
        temp = {}

        if reward == 100:
            temp['reward'] = reward
            temp['figure'] = self.canvas.create_image((UNIT * x) + UNIT / 2,
                                                       (UNIT * y) + UNIT / 2,
                                                       image=self.images[2])
            self.goal.append(temp['figure'])

        elif reward== -100:
            temp['reward'] = reward
            temp['figure'] = self.canvas.create_image((UNIT * x) + UNIT / 2,
                                                      (UNIT * y) + UNIT / 2,
                                                      image=self.images[1])
        elif reward== -10:
            temp['reward'] = reward
            temp['figure'] = self.canvas.create_image((UNIT * x) + UNIT / 2,
                                                      (UNIT * y) + UNIT / 2,
                                                      image=self.images[3])

        elif reward == -1:
            temp['reward'] = reward
            temp['figure'] = self.canvas.create_image((UNIT * x) + UNIT / 2,
                                                      (UNIT * y) + UNIT / 2,
                                                      image=self.images[4])

        temp['coords'] = self.canvas.coords(temp['figure'])
        temp['state'] = state
        self.rewards.append(temp)
        #{'reward': 100, 'figure': 250, 'coords': [150.0, 270.0], 'state': [2, 4]}

    def set_rewards(self):

        # wall
        self.set_reward([1, 2], -1)
        self.set_reward([2, 2], -1)
        self.set_reward([3, 3], -1)
        self.set_reward([9, 3], -1)
        self.set_reward([10, 3], -1)
        self.set_reward([12, 3], -1)
        self.set_reward([7, 4], -1)
        self.set_reward([6, 5],-1)
        self.set_reward([14, 5],-1)
        self.set_reward([0, 6], -1)
        self.set_reward([1, 6], -1)
        self.set_reward([2, 6], -1)
        self.set_reward([6, 6], -1)
        self.set_reward([10, 6], -1)
        self.set_reward([6, 7], -1)
        self.set_reward([10, 7], -1)
        self.set_reward([10, 8], -1)
        self.set_reward([13, 8], -1)
        self.set_reward([9, 9], -1)
        self.set_reward([13,9], -1)
        self.set_reward([3, 9], -1)
        self.set_reward([4, 9], -1)
        self.set_reward([9, 10], -1)
        self.set_reward([2, 11], -1)
        self.set_reward([8, 12], -1)
        self.set_reward([12, 1], -1)
        self.set_reward([12, 2], -1)

        # hole
        self.set_reward([1, 0], -10)
        self.set_reward([5, 1], -10)
        self.set_reward([9, 2], -10)
        self.set_reward([1, 3], -10)
        self.set_reward([8, 6], -10)
        self.set_reward([2, 7], -10)
        self.set_reward([4, 7], -10)
        self.set_reward([5, 10], -10)
        self.set_reward([10, 10], -10)
        self.set_reward([14, 11], -10)
        self.set_reward([3, 12], -10)
        self.set_reward([1, 14], -10)
        self.set_reward([9, 14], -10)

       # wumpus
        self.set_reward([11, 5], -100)
        self.set_reward([8, 11], -100)

        # goal
        self.set_reward([2, 4], 100)

    def check_if_reward(self, state):
        check_list = dict()
        check_list['if_goal'] = False
        check_list['if_wumpus'] = False
        check_list['if_hole'] = False
        check_list['if_wall'] = False

        rewards_score = 0
        for reward in self.rewards:
            if reward['state'] == state:
                rewards_score += reward['reward']
                if reward['reward'] == 100:
                    check_list['if_goal'] = True
                elif reward['reward'] == -100:
                    check_list['if_wumpus'] = True
                elif reward['reward'] == -10:
                    check_list['if_hole'] = True
                elif reward['reward'] == -1:
                    check_list['if_wall'] = True

        check_list['rewards'] = rewards_score

        return check_list

    def coords_to_state(self, coords):
        x = int((coords[0] - UNIT / 2) / UNIT)
        y = int((coords[1] - UNIT / 2) / UNIT)

        return [x, y]

    def reset(self):
        self.update()
        time.sleep(0.2)
        self.canvas.delete(self.agent)
        self.agent = self.canvas.create_image((UNIT*np.random.choice(HEIGHT)) + UNIT/2,
                                              (UNIT*np.random.choice(WIDTH))+UNIT/2, image=self.images[0])

        self.reset_reward()
        return self.get_state()

    def reset_reward(self):
        for reward in self.rewards:
            self.canvas.delete(reward['figure'])

        self.rewards.clear()
        self.goal.clear()
        self.set_rewards()

    def get_state(self):

        agent_state = self.coords_to_state( self.canvas.coords(self.agent) )
        state_map = np.zeros((WIDTH, HEIGHT))

        for reward in self.rewards:
            if reward['reward'] == -1 :
                value = -1
                state_map[reward['state'][1], reward['state'][0]] = value

            elif reward['reward']== -10:
                value = -10
                state_map[reward['state'][1], reward['state'][0]] = value


            elif reward['reward']== -100 :
                value = -100
                state_map[reward['state'][1], reward['state'][0]] = value

            elif reward['reward'] == 100:
                value = 100
                state_map[reward['state'][1], reward['state'][0]] = value
            state_map[agent_state[1], agent_state[0]] = 1

        return state_map

    def move(self, agent, action):
        agent_state = self.canvas.coords(agent)
        # agent_state = [450.0, 690.0]
        base_action = np.array([0, 0])

        if action == 0:  # up
            if agent_state[1] > UNIT:
                base_action[1] -= UNIT
                # base_action[1] = -60
                coords_action =(base_action[0]+agent_state[0], base_action[1]+agent_state[1] )
                check_list = self.check_if_reward(self.coords_to_state(list(coords_action)))
                wall = check_list["if_wall"]

                if wall ==True :
                    base_action[1] = 0

        elif action == 1:  # down
            if agent_state[1] < (HEIGHT - 1) * UNIT:
                base_action[1] += UNIT
                coords_action =(base_action[0]+agent_state[0] , base_action[1]+agent_state[1])
                check_list = self.check_if_reward(self.coords_to_state(list(coords_action)))
                wall = check_list["if_wall"]

                if wall ==True :
                    base_action[1] = 0

        elif action == 2:  # right
            if agent_state[0] < (WIDTH - 1) * UNIT:
                base_action[0] += UNIT
                coords_action =(base_action[0]+agent_state[0] , base_action[1]+agent_state[1])
                check_list = self.check_if_reward(self.coords_to_state(list(coords_action)))
                wall = check_list["if_wall"]

                if wall ==True :
                    base_action[0] = 0


        elif action == 3:  # left
            if agent_state[0] > UNIT:
                base_action[0] -= UNIT
                coords_action =( base_action[0]+agent_state[0] , base_action[1]+agent_state[1] )
                check_list = self.check_if_reward(self.coords_to_state(list(coords_action)))
                wall = check_list["if_wall"]

                if wall ==True :
                    base_action[0] = 0


        # moving agent
        self.canvas.move(agent, base_action[0], base_action[1])
        agent_state = self.canvas.coords(agent)

        return agent_state

    def step(self, action):

        next_coords = self.move(self.agent, action) # [30,30] --- Next [90,30]
        check_list = self.check_if_reward(self.coords_to_state(next_coords))
        #print(check_list)   {'if_goal': False, 'if_wumpus': False,
                           #  'if_hole': True, 'if_wall': False, 'rewards': -10}

        wumpus = check_list["if_wumpus"]
        goal = check_list['if_goal']
        reward = check_list['rewards']
        # move agent
        self.canvas.tag_raise(self.agent)
        next_state = self.get_state()
        self.render()
        return next_state, reward, goal ,wumpus


    def render(self):
        self.update()
