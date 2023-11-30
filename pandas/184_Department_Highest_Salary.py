import pandas as pd


"""
When two DataFrames are merged using pd.merge() in pandas, if there are columns with the same name in both DataFrames, pandas automatically appends suffixes _x and _y to distinguish them. In the context of your DataFrames:

name_x comes from the employee DataFrame, representing the original name column in this DataFrame.
name_y comes from the department DataFrame, representing the original name column in this DataFrame.
    # also could be done with:
    # merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left', suffixes=('_employee', '_department'))
    # in order to let more clear the columns after the merge
"""
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # merge both dataframe saving employee, dept
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')

    # serach highest salaries by dept
    max_salaries = merged_df.groupby('name_y')['salary'].transform(max)

    # select the rows
    highest_paid = merged_df[merged_df['salary'] == max_salaries]

    # select and rename columns 
    result = highest_paid[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

    # delete posible duplicates 
    result = result.drop_duplicates()

    return result
