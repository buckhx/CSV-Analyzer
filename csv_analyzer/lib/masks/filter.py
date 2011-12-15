from mask import Mask
from sys import exit as die
import re

class Filter(Mask):
  
  def is_masked(self, line, rheaders):

    if len(self.params) < 1:
      die("Filter mask requires parameters [--filter p1=regex*1,p2=[regex]+2]")
    parameters = self.params[0].split(',')
    headers = {}
    for k,v in enumerate(rheaders):
      headers[v.lower()] = rheaders[v]

    for param in parameters:
      bits = param.split('=')
      col = bits[0].lower()
      reg = bits[1].lower()
      if not col in headers:
        die(col + " not in Header set")
      val = line[headers[col]].lower()
     # print val + " " + regex
      try:
        regex = re.compile(reg.lower())
      except:
        die("Bad regex: "+reg)
      if re.search(regex, val) is None:
        return True
    return False
    
    


#./csv_util.py -l tests/bmi_mediabase.csv Station,"Artist" --filter "date played"=.*12:10.*    

