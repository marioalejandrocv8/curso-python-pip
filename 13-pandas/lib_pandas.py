import charts
import pandas 

def pandas_csv(path):
    dataframes = pandas.read_csv(path)
    dataframes = dataframes[dataframes['Continent'] == 'Africa']
    countries = dataframes['Country'].values
    percentages = dataframes['World Population Percentage'].values
    charts.generate_pie_chart(countries,percentages)