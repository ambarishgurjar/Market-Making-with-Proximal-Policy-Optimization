import gym
import numpy as np
import asyncio
from stable_baselines3 import PPO
from quantpylib.hft.mocks import Replayer
from quantpylib.gateway.master import Gateway
from quantpylib.hft.oms import OMS
from quantpylib.hft.feed import Feed

class QuantpyMarketEnv(gym.Env):
    def __init__(self, replayer, oms, feed, ticker):
        self.replayer = replayer
        self.oms = oms
        self.feed = feed
        self.ticker = ticker
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(3,))
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(2,))  # bid/ask spread
        self.mid_price = 0
        self.inventory = 0

    def reset(self):
        self.inventory = 0
        self.mid_price = self.feed.lob_mid(self.ticker)
        return np.array([self.mid_price, self.inventory, 0])

    def step(self, action):
        bid_spread, ask_spread = np.abs(action)
        mid = self.feed.lob_mid(self.ticker)

        bid_price = mid - bid_spread
        ask_price = mid + ask_spread

        # submit orders via OMS
        asyncio.run(self.oms.limit_order(exc='bybit', ticker=self.ticker, amount=0.01, price=bid_price))
        asyncio.run(self.oms.limit_order(exc='bybit', ticker=self.ticker, amount=-0.01, price=ask_price))

        # Simulate fills
        executed_bid = np.random.rand() < 0.5
        executed_ask = np.random.rand() < 0.5

        pnl = 0
        if executed_bid:
            self.inventory += 0.01
            pnl -= bid_price * 0.01
        if executed_ask:
            self.inventory -= 0.01
            pnl += ask_price * 0.01

        reward = pnl - (0.1 * self.inventory ** 2)

        self.mid_price = mid
        done = self.replayer.finished()

        obs = np.array([self.mid_price, self.inventory, pnl])
        return obs, reward, done, {}

async def main_ppo():
    gateway = Gateway()
    await gateway.init_clients()

    replayer = Replayer(...)
    oms = replayer.get_oms()
    feed = replayer.get_feed()

    env = QuantpyMarketEnv(replayer, oms, feed, ticker='SOLUSDT')

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)

    obs = env.reset()
    while not replayer.finished():
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        if done:
            break

    await gateway.cleanup_clients()

if __name__ == "__main__":
    asyncio.run(main_ppo())
