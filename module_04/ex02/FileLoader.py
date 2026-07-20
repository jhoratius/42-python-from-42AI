import pandas as pd

class FileLoader:
    def __str__(self):
        """Load and display pandas dataframes"""
        return "Load and display pandas dataframes"

    def load(self, path):
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df

    def display(self, df, n):
        if n >= 0:
            new_df = df.head(n)
        else:
            new_df = df.tail(abs(n))
        return new_df
