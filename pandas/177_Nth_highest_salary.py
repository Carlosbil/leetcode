import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    Given a DataFrame 'employee' with a column 'salary', it will return the Nth highest salary.
    this function returns a DataFrame with a single column 'getNthHighestSalary(N)'
    """
    # Sort salary without duplicated ones 
    sorted_unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    # Verify if there is more salaries than the nth greater
    if len(sorted_unique_salaries) >= N:
        # Return the seconds highest
        return pd.DataFrame({f'getNthHighestSalary({N})': [sorted_unique_salaries.iloc[N-1]]})
    else:
        # None
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})