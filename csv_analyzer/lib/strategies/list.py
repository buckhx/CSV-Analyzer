from strategy import Strategy

class List(Strategy):

  def execute(self, reader):
    if len(self.params) == 1:
      cols = map(lambda x: x.lower(), reader.headers.keys() )
    else: 
      cols = self.params[1].split(',')
      cols = map(lambda x: x.lower(), cols)
    headers = self.clean_headers(reader.headers)

    try:
      for line in reader:
        if line is None:
          continue
        vals = map(lambda x: line[headers[x]], cols)
        out = ""
        for val in vals:
          out = out + val + ", "
        print out[:len(out)-2]

    except KeyError:
      print "Input set not included in Header set"
      print "Input:"
      print "\t"+str(cols)
      print "Headers:"
      for x in headers:
        print "\t'" + x + "'"
 
