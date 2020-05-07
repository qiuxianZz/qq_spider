import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# data.describe()
# data.profile_report(title='Titanic Dataset')
profile = data.profile_report(title='Titanic Dataset')
profile.to_file(output_file='result/titanic_report.html')
