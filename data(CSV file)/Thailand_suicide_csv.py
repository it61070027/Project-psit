""" Project Psit 
    suicide analysis
    filter thailand"""
import pandas, numpy, pygal
df = pandas.read_csv('who_suicide_statistics.csv')
df = df[(df['country'] == 'Thailand')]
df.to_csv('thai_suicide.csv', index=False)