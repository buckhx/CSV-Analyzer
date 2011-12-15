import collections, os
from sys import exit as die
from reader import Reader
from execution import Execution
from strategies.strategies import Strategies as Strat
from masks.masks import Masks as Mask


class ExecFactory:

  def __init__(self,cmd_args):
    self.cmd_args = cmd_args[1:]

  #Refactor this factory relationship
  def buildExec(self):
    args = self.getArgs(self.cmd_args)
    strategy = self.buildStrategy(args["strategy"])
    reader = self.buildReader(args["file"], args["masks"])
    return Execution(strategy, reader)

### Context ###
  # Build Strategy
  def buildStrategy(self, strats):
    strat = strats.keys()[0]
    params = strats[strat]
    return Strat.build(strat, params)

  # Build Reader
  def buildReader(self, path, masklist):
    if os.path.isfile(path) is False:
      die("Invalid input file at: "+path)
    masks = []
    for mask in masklist:
      masks.append( Mask.build(mask, masklist[mask]) )
    return Reader(path, masks)

  # Get the Argument dict{}
  def getArgs(self, args):
    cmds = self.get_cmds(args)
    if len(cmds) < 1 or cmds.keys()[0].startswith('h'):
      die(Strat.Help())
    nargs = self.build_args(cmds)
    if len(nargs["strategy"]) != 1:
      die("Exactly ONE valid execution flag is required, see usage (-h)")
    strat = nargs["strategy"].keys()[0]
    if len(nargs["strategy"][strat]) < 1:
      die("File path required for this execution flag, see usage (-h)")
    nargs["file"] = nargs["strategy"][strat][0]
    return nargs

### Utilities ###
  def get_cmds(self, args):
    CMD_FLAG = '-'
    is_cmd = lambda x: x.startswith(CMD_FLAG)
    str_andard = lambda x: x.replace(CMD_FLAG,'').lower()
    cmds = {}
    if len(args) == 0:
      cmds["h"] = args
    elif not args[0].startswith(CMD_FLAG):
      cmds["f"] = args
    else:
      for arg in args:
        if is_cmd(arg):
          cmd = str_andard(arg)
          cmds[cmd] = []
        else:
          cmds[cmd].append(arg)
    return cmds
    
  def build_args(self, cmds):
    args = collections.defaultdict(dict)
    strats = filter(Strat.is_valid, cmds.keys())
    for strat in strats:
      params = cmds[strat]
      strat = Strat.get_strat(strat)
      args["strategy"][strat] = params
    masks = filter(Mask.is_valid, cmds.keys())
    for mask in masks:
      args["masks"][mask] = cmds[mask]
    return args
