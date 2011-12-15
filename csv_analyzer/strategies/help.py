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
    help += "\t-l, --list : [List] lists the contents of field list"+"\n"
    help += "\t\tcsv -l file.csv COL1,COL3\n"+"\n"

    help += "\t-f, --fields : [Fields] Print fields/headers from the file if they are detected, also is default"+"\n"
    help += "\t\tcsv -f file.csv\n"+"\n"

    help += "\t-c, --count : [Count] Print the row count"+"\n"
    help += "\t\tcsv -c file.csv\n"+"\n"

    help += "\t-a, --aggregate : [Aggregate] Aggregate field by breakdowns"+"\n"
    help += "\t\tcsv -a file.csv col4"+"\n"
    help += "\t\tcsv -a file.csv col4 by col6,col3\n"+"\n"

    help += "\t-g, --graph : [Graph] Graph field by series field"+"\n"
    help += "\t\tcsv -a file.csv col4"+"\n"
    help += "\t\tcsv -a file.csv col4 by col6,col3\n"+"\n"

    help += "Masks:"+"\n"
    help += "\t--filter : [Filter] masks results not matching filter params"+"\n"
    help += "\t\tcsv -l file.csv col1,col3 --filter col2=\"Nov. 26, 2010\",col6=swift\n"+"\n"

    help += "\t--unique : [Unique] masks non-unique records from field list"+"\n"
    help += "\t\tcsv -c file.csv --unique track,upc\n"+"\n"


    help += "Default (no flags):"+"\n"
    help += "\tcsv file.csv"+"\n"
    help += "\t\t lists fields, same as -f flag\n"+"\n"
    help += "Have a great day"+"\n"

    return help
