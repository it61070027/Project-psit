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
    data_female = list(filter(lambda x:x[0] == 'female',numpy.array(df[['sex', 'year', 'suicides_no', 'population']]).tolist()))
    data_male = list(filter(lambda x:x[0] == 'male',numpy.array(df[['sex', 'year', 'suicides_no', 'population']]).tolist()))
    data_female = pandas.DataFrame(data_female,columns=['sex', 'year', 'suicides_no', 'population'])
    data_male = pandas.DataFrame(data_male,columns=['sex', 'year', 'suicides_no', 'population'])
    data_female_sum_year = numpy.array(data_female.groupby('year').sum()['suicides_no']).tolist()
    data_male_sum_year = numpy.array(data_male.groupby('year').sum()['suicides_no']).tolist()
    data_male_population_sum_year = numpy.array(data_male.groupby('year').sum()['population']).tolist()
    data_female_population_sum_year = numpy.array(data_female.groupby('year').sum()['population']).tolist()
    rate_male = list()
    rate_female = list()
    for i in range(0, len(data_male_sum_year)):
        rate_male.append(data_male_sum_year[i]/data_male_population_sum_year[i]*100000)
        rate_female.append(data_female_sum_year[i]/data_female_population_sum_year[i]*100000)
        
    line_chart = pygal.HorizontalBar(print_labels=True, stack_from_top=False, style=custom_style)
    line_chart.title = 'Thailand suicide male and female rate in 20 years'
    line_chart.x_labels = map(str, range(1995, 2016))
    line_chart.y_labels = map(int, range(0, 16))
    line_chart.add('Male', rate_male)
    line_chart.add('Female', rate_female)
    line_chart.render_to_file('thai_rate_suicide_male_female.svg')
sum_sex()
