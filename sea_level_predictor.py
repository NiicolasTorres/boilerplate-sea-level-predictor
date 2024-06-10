import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line1_x = range(int(df['Year'].min()), 2051)  # Extend x-axis to 2050
    line1_y = slope * line1_x + intercept
    plt.plot(line1_x, line1_y, color='red', label='Best Fit Line 1')

    # Create second line of best fit using data from year 2000 onwards
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line2_x = range(2000, 2051)  # Extend x-axis to 2050
    line2_y = slope_recent * line2_x + intercept_recent
    plt.plot(line2_x, line2_y, color='green', label='Best Fit Line 2 (since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Configure x-axis ticks
    plt.xticks(range(1850, 2100, 25))

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()