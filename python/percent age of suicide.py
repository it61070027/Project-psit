""" Project Psit 
    suicide analysis
    suicide age / people age
    """
import pandas, numpy, pygal
df = pandas.read_csv('thai_suicide.csv')
def age():
    dt_age = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']
    dic = {}
    data_age = numpy.array(df.groupby('age').sum()[['suicides_no', 'population']]).tolist()
    for i in range(len(data_age)):
        dic[dt_age[i]] = ((data_age[i][0]/20)*100)/(data_age[i][1]/20)
    chart = pygal.HorizontalBar()
    chart.title = 'Browser usage in February 2012 (in %)'
    chart.legend_at_bottom = True
    chart.x_title = 'Percent of Suicides'
    chart.y_title = 'Age'
    percent_formatter = lambda x: '{:.3g}%'.format(x)
    chart.value_formatter = percent_formatter
    chart.add('5-14 years', dic['5-14 years'])
    dic.pop('5-14 years')
    for j in dic:
        chart.add(j, dic[j])
    chart.render_to_file('percent age of suicide.svg')

age()
