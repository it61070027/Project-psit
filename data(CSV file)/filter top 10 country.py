""" Project Psit
    filter Top 10 Worldwide Suicide in 20 Years
    and save to csv
    """
import numpy, pandas
df = pandas.read_csv('who_suicide_statistics.csv')
def world_wide():
    """ world wide suicide """
    dic = world_dic(numpy.array(df[['country', 'suicides_no']]).tolist())
    top_10_country = [dic[i][0] for i in range(10)]
    data_country = list(filter(lambda x:x[0] in top_10_country ,numpy.array(df[['country', 'year', 'sex', 'age', 'suicides_no', 'population']]).tolist()))
    data_country = pandas.DataFrame(data_country,columns=['country', 'year', 'sex', 'age', 'suicides_no', 'population'])
    data_country.to_csv('Top 10 country suicide.csv', index=False)

def world_dic(data):
    """ save in dic """
    dic = {}
    for i in data:
        if numpy.isnan(i[1]):
            i[1] = 0
        if i[0] in dic:
            dic[i[0]] += i[1]
        else:
            dic[i[0]] = i[1]
    return sorted(dic.items(), key=lambda x:x[1], reverse=True)
world_wide()



