import pandas as pd

def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
    gender_year_df = df[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates(subset='Name')

    if gender_year_df.empty:
        return 0.0

    sport_df = gender_year_df[gender_year_df['Sport'] == sport]
    print(f"{int(len(sport_df) / len(gender_year_df) * 100)}%")
    return len(sport_df) / len(gender_year_df)