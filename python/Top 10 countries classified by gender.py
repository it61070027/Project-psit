""" Project Psit 
    suicide analysis
    top 10 suicide country
    """
import numpy, pandas, pygal, math
country = ['Brazil', 'France', 'Germany', 'Japan', 'Mexico', 'Poland', 'Republic of Korea', 'Russian Federation', 'Ukraine', 'United States of America']
df = pandas.read_csv('Top 10 country suicide.csv')
def sex_country():
    dt = numpy.array(df[['sex', 'country', 'suicides_no']]).tolist()
    dic_male = filter_sex('male', dt)
    dic_female = filter_sex('female', dt)
    treemap = pygal.Treemap()
    treemap.legend_at_bottom = True
    treemap.truncate_legend = 19
    treemap.legend_box_size = 16
    treemap.title = 'Top 10 most average suicide countries in 20 years classified by gender'
    treemap.add('Female', [{'value': dic_female[i], 'label': i} for i in dic_female])
    treemap.add('Male', [{'value': dic_male[i], 'label': i} for i in dic_male])
    treemap.render_to_file('Top 10 countries classified by gender.svg')
def filter_sex(sex, dt):
    dic = {}
    filter_sex = pandas.DataFrame(list(filter(lambda x:x[0] == sex, dt)),columns=['sex', 'country', 'suicides_no'])
    sum_contry_sex = numpy.array(filter_sex.groupby('country').sum()['suicides_no']).tolist()
    for i in range(len(sum_contry_sex)):
        dic[country[i]] = math.ceil(sum_contry_sex[i]/20)
    return dic
sex_country()