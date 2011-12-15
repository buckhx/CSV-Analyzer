from strategy import Strategy
from sys import exit as die
import httplib, json

class Graph(Strategy):
  
  def execute(self, reader):
    if len(self.params) < 1:
      die("Graph requires units [--graph file.csv units by f1]")
    val = self.params[1].lower().strip()
    if len(self.params) > 3 and self.params[2].lower() == "by":
      key = self.params[3].lower()
    else:
      die("by flag required")

    headers = self.clean_headers(reader.headers)
    self.in_headers([key],headers)
    self.in_headers([val],headers)

    data = {}
    for line in reader:
      try:
        value = float(line[headers[val]])
      except:
        print val + ' not a numerical field at line: '+ str(reader.count+1)
        continue
      lkey = line[headers[key]]
      if lkey not in data:
        data[lkey] = value
      else:
        data[lkey] =  data[lkey] + value 
    print self.get_url(data)


  def get_url(self, data):
    url = "https://chart.googleapis.com/chart?chs=500x200&cht=lc&chds=a&chd=t:"
    vals = ""
    if len(data) < 2:
      die("Need 2+ values to graph, investigate with aggregation\n"+str(data))
    for key in sorted(data.iterkeys()):
      vals = vals + str(data[key]) + ","
    url = url + vals[:len(vals)-1]
    
    conn = httplib.HTTPSConnection("www.googleapis.com")
    headers = {'Content-Type': 'application/json'}
    params = '{"longUrl": \"'+url+'\"}'
    conn.request("POST","/urlshortener/v1/url",params,headers)
    return json.loads(conn.getresponse().read())['id']
