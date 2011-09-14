#!/usr/bin/python

import sys, csv, os

def die(msg): 
  print msg
  print "Exiting"
  sys.exit()

# Superclass
class Strategy:
  def __init__(self, args):
    self.args = args
    file = self.open(self.args[2])
    smells = self.sniff(file.read(4096))
    file.seek(0)
    self.reader = csv.reader(file, smells['format'])
    self.headers = self.get_headers(self.reader,smells['has_header'])
    
  def sniff(self, chunk):
    smells = {}
    sniffer = csv.Sniffer()
    smells['format'] = sniffer.sniff(chunk)
    smells['has_header'] = sniffer.has_header(chunk)
    return smells
    
  def get_headers(self,reader,has_header): 
    headers = {}
    if has_header:
      for k, v in enumerate(reader.next()):
        headers[v] = k
    else:
      for i in range(0,50):
        headers[str(i)] = i
        headers['NO_HEADERS'] = true
    return headers
    
  def open(self, path):
    try:
      return open(path,'rU')
    except:
      die("Bad file path:" + path)
    
# Strategies 
class DefaultStrategy():
  def __init__(self, args):
	self.args = args

  def execute(self):
    args = self.args
    path = args[1]
    try: 
	  args.append(args[2])
	  args[2] = path
	  strat = ListStrategy(args)
    except IndexError:
	  args.append(path)
	  strat = HeaderStrategy(args)
    strat.execute()

#  
class ListStrategy(Strategy):
  def execute(self):
    col = self.args[3]
    for row in self.reader:
      print row[self.headers[col]]

#   
class ListUniqueStrategy(Strategy):
  def execute(self):
    col = self.args[3]
    cset = set([])
    for row in self.reader:
      cset.add(row[self.headers[col]])
    for entry in cset:
      print entry

#
class HeaderStrategy(Strategy):
  def execute(self):
    try:
      self.headers['NO_HEADERS'] 
      print "No headers detected, use column index"
    except:
      for k, v in enumerate(self.headers):
        print v
        
#   
class CountStrategy(Strategy):
  def execute(self):
    count = 0
    for row in self.reader:
      count += 1
    print "%d records" % count
    
#   
class SizeStrategy(Strategy):
  def execute(self):
    bytes = float(os.path.getsize(self.args[2]))
    print "%.2f MB" % (bytes/float(2.**20.))


class HelpStrategy:
  def execute(self):
	print "\n**** Help for CSV-Analyzer ****\n"
	print "Usage:"
	print "\tcsv [-flags] file.csv [params]\n"
	print "Flags:"
	print "\t-l : [List] lists the contents of column name/index given as a param"
	print "\t\tcsv -l file.csv SOME_COLUMN_NAME\n"
	print "\t-lu : [Unique List] lists the unique contents of column name/index given as a param"
	print "\t\tcsv -lu file.csv SOME_COLUMN_NAME\n"
	print "\t-h : [Header] prints headers from the file if they are detected"
	print "\t\tcsv -h file.csv\n"
	print "\t-c : [Count] prints the row count"
	print "\t\tcsv -c file.csv\n"
	print "\t-s : [Size] prints the size of the file in Megabytes"
	print "\t\tcsv -s file.csv\n"
	print "Default (no flags):"
	print "\tcsv file.csv"
	print "\t\t lists headers, same as -h flag\n"
	print "\tcsv file.csv SOME_COLUMN_NAME"
	print "\t\t lists contens of given column, same as -l flag\n"
	print "Have a great day"
    
    
# There's def a better way to handle the flags...
def get_strategy(args):
  try:
	  flags = args[1]
	  if flags.startswith('-'):
	  
		if flags.startswith('-lu'):
		  return ListUniqueStrategy(args)
		  
		if flags.startswith('-l'):
		  return ListStrategy(args)
		  
		elif flags.startswith('-h'):
		  return HeaderStrategy(args)
		  
		elif flags.startswith('-c'):
		  return CountStrategy(args) 
		  
		elif flags.startswith('-s'):
		  return SizeStrategy(args)   
		
		else: 
		  return HelpStrategy()
		  
	  return DefaultStrategy(args)
  except:
    return HelpStrategy()

strat = get_strategy(sys.argv)
  
strat.execute()