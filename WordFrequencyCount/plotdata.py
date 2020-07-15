import numpy as np
import datetime
from matplotlib import pyplot as plt


def barplotter(finished_data, bins,name):
    """
    This function plots the results of word counts and exports the bar chart as a png object with timestamp to hard coded location
    Parameters:
    finished_data       - list of tuples containing words and their frequency counts
    bins                - An integer giving the number of columns
    name                - A string given the name of type of dataset being presented
    
    Returns:
    A bar chart as a png object with a timestamp to a hard coded location
    
    """

    abc = range(len(finished_data))

    print(f"\n beginning plotting {name} .....\n")
    plt.bar(abc,[val[1] for val in finished_data],align='center')
    plt.xticks(abc,[val[0] for val in finished_data])
    plt.xticks(rotation= 70)
    plt.title(f"Top {bins} words referenced for on a {name} day query")
    plt.xlabel(f"Top words referred to on a {name} day")
    plt.ylabel("number of references")
  
    t = datetime.datetime.now().strftime("%d %b %Y %H %M")

    plt.savefig(f"C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\A {name} day prepared on {t}.png")
    #plt.show()
    #plt.savefig('C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\test.png')
  

