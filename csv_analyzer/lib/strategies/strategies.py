#change to use __import__
from default import Default
from list import List
from field import Field
from count import Count
from help import Help
from aggregate import Aggregate
from graph import Graph

class Strategies:
  strategies = ["default","list","field","count","aggregate","graph","help"]

  @staticmethod 
  def build(strat, params):
    return globals()[strat.capitalize()](params)
  
  @staticmethod
  def get_strat(strategy):
    strategies = Strategies.strategies
    for strat in strategies:
      if strategy == strat or strat.startswith(strategy):
        return strat

  @staticmethod
  def is_valid(cmd):
    strategies = Strategies.strategies
    cmd = cmd.replace('-','').lower()
    prefixes = set(map(lambda x: x[0], strategies))
    return cmd in set(strategies) | prefixes

  @staticmethod
  def Help():
    return Help(None).toString()

