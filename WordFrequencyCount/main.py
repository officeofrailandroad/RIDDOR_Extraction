from getsql import gettext
from pprint import pprint
from textcleaner import textcleaner, listclean
from frequencycount import wordfrequency
from plotdata import barplotter
from excelexporter import excelexport
import pandas as pd


def main():
    """
     The source file for delay minutes is held on the warehouse environment at 
     E//ORR_Data/ARTS Documents/DM_PPM_CaSL_Charts/Daily_Delay_Minutes/Daily_Delay_Minutes
     
     Data warehouse views for DDM: [ORR_DW].[NR].[factv_319_DDM_MDX]
     Data warehouse view for DDM, disagregrated !!but very slow: [ORR_DW].[NR].[factv_319_DDM_MDX_all]  
    """

    #Get the DDM data
    DDMSQLData = gettext("[source_item_id] ,[status],[date],[day_of_week],[delay_minutes]","[ORR_DW].[NR].[factv_319_DDM_MDX]","[status] = 'published' and [day_of_week] not in ('Saturday','Sunday')")
    
    #Convert to pandas DF
    pdDDM = pd.DataFrame(DDMSQLData, columns=['source_item_id','status','date','day_of_week','delay_minutes'])
    pdDDM['DDM_ranked'] = pdDDM['delay_minutes'].rank(ascending=1)

    GoodDDM = pdDDM[pdDDM.delay_minutes < pdDDM.delay_minutes.quantile(0.1)]
    BadDDM = pdDDM[pdDDM.delay_minutes > pdDDM.delay_minutes.quantile(0.9)]

    #get the good and bad dates
    GoodDMDays = GoodDDM.date
    BadDMDays = BadDDM.date

    #Get the text data
    WordSQLData = gettext("distinct [event date], [Event ID], [Event Narrative]","[ORR_DW].[LUL].[factt_230_SMIS_2018]", " [Event Narrative] is not NULL and [Report Statutory] like '%74%' ")
     
    pdWordSQLData = pd.DataFrame(WordSQLData,columns = ['event_date','event_id','event_narrative'])

    #print("THis is just the good days")
    good_days_events = pdWordSQLData[pdWordSQLData['event_date'].isin(GoodDMDays)]


    #print("This is just the bad days")
    bad_days_events = pdWordSQLData[pdWordSQLData['event_date'].isin(BadDMDays)]

    #list of count of words
    #word_count = sum([len(x[2]) for x in WordSQLData])
    #pprint(f"total count of words in extract is {word_count}")
    print(excelexport(good_days_events,"Good day events.xlsx",'Sheet1'))
    print(excelexport(bad_days_events,"Bad days events.xlsx",'Sheet1'))
    print(excelexport(pdWordSQLData,"All days events.xlsx",'Sheet1'))

    comparison_list = list()
    good_list = good_days_events.values.tolist()
    comparison_list.append(good_list)
    bad_list = bad_days_events.values.tolist()
    comparison_list.append(bad_list)
    all_list = pdWordSQLData.values.tolist()
    comparison_list.append(all_list)

    #define number of words to return
    top = 25
    
    for counter,item in enumerate(comparison_list,0):
        nameofchart = ['good','bad','total']
        
        finaltext = listclean(item)
        results = wordfrequency(finaltext,top)
        ##placeholder for excel export of results list
        pdresults = pd.DataFrame(results,columns=['word','count_of_references'])
        excelexport(pdresults,f"{nameofchart[counter]} days results.xlsx",'Sheet1')
        barplotter(results,top, nameofchart[counter])


  

if __name__ == '__main__':
    main() 