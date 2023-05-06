import pandas as pd
data = pd.read_excel('semester2\lesson2\Grades.xlsx', usecols=['Subject', 'Grade'])
print(data)