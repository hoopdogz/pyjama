from record import Record
from db import DB

import sys
import os

# path = 'data/records.txt'
path = os.path.dirname(os.path.realpath(__file__)) + '/data/records.txt'

base = DB()
base.load(path)

if (sys.argv[1] == "add"):
  base.add_record("x,{},{}".format(sys.argv[2], sys.argv[3]).replace('-', ' '))
  base.save(path)

elif (sys.argv[1] == "get"):
  if(sys.argv[2] == "all"):
    for rec in base.records:
      print(base.read_record(rec.id).to_text())
  else:
    print(base.read_record(int(sys.argv[2])).to_text())
  
elif (sys.argv[1] == "edit"):
  base.update_record(sys.argv[2], sys.argv[3])
  base.save(path)

elif (sys.argv[1] == "del"):
  if(sys.argv[2] == "all"):
    base.records = []
  else:
    base.delete_record(sys.argv[2])
    
  base.save(path)