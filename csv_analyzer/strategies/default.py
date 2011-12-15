from strategy import Strategy
from field import Field

class Default(Strategy):
  def execute(self,reader):
    Field(self.args).execute(reader)
    
