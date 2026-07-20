import pandas as pd

def youngest_fellah(df: pd.DataFrame, year: int):
    year_df = df[(df['Year'] == year)].copy()

    if year_df.empty:
        return {'m': None, 'f': None}

    # On nettoie la colonne Age pour être sûr de pouvoir faire un .min()
    year_df['Age'] = pd.to_numeric(year_df['Age'], errors='coerce')

    m_df = year_df[year_df['Sex'] == 'M']
    min_m = m_df['Age'].min()

    f_df = year_df[year_df['Sex'] == 'F']
    min_f = m_df['Age'].min()

    result = {
        'm' : min_m,
        'f' : min_f
    }

    return result