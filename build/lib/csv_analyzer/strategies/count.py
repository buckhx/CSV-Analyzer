from strategy import Strategy

class Count(Strategy):
  def execute(self,reader):
    count = 0
    for rec in reader:
      count = count + 1
    print count
