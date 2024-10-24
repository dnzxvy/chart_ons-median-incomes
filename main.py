import pandas as pd
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'hdiifye2023.xlsx'

#
sheet_name = 'Table 2'


median_income_data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5, header=0)

#clean the column names by stripping whitespace
median_income_data.columns = median_income_data.columns.str.strip()

print("Cleaned Columns in the DataFrame:", median_income_data.columns)

# Display the first few rows of the DataFrame
print(median_income_data.head())


print("Columns in the DataFrame:", median_income_data.columns)

if 'Year' in median_income_data.columns:
    numeric_columns = ['Bottom', '2nd', '3rd', '4th', 'Top']
    for col in numeric_columns:
        median_income_data[col] = pd.to_numeric(median_income_data[col], errors='coerce')



    year = median_income_data['Year'].astype(str).tolist()
   #.astype() changes the data type to in this case a string


    print(year)


    df = pd.DataFrame(median_income_data)

    plt.figure(figsize=(10, 7))
    for quintile in numeric_columns:
        plt.plot(year, median_income_data[quintile], marker='o', label=quintile)

    plt.title('Timeseries of Median Equivalised Disposable Household Income of Individuals by Income Quintile, 1977-2022/23, UK (2022/23 Prices)')
    plt.xlabel('Year')
    plt.ylabel('Median Equivalised Disposable Household Income of Individuals')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()




    #plt.show()
    plt.savefig('figure1_median_income_plot.png')  #save as an image file
    plt.close()
    print(median_income_data['Bottom'])


else:
    print("Column 'Year' not found in the DataFrame.")