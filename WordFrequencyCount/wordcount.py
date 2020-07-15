import collections
import pypyodbc
from pprint import pprint
from plotdata import barplotter
from textcleaner import textcleaner
"""
This is legacy code and can be ignored

"""
extract = list()
finaltext = list()

#connection = pypyodbc.connect(
#'Driver={SQL Server};'
#'Server=192.168.10.26;'
#'Database=ORR_DW;'
#'uid=Live_SQLadmin;pwd=OrrCube2014'
#)

#print("Connecting to ORR_DW: 192.168.10.26")
#cursor = connection.cursor()

#search_term = '62'
#print("setting the SQL Command......")
#SQLCommand = ("SELECT distinct [event date], [Event ID], [Event Narrative] FROM [ORR_DW].[LUL].[factt_230_SMIS_2018]" 
#            "WHERE [Event Narrative] is not NULL and [Report Statutory] like '%" + search_term + "%'")

#cursor.execute(SQLCommand)
#print("Executing the command: \n \n" + SQLCommand )

#popcount = 0
#while True:
#    row = cursor.fetchone()
#    if row is None:
#        break
    
#    #convert row object into a list object
#    extract.append(row)

#    print(f"Appending {popcount} row of data", end = '\r')
#    popcount += 1

#connection.close()
#print("closed connection ")
#print(f"{popcount} rows appended \n")
#print(f"{len(extract)} rows in extract \n")



    
##list of count of words
#word_count = sum([len(x[2]) for x in extract])
#pprint(f"total count of words in extract is {word_count}")

## print all data
##for i in range(0,len(extract)):
##    pprint(extract[i][2])


#for i in range(0,len(extract)):
#    cleanedtext = textcleaner(extract[i][2])
#    finaltext.append(cleanedtext)

##pprint(finaltext)
##print(type(finaltext))
##pprint(extract2)



#c = collections.Counter(str(finaltext).split(' '))

## words and frequencies
##how many words to see
#top = 20    
#frequencies = c.most_common(top)
#frequencies = [x for x in frequencies if x[0] not in  ("", "[","]","s","t","'at", "['at" ,"['","']"," ']")] 
#pprint(frequencies)

#barplotter(frequencies, top)










