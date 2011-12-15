import os,csv
from sys import exit as die

INIT_READ_SIZE = 4096

class Reader:
 
  def __init__(self, path, masks):
    self.file = self.open(path)
    smells = self.sniff(self.file)
    self.masks = masks
    self.reader = csv.reader(self.file, smells['format'])
    self.headers = self.get_headers(smells['has_header'])
    self.count = 0
    self.errors = []

  def __iter__(self):
    return self

  def next(self):
    self.count = self.count + 1
    try:
      line = self.reader.next()
      while self.masked(line): 
        self.count = self.count + 1
        line = self.reader.next()
        if line is None:
          raise StopIteration
      return line

    except Exception as e:
      if type(e) == StopIteration:
         raise StopIteration
      else:
        self.errors.append("Error on line: " + str(self.count)  + "\n" + str(e) + "\n")


### Utilities ###
  
  # Mask records
  def masked(self,line):
    if len(self.masks) is 0:
      return False 
    mapped = map( lambda m: m.is_masked(line,self.headers), self.masks )
    reduced = reduce( lambda x,y: x or y, mapped )
    return reduced
   
  # Open the file for reading or die
  def open(self, path):
    try:
      return open(path, 'rU')
    except:
      die("Bad file path" + path)

  # Gets smells {'format','has_header'}
  def sniff(self, file):
    smells = {}
    sniffer = csv.Sniffer()
    chunk = self.get_chunk(file)
    smells['format'] = sniffer.sniff(chunk)
    smells['has_header'] = sniffer.has_header(chunk)
    return smells

  # Gets first INIT_READ_SIZE bytes of file
  def get_chunk(self, file):
    chunk = file.read(INIT_READ_SIZE)
    file.seek(0)
    return chunk

  # Get headers if they exist
  def get_headers(self,has_header):
    headers = {}
    if has_header:
      for k, v in enumerate(self.reader.next()):
        headers[v.strip().translate(None,"\xef\xbb\xbf\"")] = k
    else:
      for k, v in enumerate(self.reader.next()):
        headers[str(k)] = k
        headers['NO_HEADERS'] = True
        self.file.seek(0)
    return headers

