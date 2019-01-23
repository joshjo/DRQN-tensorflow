import gym
import time
from random import randint


env = gym.make('Breakout-v0')


for i_episode in range(20):
    observation = env.reset()
    x = randint(2, 3)
    old_reward = 0
    reward = 0
    for t in range(100):
        env.render()
        # action = env.action_space.sample()
        if t == 0:
            env.step(1)
        old_reward = reward
        observation, reward, done, info = env.step(x)
        if old_reward != reward:
            x = randint(2, 3)
        time.sleep(0.1)
        print('reward', reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close() 
