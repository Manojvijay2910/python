import pandas_demo as pd

reviews = pd.Series([4.6, 4.4, 4.8, 5])
print(reviews, type(reviews))
print(reviews.describe())
print(reviews[0])

print(reviews.count())
print(reviews.mean())
print(reviews.min())
print(reviews.max())
print(reviews.median())
print(reviews.std())

reviews = pd.Series([4.6, 4.4, 4.8, 5], index = ["Python", "Java", "Angular", "MySql"])
print(reviews)

reviews = pd.Series({"Python": 4.6, "Java": 4.4, "Angular": 4.8, "MySql": 5})
print(reviews)
print(reviews["Python"])
print(reviews.Java)
print(reviews.values)
print(reviews.index)

courses = pd.Series(['java', 'python', 'aws'])
print(courses)
print(courses.str.upper())
print(courses.str.contains('y'))