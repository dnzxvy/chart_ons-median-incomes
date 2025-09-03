import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'hdiifye2023.xlsx'


# LOAD TABLE 2 (Quintiles)

sheet_name = 'Table 2'
median_income_data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5, header=0)

# Clean the column names
median_income_data.columns = median_income_data.columns.str.strip()

print("\nCleaned Columns in Table 2:", median_income_data.columns)
print(median_income_data.head())

if 'Year' in median_income_data.columns:
    numeric_columns = ['Bottom', '2nd', '3rd', '4th', 'Top']
    for col in numeric_columns:
        median_income_data[col] = pd.to_numeric(median_income_data[col], errors='coerce')

    # Convert Year to string (first 4 characters)
    year_quintiles = median_income_data['Year'].astype(str).str[:4]

    df_quintiles = pd.DataFrame(median_income_data)
else:
    print("Column 'Year' not found in Table 2.")

# ==============================
# LOAD TABLE 3 (Deciles)
sheet_name = 'Table 3'
median_equivalised_data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5, header=0)

median_equivalised_data.columns = median_equivalised_data.columns.str.strip()

print("\nCleaned Columns in Table 3:", median_equivalised_data.columns)
print(median_equivalised_data.head())

if 'Year' in median_equivalised_data.columns:
    numeric_columns = ['2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
    for col in numeric_columns:
        median_equivalised_data[col] = pd.to_numeric(median_equivalised_data[col], errors='coerce')

    year_deciles = median_equivalised_data['Year'].astype(str).str[:4]

    df_deciles = pd.DataFrame(median_equivalised_data)
else:
    print("Column 'Year' not found in Table 3.")

# ==============================
# Displaying both dataframes

print("\nQuintiles DataFrame:")
print(df_quintiles.head())

print("\nDeciles DataFrame:")
print(df_deciles.head())

# ==============================
# Plotting both tables

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,6))
fig.tight_layout(pad=3.0)

# First subplot
for col in ['Bottom', '2nd', '3rd', '4th', 'Top']:
    axes[0].plot(year_quintiles, df_quintiles[col], marker='o', label=col)
axes[0].set_title('Median Household Income by Quintile (1977–2022/23)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Income (£)')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True)
axes[0].legend()

# Second subplot
for col in ['2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']:
    axes[1].plot(year_deciles, df_deciles[col], marker='o', label=col)
axes[1].set_title('Median Household Income by Decile (1977–2022/23)')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Income (£)')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True)
axes[1].legend()

plt.show()

# # ==============================
# Analysis Functions to provide insight

# Quintiles Analysis
print("\nQuintile Analysis")

# Income Gap (Top - Bottom)
df_quintiles['Income_Gap'] = df_quintiles['Top'] - df_quintiles[
    'Bottom']

# Income Ratio (Top / Bottom)
df_quintiles['Income_ratio'] = df_quintiles['Top'] / df_quintiles[
    'Bottom']
# Growth Rate (Year-on-Year %) for each quintile
growth_quintiles = df_quintiles[['Bottom', '2nd', '3rd', '4th', 'Top']].pct_change(fill_method=None) * 100

# # ==============================
# Deciles Analysis
print("\nDeciles Analysis")

# Income Gap (Top - Bottom)
df_deciles['Income_Gap'] = df_deciles['2nd'] - df_deciles[
    '10th']

# Income Ratio (Top / Bottom)
df_deciles['Income_ratio'] = df_deciles['2nd'] / df_deciles[
    '10th']

# Growth Rate (Year-on-Year %) for each decile
growth_deciles = df_deciles[['2nd','3rd','4th','5th',
'6th','7th','8th','9th','10th']].pct_change(fill_method=None) * 100


# Print first 5 rows of quintiles with Income Gap and Ratio
print("\n--- Quintiles Analysis ---")
print(df_quintiles[['Year', 'Bottom', '2nd', '3rd', '4th', 'Top', 'Income_Gap', 'Income_ratio']].round(2).head())

# Print Year-on-Year Growth Rates for quintiles
print("\nYear-on-Year Growth Rate (%) for Quintiles:")
print(growth_quintiles.round(2).head())

# Print first 5 rows of deciles with Income Gap and Ratio
print("\n--- Deciles Analysis ---")
print(df_deciles[['Year','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','Income_Gap','Income_ratio']].round(2).head())

# Print Year-on-Year Growth Rates for deciles
print("\nYear-on-Year Growth Rate (%) for Deciles:")
print(growth_deciles.round(2).head())

# # ==============================
# Plotting the Quintile & Decile Analysis


df_quintiles['Year_numeric'] = pd.to_numeric(df_quintiles['Year'].str[:4], errors='coerce')
df_deciles['Year_numeric'] = pd.to_numeric(df_deciles['Year'].str[:4], errors='coerce')

# Plot Income Gap


plt.figure(figsize=(12,6))
plt.plot(df_quintiles['Year_numeric'], df_quintiles['Income_Gap'], marker='o', label='Quintiles Gap')
plt.plot(df_deciles['Year_numeric'], df_deciles['Income_Gap'], marker='s', label='Deciles Gap')
plt.title('Income Gap Over Time (Top - Bottom)')
plt.xlabel('Year')
plt.ylabel('Income Gap (£)')
plt.grid(True)
plt.legend()
plt.show()

# Plot Income Ratio

plt.figure(figsize=(12,6))
plt.plot(df_quintiles['Year_numeric'], df_quintiles['Income_ratio'], marker='o', label='Quintiles Ratio')
plt.plot(df_deciles['Year_numeric'], df_deciles['Income_ratio'], marker='s', label='Deciles Ratio')
plt.title('Income Ratio Over Time (Top / Bottom)')
plt.xlabel('Year')
plt.ylabel('Income Ratio')
#plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()


import pandas as pd

# --- Quintiles Analysis Table ---
df_quintiles['Gap_Growth_%'] = df_quintiles['Income_Gap'].pct_change(fill_method=None) * 100
df_quintiles['Ratio_Change_%'] = df_quintiles['Income_ratio'].pct_change(fill_method=None) * 100

quintiles_table = df_quintiles[['Year', 'Bottom', 'Top', 'Income_Gap', 'Income_ratio', 'Gap_Growth_%', 'Ratio_Change_%']].round(2)

# Export to Excel
quintiles_table.to_excel('quintiles_income_gap_ratio.xlsx', index=False)
print("Quintiles table saved to 'quintiles_income_gap_ratio.xlsx'")

# --- Deciles Analysis Table ---
df_deciles['Gap_Growth_%'] = df_deciles['Income_Gap'].pct_change(fill_method=None) * 100
df_deciles['Ratio_Change_%'] = df_deciles['Income_ratio'].pct_change(fill_method=None) * 100

deciles_table = df_deciles[['Year', '2nd', '10th', 'Income_Gap', 'Income_ratio', 'Gap_Growth_%', 'Ratio_Change_%']].round(2)

# Export to Excel
deciles_table.to_excel('deciles_income_gap_ratio.xlsx', index=False)
print("Deciles table saved to 'deciles_income_gap_ratio.xlsx'")
