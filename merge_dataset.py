# scripts/merge_datasets.py

import pandas as pd
import os

def merge_fake_true(fake_file, true_file, output_file):
    # Load CSVs
    fake_df = pd.read_csv(fake_file)
    true_df = pd.read_csv(true_file)

    # Add labels
    fake_df["label"] = 0  # Fake
    true_df["label"] = 1  # True

    # Merge
    merged_df = pd.concat([fake_df, true_df], ignore_index=True)

    # Shuffle
    merged_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save to output
    merged_df.to_csv(output_file, index=False)
    print(f"✅ Dataset merged and saved to: {output_file}")

if __name__ == "__main__":
    # File paths (relative to this script)
    fake_path = os.path.join("..", "data", "Fake.csv")
    true_path = os.path.join("..", "data", "True.csv")
    output_path = os.path.join("..", "merged", "news.csv")

    merge_fake_true(fake_path, true_path, output_path)
