""" Project Psit 
    suicide analysis
    thai suicide 
    """
import pandas, numpy, pygal
def sum_thai():
    """ sum number suicide thai 20 year """
    df = pandas.read_csv('thai_suicide.csv')
    data = numpy.array(df.groupby('year').sum()[['suicides_no', 'population']]).tolist()
    chart = pygal.Line()
    chart.title = 'Thailand suicide rate in 20 years'
    chart.x_labels = map(str, range(1995, 2016))
    chart.legend_at_bottom = True
    chart.add('Thai Suicide', [i[0] for i in data])
    chart.render_to_file('thai_rate_suicide.svg')


sum_thai()

