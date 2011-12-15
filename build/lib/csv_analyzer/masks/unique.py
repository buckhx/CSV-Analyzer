from mask import Mask
from sys import exit as die

class Unique(Mask):
  
  def __init__(self,params):
    self.params = params
    self.set = set([])
  
  def is_masked(self, line, rheaders):
    if len(self.params) < 1:
      die("Unique mask requires parameters [--unique p1,p2,p3]")
    parameters = map(lambda x: x.lower(), self.params[0].split(','))

    headers = {}
    for k,v in enumerate(rheaders):
      headers[v.lower()] = rheaders[v]

    out = ""
    for param in parameters:
      try:
        val = line[headers[param]].lower()
      except KeyError:
        die("Bad parameters: \n"+str(parameters))
      out = out + val

    if out in self.set:
      return True
    else:
      self.set.add(out)
      return False 

#./csv_util.py -l tests/bmi_mediabase.csv Station,"Artist" --filter "date played"=.*12:10.* --unique station
