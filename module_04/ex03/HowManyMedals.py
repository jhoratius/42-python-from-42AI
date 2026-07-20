import pandas as pd

def how_many_medals(df: pd.DataFrame, name: str):
    named_df = df[df['Name'] == name].copy()

    if named_df.empty:
        return {name : None}

    # Creating the Series
    # sr = pd.Series(['New York', 'Chicago', 'Toronto', None, 'Rio'])
    
    # sport_df = gender_year_df[gender_year_df['Sport'] == sport]

    # Create the Index
    # index_ = ['City 1', 'City 2', 'City 3', 'City 4', 'City_5']

    # set the index
    # sr.index = index_

    # Print the series
    # print(sr)
    
    return {name : None}