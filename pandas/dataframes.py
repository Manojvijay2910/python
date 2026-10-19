import pandas as pd

scores_dict = {'Kohli': [100, 50, 70], 'Rohit': [100, 88, 0],
               'Surya': [77, 110, 0], 'Jadeja': [99, 120, 8]}

scores = pd.DataFrame(scores_dict)
scores.index = ['I1', 'I2', 'I3']
print(scores)

print(scores.Kohli)

print(scores.loc['I1'])
print(scores.iloc[1])

print(scores.loc['I1': 'I2'])
print(scores.iloc[0: 2])

print(scores.loc[['I1', 'I3']])
print(scores.iloc[[0, 1]])

print(scores.loc['I1': 'I2', ['Kohli', 'Jadeja']])

print(scores[scores >= 90])
print(scores[(scores >= 80) & (scores <= 90)])

print(scores.at['I2', 'Kohli'])

scores.at['I2', 'Kohli'] = 150
print(scores.at['I2', 'Kohli'])

print(scores)
print(scores.mean())
pd.set_option('display.precision', 2)
print(scores.describe())

print(scores.T)

print(scores.sort_index(ascending=False))
print(scores.sort_index(axis = 1))

print(scores.sort_values(by = 'I1' ,axis = 1))