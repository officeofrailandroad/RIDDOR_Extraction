import collections

def wordfrequency(textlist, countofbins):
    """
    This function produces a count of distinct words used in a string.
    Parameters:
    textlist        - A list of strings containing text to be counted
    countofbins     - An initiger specifying the top x results to be returned

    Returns
    frequencies     - A list of tuples containing words and their frequency count
    """
    c = collections.Counter(str(textlist).split(' '))

    # words and frequencies
    #how many words to see

    frequencies = c.most_common(countofbins)
    frequencies = [x for x in frequencies if x[0] not in  ("", "[","]","s","t","'at", "['at" ,"['","']"," ']")] 
 

    return (frequencies)
   
