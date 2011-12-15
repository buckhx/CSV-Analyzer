from strategy import Strategy
import operator

class Field(Strategy):
  def execute(self,reader):
    if 'NO_HEADERS' in reader.headers:
      print "No headers detected, use column index:"
      del reader.headers['NO_HEADERS']
    for x in sorted(reader.headers.iteritems(), key=operator.itemgetter(1)):
      print x[0]
