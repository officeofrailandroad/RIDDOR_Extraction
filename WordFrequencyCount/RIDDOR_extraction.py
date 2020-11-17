from sqlalchemy import create_engine, MetaData, select, Table, Column, Integer,String,DateTime
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pprint as pp
import datetime
import pyodbc
import pandas as pd


def main():

    #wordlisted = getwords()

    plain_df = getDWdata('01/11/2020','16/11/2020')
    output_file_name = 'RIDDOR_Data_2020_11_partial'

    filtered_df = plain_df
    #commented to run against full set
    #filtered_df = filternarratives(plain_df,wordlisted)
    
    stnlist = getSTNdata()
    
    #do 'fuzzy matching on the station name' and return known or not known
    df_with_stn = replace_loc_with_stn(filtered_df,stnlist)

    exportfile(df_with_stn,'output\\',output_file_name)


def replace_loc_with_stn(data,stn):
    print("get alt location")
    
    data['alt_location'] = data['location'].astype('str').map(lambda x: process.extractOne(x,stn)[0])
    print("get fit index")
    data['fit_index'] = data['location'].astype('str').map(lambda x: process.extractOne(x,stn)[1])
    print("return data")

    #data.apply(process.extractOne(data['location'],stn),axis=1,result_type='expand')
    #for row in  data:
        #print(row + "\n")
        #best_fit = process.extractOne(row['location'],stn)
        
        #pp.pprint(f"The location of '{row['location']}' gives us a best match of '{str(best_fit[0])}' with a match index of '{str(best_fit[1])}'")
        #data['possible_location'] = str(best_fit)
        #data['ranking of fit'] = str(best_fit)
    
    return data


def getwords():
    words = []
    userinput = ''
    while userinput != 'exit':
        userinput = input("please type a word to search for: type 'exit' to leave ")
        words.append(userinput)
    words.pop()
    return words


def getSTNdata():
    print("setting stn connection")
    engine = create_engine('mssql+pyodbc://AZORRDWSC01/ORR_DW?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes')
    conn = engine.connect()
    metadata = MetaData(engine)

    stn_list = list()
    print("reflecting snt view")
    stn_data = Table(
        'factv_station_LC_LUL_LMD_nonmainline_names',metadata,
        Column('location_name',String,key='location_name'),
        autoload=True,autoload_with=engine,schema='NRE'
        )

    print("selecting stn data")
    query = select([stn_data.c.location_name])

    print("eexcuting select")
    result = conn.execute(query)
    
    print("turning result set into list")
    for row in result:
        stn_list.append(row)
    
    print("closing connection")
    conn.close()
    
    print("return data ")
    return stn_list



def getDWdata(start_date, end_date):
    print("setting connection")
    engine = create_engine('mssql+pyodbc://AZORRDWSC01/ORR_DW?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes')
    conn = engine.connect()
    #session = Session(bind=conn)

    metadata = MetaData(engine)

    textual_data = Table(
        'SMIS_Weekly_Report_new_and_non_reports_2018_DT',metadata,
        Column('status_description',String,key='status_description'),
        Column('id_number',Integer,key= 'id_number'),
        Column('date_key',DateTime,key= 'date_key'),
        Column('location',String,key='location'),
        Column('organisation name',String,key='organisation_name'),
        Column('Operation Route',String,key='route'),
        Column('ORR_Team',String,key='orr_team'),
        Column('injury description',String,key='injury_description'),
        Column('Dangerous_Occurence',String,key='dangerous_occurrence'),
        Column('narrative',String,key='narrative'),
        autoload=True,autoload_with=engine,schema='RSD'
        )

    query = select(
                [textual_data.c.id_number,
                textual_data.c.status_description,
                textual_data.c.date_key,
                textual_data.c.location,
                textual_data.c.organisation_name,
                textual_data.c.route,
                textual_data.c.orr_team,
                textual_data.c.injury_description,
                textual_data.c.dangerous_occurrence,
                textual_data.c.narrative]
        ).distinct().where(textual_data.c.status_description == 'published').where(textual_data.c.date_key >= start_date).where(textual_data.c.date_key <= end_date)
    
    df = pd.read_sql_query(query,conn)

    conn.close()

    return df


def filternarratives(df, key_words):
    print("filtering text")
    
    colnames = ["id_number","date_key","location","organisation_name","route","orr_team","injury_description","dangerous_occurrence","narrative","search_word"]

    filtered_sets = []
    
    for word in key_words:
        answerset = df[df['narrative'].str.contains(word,case=False,na=False)]
        ans2 = answerset.copy()
        ans2["search_word"] = word
    
        filtered_sets.append(ans2)

    final_answer = pd.concat(filtered_sets)
    
    
    return final_answer


def exportfile(df,destinationpath,filename,numberoffiles=1):
    """
    This procedure exports the finalised file as a CSV file with a datetime stamp in filename

    Parameters:
    df        - a dataframe containing the finalised data
    destinationpath     - a string providing the filepath for the csv file
    numberoffiles       - an int with the number of files being processed
    
    Returns:
    None, but does export dataframe df as a csv object
    """
     
    formatted_date = datetime.datetime.now().strftime('%Y%m%d_%H-%M')
    destinationfilename = f'{filename}_{formatted_date}.csv'
    print(f"Exporting {filename} to {destinationpath}{destinationfilename}\n")
    print(f"If you want to check on progress, refresh the folder "+ destinationpath + " and check the size of the " + filename + ".csv file. \n")  
    df.to_csv(destinationpath + destinationfilename)



if __name__ == '__main__':
    main()
