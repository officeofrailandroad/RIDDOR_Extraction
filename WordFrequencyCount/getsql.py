import pypyodbc
from pprint import pprint


def gettext(fieldlist, tablename, search_term):
    """
    This function uses a odbc connection to connect to the ORR_DW database and extract data
    
    Parameters:
    - fieldlist: A string containing the fields to be extracted from the database table.
    - tablename: A string containing the table to be extracted from the warehouse.
    - search terms: A string containing the elements of the WHERE clause, filtering the return set
    Returns:
    - extract: A list of tuples, outer list is a row, inner tuples are each field.  Text fields are broken into separate strings.
     

    """
    extract = list()
    
    connection = pypyodbc.connect(
    "Driver={SQL Server};"
    "Server=172.21.5.21;"
    #'Server=192.168.10.26;'
    "Database=ORR_DW;"
    "uid=Live_SQLadmin;pwd=OrrCube2014"
    )

    #'Driver={SQL Server};'
    #'Server=AZORRDWSC01;'
    #'Database=ORR_DW;'
    #'uid=Live_SQLadmin;pwd=OrrCube2014'

    print("Connecting to ORR_DW: 192.168.10.26")
    cursor = connection.cursor()

    print("setting the SQL Command...... \n")
    SQLCommand = ("SELECT " + fieldlist + " FROM " + tablename + " WHERE " + search_term)

    
    cursor.execute(SQLCommand)
    print("Executing the command: \n \n" + SQLCommand + "\n")

    popcount = 0
    while True:
        row = cursor.fetchone()
        if row is None:
            break
    
        #convert row object into a list object
        extract.append(row)

        print(f"Appending {popcount} row of data", end = '\r')
        popcount += 1

    connection.close()
    print("closed connection ")
    print(f"{popcount} rows appended \n")
    print(f"{len(extract)} rows in extract \n")

    return (extract)


