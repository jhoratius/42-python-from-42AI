from FileLoader import FileLoader

fl = FileLoader()

# Load the dataset
df = fl.load("data.csv")
print(f"\n{df.head()}\n")

if df is not None:
    # This shows the top rows of the dataset to prove it loaded perfectly
    print(fl.display(df, -2))
else:
    print("Failed to load dataset.")
