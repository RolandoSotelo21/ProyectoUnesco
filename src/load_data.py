
import pandas as pd


def load_dataset(file_path):

    print("[INFO] Loading dataset...")

    try:

        df = pd.read_csv(file_path)

        print(f"[SUCCESS] Dataset loaded: {df.shape}")

        return df

    except Exception as e:

        print(f"[ERROR] Failed loading dataset: {e}")

        raise