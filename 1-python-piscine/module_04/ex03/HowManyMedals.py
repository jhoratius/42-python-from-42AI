import pandas as pd

def how_many_medals(df: pd.DataFrame, name: str) -> dict:

    athlete_df = df[df['Name'] == name]

    if athlete_df.empty:
        return {}
    medals_by_year = {}

    for year, group in athlete_df.groupby('Year'):
        
        gold = (group['Medal'] == 'Gold').sum()
        silver = (group['Medal'] == 'Silver').sum()
        bronze = (group['Medal'] == 'Bronze').sum()

        medals_by_year[int(year)] = {
            'G': int(gold),
            'S': int(silver),
            'B': int(bronze)
        }

    years = list(medals_by_year.keys())
    for i, year in enumerate(years):
        print(f"{year}: {medals_by_year[year]}")

    return medals_by_year