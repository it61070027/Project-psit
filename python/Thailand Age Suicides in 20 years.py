""" Project Psit 
    suicide analysis
    thai suicide 
    age chart
    """
import pandas, numpy, pygal
def age():
    """ chart age/year """
    df = pandas.read_csv('thai_suicide.csv')
    data_age = sum_age_of_year(df)
    chart = pygal.Line()
    chart.legend_at_bottom = True
    chart.legend_box_size = 10
    chart.title = 'Thailand Age Suicides in 20 years'
    chart.x_title = 'Year'
    chart.y_title = 'Number Of Suicides'
    chart.x_labels = map(str, range(1995, 2016))
    dt_age = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']
    for i in range(len(dt_age)):
        chart.add(dt_age[i], [j[1] for j in data_age if j[0] == dt_age[i]])
    chart.render_to_file('thai_age_suicide_in_years.svg')


def sum_age_of_year(df):
    """ sum male female / age / year """
    data_age_femle = list(filter(lambda x:x[0] == 'female', numpy.array(df[['sex', 'age', 'suicides_no']]).tolist()))
    data_age_male = list(filter(lambda x:x[0] == 'male', numpy.array(df[['sex', 'age', 'suicides_no']]).tolist()))
    for i in range(len(data_age_femle)):
        data_age_femle[i][2] += data_age_male[i][2]
        data_age_femle[i].pop(0)
    return  data_age_femle
age()
