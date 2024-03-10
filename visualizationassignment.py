import pandas as pd
import matplotlib.pyplot as plt


# Loading the data
ukweather = pd.read_csv('chart-data.csv')

# Renaming the unnamed column
ukweather.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
ukweather.sort_values(by='Year', inplace=True)
print(ukweather)
print(ukweather.describe())


# LINE PLOT (plot no.1)
def plot_temperature_trends(ukweather):
    '''Creates a line plot for the temperature trends by regions(UK, England,
        Northern Ireland, Scotland and Wales)'''
    plt.figure(figsize=(10, 6))

    # Plotting the data
    plt.plot(ukweather['Year'], ukweather['UK'], label='UK')
    plt.plot(ukweather['Year'], ukweather['England'], label='England')
    plt.plot(ukweather['Year'], ukweather['Northern Ireland'],
             label='Northern Ireland')
    plt.plot(ukweather['Year'], ukweather['Scotland'], label='Scotland')
    plt.plot(ukweather['Year'], ukweather['Wales'], label='Wales')

    # Adding labels
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends by Region (1884-2022)')

    plt.grid(True)
    plt.xlim(1883, 2022)
    plt.legend()

    plt.savefig('Temperature-trends-by-regions-lineplot.png')
    plt.show()


# HISTOGRAM (plot no.2)
def plot_temperature_histograms(ukweather):
    '''Creates a histogram for the weather data for comparison between
    1961 to 1990 vs 1991 to 2020'''
    # Extract temperature data for the time periods
    data_1961_to_1990 = ukweather.loc[(ukweather['Year'] >= 1961) &
                                      (ukweather['Year'] <= 1990), 'UK']
    data_1991_to_2020 = ukweather.loc[(ukweather['Year'] >= 1991) &
                                      (ukweather['Year'] <= 2020), 'UK']

    # Plotting histograms
    plt.figure(figsize=(10, 6))

    plt.hist(data_1961_to_1990, bins=30, label='1961 to 1990', alpha=0.7)
    plt.hist(data_1991_to_2020, bins=30, label='1991 to 2020', alpha=0.7)

    # Adding labels and title
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Temperature Distribution Comparison (1961-1990 vs 1991-2020)')
    plt.grid(True)
    plt.legend()

    plt.savefig('Temperature-distribution-comparison-histogram.png')
    plt.show()


# BOXPLOT (plot no.3)
def plot_temperature_boxplots(ukweather):
    '''Creates a boxplot for temperature distribution for all five regions'''
    ukweather = ukweather.drop(columns=['Year'])
    ukweather.drop(columns=['1961 to 1990 long-term average'], inplace=True)
    ukweather.drop(columns=['1991 to 2020 long-term average'], inplace=True)

    # Create box plots
    plt.figure(figsize=(10, 6))
    ukweather.boxplot()
    plt.title('Temperature Distribution for Different Regions')
    plt.xlabel('Region')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.savefig('Temperature-distribution-of-different-regions.png')
    plt.show()


plot_temperature_trends(ukweather)
plot_temperature_histograms(ukweather)
plot_temperature_boxplots(ukweather)