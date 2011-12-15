from factory import ExecFactory

class CSVAnalyzer:
  def __init__(self, args):
    self.factory = ExecFactory(args)
    self.execution = self.factory.buildExec()
    self.execution.run()
