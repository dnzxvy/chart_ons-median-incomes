# ons-median-incomes
This project analyzes UK household disposable income using data published by the Office for National Statistics (ONS).
It extracts, processes, and visualizes income statistics from the ONS Excel dataset: ONS: The effects of taxes and benefits on household income, disposable income estimate
  https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/householddisposableincomeandinequality
Using Python, the project converts the raw data into time series plots (1977 – 2022/23) and forecasts future incomes using Linear Regression.

## Motivation
The reason behind this project was to:
- Explore how disposable household income has changed over time.
- Practice data wrangling using pandas.
- Visualize trends with clear charts using matplotlib.
- Extend the analysis by forecasting future income levels with machine learning.

By making the data visual, the project helps people quickly see trends that would otherwise be hidden in spreadsheets.

## Features
- Load raw income data from the ONS Excel file.
- Clean and preprocess data (handling years in formats like 1994/95).
- Generate historical time series plots of median household income.
- Compute income gaps and ratios across quintiles/deciles.
- Export cleaned data and results to Excel for further analysis.
- Forecast future income trends using Linear Regression (scikit-learn).

## Example Outputs
- **Median Income Time Series (1977–2022/23)**
- **Forecast Plots: Historical vs Predicted incomes (next 20 years)**
- **Excel Tables: Historical data + Forecast results (quintiles & deciles)**
- **Plot historical vs. forecasted incomes side by side for comparison.**

## Libraries Used
- **Pandas** for reading, cleaning, and exporting data
- **Matplotlib** for plotting income trends
- **Scikit-learn** for Linear Regression forecasting
- **NumPy** for numerical operations

## Project Structure
chart_median_incomes_uk/
│
├── hdiiifye2023.xlsx # Original ONS dataset (Excel file)
├── median_income.py # Main script for data extraction, cleaning, forecasting, and visualization
├── income_forecasts.xlsx # Quintiles historical + forecast data
├── income_forecasts_deciles.xlsx # Deciles historical + forecast data
├── quintiles_income_gap_ratio.xlsx # Processed quintiles income gap & ratio
├── deciles_income_gap_ratio.xlsx # Processed deciles income gap & ratio
│
├── median_income_plot.png # Median income visualization
├── median_quintile_decile_incomes.png # Combined quintiles & deciles plot
├── figure2_median_decile_incomes.png # Deciles median income plot
├── income_gap.png # Income gap over time plot
├── income_ratio.png # Income ratio over time plot
├── historic_future_forecasts.png # Forecast visualization for quintiles & deciles
│
└── README.md # Project documentation

## Setup

1. Clone the repository:

git clone <your-repo-url>
cd ons-median-incomes

2.Install dependencies
pip install pandas matplotlib scikit-learn numpy

3.Run the script:

python median_income.py
