import pandas as pd
import os
from datetime import datetime

LABELS_FILE = "labels.csv"

def load_csv(file):
    """Loads a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file)
        # Ensure required columns exist
        required_columns = ["question", "response_a", "response_b"]
        if not all(col in df.columns for col in required_columns):
            return None, f"CSV must contain columns: {', '.join(required_columns)}"
        return df, None
    except Exception as e:
        return None, str(e)

def save_label(question, response_a, response_b, preferred, note=""):
    """Appends a labeling result to the labels CSV file."""
    label_data = {
        "question": [question],
        "response_a": [response_a],
        "response_b": [response_b],
        "preferred": [preferred],
        "note": [note],
        "timestamp": [datetime.now().isoformat()]
    }
    df = pd.DataFrame(label_data)
    
    if not os.path.exists(LABELS_FILE):
        df.to_csv(LABELS_FILE, index=False)
    else:
        df.to_csv(LABELS_FILE, mode='a', header=False, index=False)

def get_progress(total_rows):
    """Returns the number of labeled items and basic stats."""
    if not os.path.exists(LABELS_FILE):
        return 0, {}
    
    try:
        df = pd.read_csv(LABELS_FILE)
        count = len(df)
        stats = df['preferred'].value_counts().to_dict()
        return count, stats
    except pd.errors.EmptyDataError:
         return 0, {}
    except Exception:
        return 0, {}
