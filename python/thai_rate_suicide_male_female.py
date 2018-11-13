""" Project Psit 
    suicide analysis
    thai suicide 
    female / male bar
    """
import pandas, numpy, pygal
from pygal.style import Style
def sum_sex():
    """ sum male / sum female number suicide thai 20 year """
    custom_style = Style(
    colors=('#0502c8', '#ef0200'))
    df = pandas.read_csv('thai_suicide.csv')
    data_female = list(filter(lambda x:x[0] == 'female',numpy.array(df[['sex', 'year', 'suicides_no']]).tolist()))
    data_male = list(filter(lambda x:x[0] == 'male',numpy.array(df[['sex', 'year', 'suicides_no']]).tolist()))
    data_female = pandas.DataFrame(data_female,columns=['sex', 'year', 'suicides_no'])
    data_male = pandas.DataFrame(data_male,columns=['sex', 'year', 'suicides_no'])
    data_female_sum_year = numpy.array(data_female.groupby('year').sum()['suicides_no']).tolist()
    data_male_sum_year = numpy.array(data_male.groupby('year').sum()['suicides_no']).tolist()
    chart = pygal.StackedBar(style=custom_style)
    chart.title = 'Thailand suicide  male and female rate in 20 years'
    chart.x_title = 'Year'
    chart.y_title = 'Number Of Suicides'
    chart.x_labels = map(str, range(1995, 2016))
    chart.legend_at_bottom = True
    chart.add('Male', data_male_sum_year)
    chart.add('Female', data_female_sum_year)
    chart.render_to_file('thai_rate_suicide_male_female.svg')
sum_sex()
