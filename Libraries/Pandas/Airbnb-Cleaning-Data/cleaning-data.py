import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent
data = pd.read_csv(BASE / 'archive (1)\\Airbnb_Open_Data.csv')

#^CHECK ALL THE COLUMNS:
print(data.columns)