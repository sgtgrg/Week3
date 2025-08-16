import pandas as pd

class DatasetProcessor:
    def __init__(self):
        self.stats = {}

    def csv_to_parquet(self, csv_file, parquet_file):
        df = pd.read_csv(csv_file, sep=';')
        print(f"Loaded: {df.shape}, Columns: {list(df.columns)}")
        df.to_parquet(parquet_file, compression='snappy')
        print(f"Converted {csv_file} → {parquet_file}")
        return df

    def compute_stats(self, df):
        numeric_df = df.select_dtypes(include='number')
        self.stats = {
            col: {
                'max': numeric_df[col].max(),
                'min': numeric_df[col].min(),
                'average': numeric_df[col].mean(),
                'absolute_max': numeric_df[col].abs().max()
            }
            for col in numeric_df
        }
        return self.stats

    def display_stats(self):
        if not self.stats:
            print("No numeric data found.")
            return
        for metric in ["max", "min", "average", "absolute_max"]:
            print(f"\n{metric.capitalize()} values")
            print("-" * 60)
            for col, vals in self.stats.items():
                print(f"{col:20} {vals[metric]}")

    def process_dataset(self, csv_file, parquet_file=None):
        parquet_file = parquet_file or csv_file.replace('.csv', '.parquet')
        df = self.csv_to_parquet(csv_file, parquet_file)
        self.compute_stats(df)
        self.display_stats()
        return self.stats

if __name__ == "__main__":
    processor = DatasetProcessor()
    csv_file = "winequalitywhite.csv"
    try:
        processor.process_dataset(csv_file)
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_file}'. Place it in the same folder.")
