from src.util import *
import matplotlib.pyplot as plt

PLOTSIZE = (30,10)

class Plot:
    def __init__(self, ret, pos, cost):
        self.ret = ret
        self.pos = pos
        self.cost = cost
        self.turnover = turnover(self.pos)
        self.pnl = self.pos * self.ret
        self.daily_pnl = daily(self.pnl)
        self.daily_pnl_cost = self.daily_pnl - daily(t_cost(self.turnover,self.cost))

    def plot_cumulative_pnl(self):
        fig, ax = plt.subplots(figsize=PLOTSIZE)
        self.daily_pnl.cumsum().plot(ax=ax)
        self.daily_pnl_cost.cumsum().plot(ax=ax)
