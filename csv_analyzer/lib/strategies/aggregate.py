from strategy import Strategy
from sys import exit as die

class Aggregate(Strategy):

  def execute(self,reader):
    if len(self.params) < 2:
      die("Aggregation requires a field list [--aggregate file.csv units by f1,f2]")
    agg = self.params[1].lower().strip()
    if len(self.params) > 3 and self.params[2].lower() == "by":
      keys = map( lambda x: x.lower().strip(), self.params[3].split(','))
    else:
      keys = []

    headers = self.clean_headers(reader.headers)
    self.in_headers([agg],headers)
    self.in_headers(keys,headers)
    
    counts = {}
    for line in reader:
      if line is None : continue
      try:
        incr = float( line[headers[agg]] )
      except ValueError:
        print agg + ' not a numerical field at line: '+ str(reader.count+1)
        continue
      key = self.get_keys_hash(keys, line, headers)
      if key not in counts:
        counts[key] = incr
      else:
        counts[key] = counts[key] + incr

    keys.append(agg)
    print ", ".join(keys)
    for key in counts:
      print key + str(counts[key])


### Utils ###
  def get_keys_hash(self,keys,line,headers):
    hash = ""
    for key in keys:
      hash = hash + line[headers[key]] + ", "
    return hash

    



#./csv --aggregate file.csv 'col4' --by 'col3','col7'
#./csv_util.py -a /Users/buck/Documents/sony/sc/sc_sony_backfillstore_010110_100911.csv "all visits" --by "nbs artist id"
