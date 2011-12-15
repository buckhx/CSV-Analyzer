

class Execution:

  def __init__(self,strategy,reader):
    self.reader = reader
    self.strategy = strategy

  def run(self):
    try:
      self.strategy.run(self.reader)
    except KeyboardInterrupt:
      print "\nApplication Killed, thanks bro"

