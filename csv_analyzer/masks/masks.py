from filter import Filter
from unique import Unique

class Masks:
  masks = ["filter","unique"]

  @staticmethod 
  def build(mask, params):
    return globals()[mask.capitalize()](params)

  @staticmethod
  def is_valid(cmd):
    masks = Masks.masks
    cmd = cmd.replace('-','').lower()
    return cmd in masks


