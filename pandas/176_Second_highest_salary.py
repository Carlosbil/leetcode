import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame 'employee' with a column 'salary', 
    this function returns a DataFrame with a single column 'SecondHighestSalary'
    containing the second highest salary. If there is only one unique salary 
    and more than one employee, it returns that salary.
    """
    # Sort salary without duplicated ones 
    sorted_unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    # Verify if there is more than one
    if len(sorted_unique_salaries) > 1:
        # Return the seconds highest
        return pd.DataFrame({'SecondHighestSalary': [sorted_unique_salaries.iloc[1]]})
    else:
        # None
        return pd.DataFrame({'SecondHighestSalary': [None]})

