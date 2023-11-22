import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if 'num' not in logs.columns or logs.empty:
        return pd.DataFrame(columns=['ConsecutiveNums'])

    # Group by consecutive identical numbers and count occurrences
    grouped = logs['num'].groupby((logs['num'] != logs['num'].shift()).cumsum()).value_counts()

    # Filter groups where the count is 3
    result = grouped[grouped == 3].reset_index(level=1)['num']

    return pd.DataFrame({"ConsecutiveNums": result.unique()})
