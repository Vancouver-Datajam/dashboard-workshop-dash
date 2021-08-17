import pandas as pd
# ----------------------------- functions for data preparation ------------------------------------------
def data_prep(data_file):
    #Reading the data and making a copy
    df = pd.read_excel(data_file)
    temp = df.copy()

    #Removing empty rows
    temp.dropna(thresh=3, inplace=True)

    #Reseting columns - Changing the column names using the values in the 1st row
    temp_header = temp.iloc[0,]
    temp = temp[1:]
    temp.columns = temp_header

    #Removing all columns whose names are nan
    temp = temp.loc[:, temp.columns.notnull()]

    #Ensuring the indices go from 0 without skipping any number
    temp.reset_index(inplace=True, drop = True)

    #Categorize Geography as Country, Province, and City
    temp['Region/City'] = ""
    temp['Region/City'][temp.index ==0] = 'Country'
    temp['Region/City'][(temp.index < 11) & (temp.index >0)] = 'Province'
    temp['Region/City'][temp.index >= 11] = 'City'

    #Rearrange columns -- bring column 'Region/City' to the 1st column position
    # Access columns
    cols = temp.columns.tolist()
    # Bring last col to front
    cols = cols[-1:] + cols[:-1]
    # Set new column order
    temp = temp[cols] 

    #Converting data type to the right format
    #Isolating yearly and quarterly columns and convert to numeric.
    int_cols = temp.columns.drop(['Region/City', 'Geography'])
    temp[int_cols] = temp[int_cols].apply(pd.to_numeric, errors='coerce')

    return temp



def slice_data(df, level):
    """
    df: data frame with mortgage data
    level: "Province" or "City"
    Extract a subset of df based on level
    Return a dataframe
    """
    try:
        temp = df[df['Region/City']==level]
        temp = pd.melt(temp, id_vars='Geography', value_vars=temp.columns[2:])
        temp.rename(columns = {3:'Time'}, inplace = True)
        return temp
    except KeyError:
        print("Key not found. Make sure that 'level' is in ['Province','City']")

        
    
def combine_data(df_mortgage, df_income):
    mortgage = df_mortgage.copy()
    income = df_income.copy()
    
    # change the name of 2 provinces to make the provinces match in 2 datasets
    income_replace = {'Newfoundland and Labrador': 'Newfoundland', 'Quebec':'Québec'}
    income.replace(income_replace, inplace=True)
    
    # create yearly data for mortgage for some years
    select_year = df_income.columns.tolist()
    select_year = select_year[select_year.index(2013.0):]
    select_year = [str(int(y)) for y in select_year]

    # average over 4 quarters to get the yearly value
    q = ['Q1', 'Q2', 'Q3', 'Q4']
    for y in select_year:
        y1 = [y+j for j in q]
        mortgage[y] = mortgage[y1].mean(axis=1)
    
    # select columns in mortgage data
    col_mortgage = ['Region/City', 'Geography']+select_year
    mortgage13_18 = mortgage[col_mortgage]
    col_income = ['Region/City', 'Geography']+[float(y) for y in select_year]
    mortgage13_18.columns = col_income

    income13_18 = income[col_income]
    mortgage13_18['Type'] = 'Mortgage'
    income13_18['Type'] = 'Income'

    df13_18 = pd.concat([mortgage13_18, income13_18])

    df13_18.reset_index(inplace=True, drop=True)
    df_province = df13_18[df13_18['Region/City']=='Province']

    pivot_income_province = df_province.pivot_table(columns=["Type", "Geography"])
    
    return pivot_income_province