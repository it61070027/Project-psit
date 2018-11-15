""" Project Psit 
    suicide analysis
    thai suicide 
    """
import pandas, numpy, pygal
from pygal.style import Style
def sum_thai():
    """ sum number suicide thai 20 year """
    custom_style = Style(colors=('#ff0000', '#0000fe'))
    df = pandas.read_csv('thai_suicide.csv')
    data = numpy.array(df.groupby('sex').sum()['suicides_no']).tolist()
    dt_sex = ['female', 'male']
    chart = pygal.Pie(style=custom_style)
    chart.title = 'Thailand\'s sex of suicide in 20 years'
    for i in range(len(dt_sex)):
        print(dt_sex[i])
        chart.add(dt_sex[i], [{'value': data[i], 'label':'{:.2f}%'.format((data[i]*100)/sum(data))}])
    chart.legend_at_bottom = True
    chart.render_to_file('thai_rate_suicide_sex.svg')
    
sum_thai()
