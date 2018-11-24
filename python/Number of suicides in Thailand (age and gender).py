""" Project Psit 
    suicide analysis
    suicide age and sex in 20 years
    """
import pandas, numpy, pygal, math
from pygal.style import Style
df = pandas.read_csv('thai_suicide.csv')
dt_age = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']
dt_age2 = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
def main():
    """ age suicides """
    custom_style = Style(
    colors=('#302fff', '#ff2f31'))
    dt_sex = numpy.array(df[['sex', 'age', 'suicides_no']]).tolist()
    female_data = list(filter(lambda x:x[0] == 'female', dt_sex))
    male_data = list(filter(lambda x:x[0] == 'male', dt_sex))
    dic_age_female = sum_age(female_data)
    dic_age_male = sum_age(male_data)
    chart = pygal.StackedBar(style=custom_style)
    chart.title = 'Number of suicides in Thailand classified by age and gender (20 years)'
    chart.x_labels = dt_age2
    chart.legend_box_size = 16
    chart.legend_at_bottom = True
    chart.x_title = 'Age'
    chart.y_title = 'Number Of Suicides'
    chart.add('Male', [dic_age_male[i] for i in dt_age2])
    chart.add('Female',[dic_age_female[i] for i in dt_age2])
    chart.render_to_file('Number of suicides in Thailand (age and gender).svg')
def sum_age(data):
    dic = {}
    df_new = pandas.DataFrame(data,columns=['sex', 'age', 'suicides_no'])
    dt_new = numpy.array(df_new.groupby('age').sum()['suicides_no']).tolist()
    for i in range(len(dt_new)):
        dic[dt_age[i]] = math.ceil(dt_new[i]/20)
    return dic
main()
