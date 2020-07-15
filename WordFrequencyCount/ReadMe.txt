Dear Ruben,

Thanks for agreeing to look at this.  My main points are below, but any more general advice is welcome 

The main areas for improvement here I think are

Main.py:
1) Line 21: I'd rather be using "for item in NY", but I seemed to get error messages 
2) Line 23: Convert generic list into Named Tuples, so that (textcleaner(SQLData[i][2]) becomes SQLData(SQLData(NT.narrative_text))      )

Frequency.py
1) Line 4 I converted the whole list to a giant string, which feels clunky and produced characters like "['" and "']" appearing in the results set. 
	I had tried to append the list items into a new string: new_string = new_string + frequencies[item], but that crashed the PC due to runaway demand

getsql.py:
1)	This I'm reasonably happy with, but would like to replace with SQLAlchemy at some point.

textcleaner.py
1) yikes! this is fugly!

plotdata.py
1)	this is very bare, but that's for me to get to know plotmatlab better.

wordcount.py
This can be ignored as it's most of the above before I split the code into different functions
