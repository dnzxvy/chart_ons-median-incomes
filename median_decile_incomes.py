import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#load excel file

file_path = 'hdiifye2023.xlsx'

sheet_name = 'Table 3'

median_equivalised_data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5, header=0)

median_equivalised_data.columns = median_equivalised_data.columns.str.strip()

print("Cleaned Columns in the DataFrame:", median_equivalised_data.columns)

# Display the first few rows of the DataFrame
print(median_equivalised_data.head())



if 'Year' in median_equivalised_data.columns:
    numeric_columns = ['2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
    for col in numeric_columns:
        median_equivalised_data[col] = pd.to_numeric(median_equivalised_data[col], errors='coerce')

        year = median_equivalised_data['Year'].astype(str).tolist()

        df = pd.DataFrame(median_equivalised_data)




    plt.figure(figsize=(10, 7))
    for quintile in numeric_columns:
        plt.plot(year, median_equivalised_data[quintile], marker='o', label=quintile)

    plt.title(
        'Timeseries of decile points of median equivalised disposable household income, 1977-2022/23, UK (2022/23 prices)')
    plt.xlabel('Year')
    plt.ylabel(' decile points of median equivalised disposable household income')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    plt.show()
    #plt.savefig('figure2_median_decile_incomes.png')  # save as an image file
    plt.close()



else:
    print("Column 'Year' not found in the DataFrame.")