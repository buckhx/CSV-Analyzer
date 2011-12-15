from sys import exit as die

class Strategy:

  def __init__(self, params):
    self.params = params

  def run(self, reader):
    self.execute(reader)
    if reader and len(reader.errors) > 0:
      print "\n*** Errors ***"
      for error in reader.errors:
        print error

  def execute(self,reader):
    die("no strategy")

  def get_fields(self, field_str):
    if len(field_str) < 1:
      cols = map(lambda x: x.lower(), reader.headers.keys() )
    else: 
      cols = map(lambda x: x.lower(), cols)    

  def clean_headers(self, r_headers):
    headers = {}
    for k,v in enumerate(r_headers):
      headers[v.lower().strip()] = r_headers[v]
    return headers

  def in_headers(self, keys, headers):
    if not set(keys).issubset(headers) : self.H_ERROR(keys,headers)

  def H_ERROR(self, keys, headers):
    error = 'Field list not included in Header set\n'
    error += "Input:\n"
    error += "\t"+str(keys)+"\n"
    error += "Headers:\n"
    for x in headers:
      error += "\t'" + x + "'\n"
    die(error)
