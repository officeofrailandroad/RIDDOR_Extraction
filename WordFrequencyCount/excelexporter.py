from pandas import ExcelWriter

def excelexport(df, filename, sheet):
    """
    This function exports a dataframe to excel at a hard-coded location
    Parameters:
    df          - a pandas dataframe containing data
    file name   - a string specifying the name of the excel workbook
    sheet       - a string specifying the name of the sheet in the excel workbook

    Returns:
    An excel workbook to the hard coded location
    """
    
    writer = ExcelWriter(f"C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\{filename}")
    df.to_excel(writer,sheet)
    writer.save()

    return f"C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\{filename}"


