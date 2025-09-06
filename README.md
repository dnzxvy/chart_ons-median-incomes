# ons-median-incomes

This project analyzes UK household disposable income using data published by the Office for National Statistics (ONS).
It extracts, processes, and visualizes income statistics from the ONS Excel dataset: ONS: The effects of taxes and benefits on household income, disposable income estimate
  https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/householddisposableincomeandinequality
Using Python, the project converts the raw data into time series plots (1977 – 2022/23) and forecasts future incomes using Linear Regression.

The reason behind this project was to:
- Explore how disposable household income has changed over time.
- Practice data wrangling using pandas.
- Visualize trends with clear charts using matplotlib.
- Extend the analysis by forecasting future income levels with machine learning.

By making the data visual, the project helps people quickly see trends that would otherwise be hidden in spreadsheets.
Various Features Include:
- Load raw income data from the ONS Excel file.
- Clean and preprocess data (handling years in formats like 1994/95).
- Generate historical time series plots of median household income.
- Compute income gaps and ratios across quintiles/deciles.
- Export cleaned data and results to Excel for further analysis.
- Forecast future income trends using Linear Regression (scikit-learn).
- Plot historical vs. forecasted incomes side by side for comparison.

Example Outputs:
Median Income Time Series (1977–2022/23): 

Forecast Plots: Historical vs Predicted incomes (next 20 years): 

Excel Tables: Historical data + Forecast results (quintiles & deciles): 

Libraries Used:
Pandas
 - for reading, cleaning, and exporting data
Matplotlib
 - for plotting income trends
Scikit-learn
 - for Linear Regression forecasting
NumPy
 - for numerical operations


