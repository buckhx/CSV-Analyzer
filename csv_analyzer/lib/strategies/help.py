from strategy import Strategy

class Help(Strategy):
  def execute(self,reader):
    return Help.toString()

  @staticmethod
  def toString():
    help = "\n**** Help for CSV-Analyzer ****\n"+"\n"
    help += "Usage:"+"\n"
    help += "\tcsv [-flags] file.csv [params] [--masks]\n"+"\n"

    help += "Execution Flags:"+"\n"
    help += "\t-l, --list : [List] lists the contents of field list given as a param"+"\n"
    help += "\t\tcsv -l file.csv COL1,COL3\n"+"\n"
    help += "\t-f, --fields : [Fields] help +=s fields/headers from the file if they are detected, also is default"+"\n"
    help += "\t\tcsv -f file.csv"+"\n"
    help += "\t\tcsv file.csv\n"+"\n"
    help += "\t-c, --count : [Count] help +=s the row count"+"\n"
    help += "\t\tcsv -c file.csv\n"+"\n"
    help += "\t-a, --aggregate : [Aggregate-by] Aggregate field and breakdown aggregation"+"\n"
    help += "\t\tcsv -a file.csv col4\n"+"\n"
    help += "\t\tcsv -a file.csv col4 by col6,col3\n"+"\n"
    help += "\t\tcsv --aggregate file.csv col4 by col6,col3\n"+"\n"

    help += "Masks:"+"\n"
    help += "\t--filter : [Filter] masks results not matching filter params"+"\n"
    help += "\t\t\tParams are a list of field=regex tuples"+"\n"
    help += "\t\t\tRecords are 'filtered' out of results if they do not match on the regex"+"\n"
    help += "\t\t\tRegex list uses AND between all params"+"\n"
    help += "\t\tcsv -l file.csv col1,col3 --filter col2=\"Nov. 26, 2010\",col6=swift\n"+"\n"
    help += "\t--unique : [Unique] masks non-unique records from field list"+"\n"
    help += "\t\t\tUniqueness is based on given field list"+"\n"
    help += "\t\t\tUnique set stays in memory, keep in mind for large files"+"\n"
    help += "\t\tcsv -c file.csv --unique track,upc\n"+"\n"


    help += "Default (no flags):"+"\n"
    help += "\tcsv file.csv"+"\n"
    help += "\t\t lists fields, same as -f flag\n"+"\n"
    help += "Have a great day"+"\n"

    return help
