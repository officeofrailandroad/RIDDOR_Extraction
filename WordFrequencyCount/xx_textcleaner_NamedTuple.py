import collections
import re

def textcleaner (narrative):
    textchunk = collections.deque()
    
    for item in narrative.event_narrative:
        word = narrative.event_narrative
        word = str(word)
        word = word.lower()
        
        #word = narrative.Event_Narrative
        word = re.sub(r'\[a-z]'," ",word)
        word = re.sub(r'[\\[a-z]]'," ",word)
        word = re.sub(r'[^A-Za-z_]', " ", word)
        word = word.replace(" the "," ")
        word = word.replace(" a ", " ")
        word = word.replace(" was ", " ")
        word = word.replace(" she ", " ")
        word = word.replace(" he ", " ")
        word = word.replace(" at ", " ")
        word = word.replace(" and ", " ")
        word = word.replace(" to ", " ") 
        word = word.replace(" of "," ")
        word = word.replace(" on ", " ")
        word = word.replace(" that ", " ")
        word = word.replace(" had ", " ")
        word = word.replace(" were ", " ")
        word = word.replace(" by ", " ")
        word = word.replace(" being ", " ")
        word = word.replace(" with ", " ")
        word = word.replace(" in ", " ")
        word = word.replace(" for ", " ")
        word = word.replace(" from ", " ")
        word = word.replace(" - ", " ")
        word = word.replace(" as ", " ")
        word = word.replace(" 'at ", " ")
        word = word.replace(" when ", " ")
        word = word.replace(" not ", " ")
        word = word.replace(" they ", " ")
        word = word.replace(" no ", " ")
        word = word.replace(" reported ", " ")
        word = word.replace(" stated ", " ")
        word = word.replace(" advised ", " ")
        word = word.replace(" been ", " ")
        word = word.replace(" line ", " ")
        word = word.replace(" his ", " ")
        word = word.replace(" up ", " ")
        word = word.replace(" down ", " ")
        word = word.replace(" but ", " ")
        word = word.replace(" be ", " ")
        word = word.replace(" an ", " ")
        word = word.replace(" \t ", " ")
        word = word.replace(" \r ", " ")
        word = word.replace(" \n ", " ")
        word = word.replace(" site ", " ")
        word = word.replace(" it ", " ")
        word = word.replace(" after ", " ")
        word = word.replace(" 'at ", " ")
        word = word.replace(" is ", " ")
        word = word.replace(" this ", " ")
        word = word.replace(" her ", " ")
        word = word.replace(" there ", " ")
        word = word.replace(" out ", " ")
        word = word.replace(" which ", " ")
        word = word.replace(" has ", " ")
        word = word.replace(" all ", " ")
        word = word.replace(" have ", " ")
        word = word.replace(" taken ", " ")
        word = word.replace(" would ", " ")
        word = word.replace(" over ", " ")
        word = word.replace(" normal ", " ")
        word = word.replace(" confirmed ", " ")
        word = word.replace(" back "," ")
        word = word.replace(" their "," ")


        word = word.replace("   ", " ")
        word = word.replace("  ", " ")
 
     
  
        textchunk.append(word)

    return textchunk


