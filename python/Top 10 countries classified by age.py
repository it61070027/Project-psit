""" Project Psit 
    suicide analysis
    top 10 suicide country
    age
    """
import numpy, pandas, pygal, math
from pygal.style import Style
country = ['Brazil', 'France', 'Germany', 'Japan', 'Mexico', 'Poland', 'Republic of Korea', 'Russian Federation', 'Ukraine', 'United States of America']
dt_age = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
df = pandas.read_csv('Top 10 country suicide.csv')
def chart_c():
    """ make chart """
    custom_style = Style(plot_background='#d4d3d6' ,background='#e6f4f6') #ตกแต่งกราฟ
    chart = pygal.StackedLine(fill=True, interpolate='cubic', dots_size=1.5, style=custom_style)
    chart.legend_at_bottom = True
    chart.title = 'Top 10 countries most of suicides number classified by age'
    chart.x_labels = dt_age
    chart.x_title = 'Age'
    chart.y_title = 'Averange Number Of Suicides in 20 years'
    for i in country:
        chart.add(i, [{'value': j[1], 'label': j[0]} for j in list(sum_age(i).items())])
    chart.render_to_file('Top 10 countries classified by age.svg')

def sum_age(text):
    """ funtion make a sum age / country """
    dic = {}
    df_age = pandas.DataFrame(list(filter(lambda x:x[1] == text, numpy.array(df[['age', 'country', 'suicides_no']]))),\
        columns=['age', 'country', 'suicides_no'])
    sum_age_country = numpy.array(df_age.groupby('age').sum()['suicides_no']).tolist()
    dic['5-14 years'] = math.ceil(sum_age_country[3]/20)
    sum_age_country.pop(3)
    for i in range(len(sum_age_country)):
        dic[dt_age[i+1]] = math.ceil(sum_age_country[i]/20)
    return dic

chart_c()
