import docx
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import pprint as pp
import pandas as pd
import datetime
import re

def main():
    
    doc = docx.Document('word_documents\\2020 01 11 NR Daily Log.docx')

    docaslist = list()
    finallist = list()
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            docaslist.append(block.text)
            
        #elif isinstance(block, Table):
        #    docaslist.append(table_print(block))
    
    docdf = cleanthelist(docaslist)
    dateofincident = getdate(doc)
    
    docdf = getrouteccil(docdf)
    docdf = getlocation(docdf)
       
    docdf.insert(0,'incident_date' , dateofincident)
    exportfile(docdf,'output\\','nrlog')

def getlocation(cleandoc):

    return cleandoc

def getrouteccil(docdf):
    """
    This splits the data frame column to produce new columns holding route and ccil information

    Parameters
    docdf:      A dataframe holding the paragraphs of the document

    Returns
    docdf:      A dataframe with new columns in appropriate order

    """
    docdf[['route','narrative']] = docdf['narrative'].str.split(' – ',1,expand=True)
    docdf[['ccil','narrative']]  = docdf['narrative'].str.split(' / ',1,expand=True)
    
    docdf = docdf[['route','ccil','narrative']]
    return docdf
    

def getdate(docobj):
    """
    Gets date from the core properties of the document, with the first 10 characters being the date.
    converts string into date format

    Parameters:
    docobj:            A docx object containing the document

    Returns:
    dateofincident:    A datetimeobject representing the date of the incident
    """
    dateofincident = datetime.datetime.strptime(str(docobj.core_properties.title)[:10],'%Y %m %d').date()

    return dateofincident


def cleanthelist(text):
    """
    This takes the list of paragraphs from the word document and removes irrelevant entries.  It finds paragraphs with the key
    reference point CCIL and appends them and the following paragraph to a new list.  This new list is then converted to a dataframe
    
    Parameters
    text:       A docx Document object containing the full document

    Returns
    textdf:     A dataframe holding the relevant text documents
    """
    
    finallist = list()
    
    #remove non-reports
    cleanerdoc = list(filter(None,text))
    #remove first 26 items - the cover page
    #cleanerdoc = cleanerdoc[26:]

    cleanerdoc = [i for i in cleanerdoc if not i.startswith('None')]
    cleanerdoc = [i for i in cleanerdoc if not i.startswith('Disconnected')]

    #mask for the CCIL codes
    ccil = [i for i, s in enumerate(cleanerdoc) if 'CCIL' in s]

    #join ccil codes and ccil text
    for i in ccil:
        finallist.append(cleanerdoc[i] +" / "+ cleanerdoc[i+1])

    textdf = pd.DataFrame(finallist,columns=['narrative'])


    return textdf


##unashamedly stolen from https://github.com/python-openxml/python-docx/issues/276
def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def table_print(block):
    tablelist = list()
    table=block
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                tablelist.append(paragraph.text)
               
    return tablelist


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
    df.to_csv(destinationpath + destinationfilename, encoding='cp1252')

if __name__ == '__main__':
    main()
