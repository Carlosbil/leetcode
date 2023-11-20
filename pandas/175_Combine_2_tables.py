import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Combine dataframes
    result_df = pd.merge(person, address, on='personId', how='left', suffixes=('', '_address'))

    # Select the columns that it is needed
    result_df = result_df[['firstName', 'lastName', 'city', 'state']]
    return result_df