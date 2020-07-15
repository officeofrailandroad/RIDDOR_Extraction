import pypyodbc
#from textcleaner_NamedTuple import textcleaner
import pandas as pd
import collections
from collections import namedtuple
from pprint import pprint


connection = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=192.168.10.26;'
    'Database=ORR_DW;'
    'uid=Live_SQLadmin;pwd=OrrCube2014'
    )

print("Connecting to ORR_DW: 192.168.10.26")
cursor = connection.cursor()

print("setting the SQL Command......")
SQLCommand = ("SELECT distinct [event date], [Event ID], [Event Narrative] FROM [ORR_DW].[LUL].[factt_230_SMIS_2018] WHERE [Event Narrative] is not NULL and [Report Statutory] like '%74%'") 

cursor.execute(SQLCommand)
print("Executing the command: \n \n" + SQLCommand )

#extract = list()
extract = collections.deque()
extract2 = namedtuple('extract', 'event_date event_id event_narrative')

popcount = 0
while True:
    row = cursor.fetchone()
    if row is None:
        break
    
    #convert row object into a list object
    extract.append([x for x in row])

    print(f"Appending {popcount} row of data", end = '\r')

    popcount += 1
    #put list object into named tuple
    
    for record in row:
        extract2.event_date = row[0]
        extract2.event_id = row[1]
        extract2.event_narrative = row[2]
    print (extract2.event_narrative)

    c = collections.Counter(str(textcleaner(extract2.eventnarrative)).split(' '))






print(f"{popcount} rows appended \n")
print(f"{len(extract)} rows in extract \n")

#list of dates
#date_list = [str(x[0]) for x in extract]
#pprint(str(date_list))

#for i in range(0,popcount):
#    pprint(i.event_narrative)




frequencies = c.most_common(200)

## words and frequencies    
pprint(frequencies)







