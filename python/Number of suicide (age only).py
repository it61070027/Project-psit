""" project psit
    suicide analysis
    age suicide """
import pandas, numpy, pygal
from pygal.style import Style
def age():
    custom_style = Style(colors=('#ff0000', '#0000fe','#ff0081', '#1ac3f8', '#61b700', '#ffb700'))
    df = pandas.read_csv('thai_suicide.csv')
    data_age = numpy.array(df.groupby('age').sum()['suicides_no']).tolist()
    dt_age = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']
    chart = pygal.Pie(style=custom_style)
    chart.title = 'Number of suicide in Thailand classified by age'
    for i in range(len(dt_age)):
        chart.add(dt_age[i], [{'value': data_age[i], 'label':'{:.2f}%'.format((data_age[i]*100)/sum(data_age))}])
    chart.legend_at_bottom = True
    chart.render_to_file('Number of suicide (age only).svg')
age()
