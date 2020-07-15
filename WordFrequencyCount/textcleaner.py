import collections
import re


def textcleaner (narrative):
    """
    This functon removes key words, numeric and punctuation from strings, prior to later analysis.
    Parameters:
    - narrative: element from a tuple within a list

    Returns:
    - textchunk: a list of text with the text cleaned
    """
    
    
    textchunk = list()
    
    removal_list = [
        " the ", " a ", " was ", " she ", " he ", " at "," and ", " to "," of "," on "," that ", " had "," were "," by ", " being "," with ", 
    " in ", " for "," from "," - ", " as "," 'at "," when "," not "," they "," no "," reported ", " stated "," advised "," been ", 
    " line "," his "," up "," down "," but "," be "," an "," \t "," \r "," \n "," site "," it "," after ", " 'at "," is ", " this ", 
    " her ", " there ", " out ", " which ", " has "," all ", " have "," taken ", " would ", " over ", " normal ", " confirmed ", 
    " back ", " where ",]

    report = str(narrative)
    report = report.lower()
    report = re.sub(r'\[a-z]'," ",report)
    report = re.sub(r'[\\[a-z]]'," ",report)
    report = re.sub(r'[^A-Za-z_]', " ", report)

    for item in removal_list:
        if item in removal_list:
            report = report.replace(item," ")
            
    report = report.replace("   ", " ")
    report = report.replace("  ", " ")
  
    textchunk.append(report)
    
    return textchunk

def listclean(narrative_list):
    """
    This takes the textual element using from a list of tuples and appends it to a new list of strings
    Parameter:
    - narrative_list:       - list of tuples containing extracted warehouse data

    Returns:
    - finaltext:            - list of strings containing textual data

    """

    finaltext = list()
    for i in range(0,len(narrative_list)):
        cleanedtext = textcleaner(narrative_list[i][2])
        finaltext.append(cleanedtext)

    return finaltext
