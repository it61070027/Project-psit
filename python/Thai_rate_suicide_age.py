""" project psit
    suicide analysis
    age suicide """
import pandas, numpy, pygal
def age():
    df = pandas.read_csv('thai_suicide.csv')
    data_age = numpy.array(df.groupby('age').sum()['suicides_no']).tolist()
    dt_age = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']
    color = ['rgba(252, 74, 0)', 'rgba(210, 5, 36)', 'rgba(36, 89, 236)', 'rgba(212, 2, 230)','rgba(4, 190, 92)','rgba(255, 203, 0)']
    chart = pygal.Pie()
    chart.title = 'Thailand Suicides rate in 20 years (Age)'
    for i in range(len(dt_age)):
        chart.add(dt_age[i], [{'value': data_age[i], 'label':'{:.2f}%'.format((data_age[i]*100)/sum(data_age)), 'color': color[i]}])
    chart.legend_at_bottom = True
    chart.render_to_file('thai_rate_suicide_age.svg')
age()