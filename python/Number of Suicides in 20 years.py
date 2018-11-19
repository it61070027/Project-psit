""" Project Psit 
    suicide analysis
    top 10 suicide
    thai suicide 
    """
import pandas, numpy, pygal
country_no = ['br', 'fr', 'de', 'jp', 'mx', 'pl','kr', 'ru', 'ua', 'us']
df_thai = pandas.read_csv('thai_suicide.csv')
df_top = pandas.read_csv('Top 10 country suicide.csv')

def sum_country():
    """ sum number suicide thai 20 year and Top coountry """
    dic = {}
    data_thai = numpy.array(df_thai.groupby('country').sum()['suicides_no']).tolist()
    dic['th'] = data_thai[0]
    data_country = numpy.array(df_top.groupby('country').sum()['suicides_no']).tolist()
    for i in range(len(data_country)):
        dic[country_no[i]] = data_country[i]
    chart = pygal.maps.world.World()
    chart.title = 'Top 10 Country and Thailand most Suicides in 20 years'
    chart.legend_at_bottom = True
    chart.add('Number of Suicides in 20 years', dic)
    chart.render_to_file('Number of Suicides in 20 years.svg')
sum_country()

