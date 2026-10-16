# Local Business Sales Analysis

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Excel](https://img.shields.io/badge/Excel-Reports-217346)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A field project that analyses the sales records of a local grocery shop (3 July 2026 to 20 September 2026) to find best-selling and low-selling products, sales trends and category performance, and to suggest ways to improve sales and inventory management.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Dataset](#dataset)
5. [Tools and Technologies](#tools-and-technologies)
6. [Project Structure](#project-structure)
7. [Methodology](#methodology)
8. [How to Run](#how-to-run)
9. [Output Files](#output-files)
10. [Key Findings](#key-findings)
11. [Recommendations](#recommendations)
12. [Power BI Dashboard](#power-bi-dashboard)
13. [Future Scope](#future-scope)
14. [Acknowledgement](#acknowledgement)

---

## Project Overview

Small shops record every sale but rarely study the data. This project cleans a grocery shop's sales records and turns them into clear reports:

| No. | Report | What it shows |
|---|---|---|
| 1 | Total Sales | Revenue, discount, invoices, quantity and average invoice value |
| 2 | Best-Selling Products | Products sold most often (by number of invoices) |
| 3 | Category-wise Sales | Sales, quantity and share of each product category |
| 4a | Sales Trend (Weekly) | Sales for each 7-day week, average daily sales and change from the previous week |
| 4b | Sales Trend (Monthly) | Monthly sales, average daily sales and change from the previous month |
| 5 | Top Revenue Products | Products that earn the most, with share and cumulative share |
| 6 | Quantity Sold | Units sold for every product |

The program also writes data-driven **recommendations** for the shop owner.

## Problem Statement

The owner of a local grocery shop does not know clearly which products give the most sales, which products sell slowly, and how sales change from week to week and day to day. Without this information, stock decisions are based on guesswork, which can lead to stock-outs of popular items and unsold slow items.

## Objectives

- Collect, clean and organise the sales data of the grocery shop.
- Identify best-selling and low-selling products.
- Study sales trends by week, month, weekday, category, payment method and customer type.
- Present the findings through tables, Excel reports and a Power BI dashboard.
- Suggest practical ways to improve sales and inventory management.

## Dataset

- **File:** `local_business_sales_analysis_1500_records.csv`
- **Records:** 1,500 invoices
- **Period:** 3 July 2026 to 20 September 2026 (80 days)
- **Products:** 30 products across 14 categories (after cleaning)

> **Data note:** the dataset combines 617 records taken from the shop's original sales file with 883 additional records generated in the same pattern (product mix, prices, quantities, discounts, payment methods and customer types) to reach 1,500 records for the selected period.

| Column | Description |
|---|---|
| `Invoice_ID` | Unique invoice number |
| `Date`, `Year`, `Month`, `Month_Number`, `Day` | Date details of the sale |
| `Product_ID`, `Product_Name` | Product identifier and name |
| `Category` | Product category (Grains, Pulses, Dairy, and others) |
| `Quantity` | Units sold |
| `Unit_Price_INR` | Price per unit in rupees |
| `Discount_Percent` | Discount given on the sale |
| `Total_Sales_INR` | Final amount = Quantity x Price x (1 - Discount%) |
| `Payment_Method` | Cash, UPI or Debit/Credit Card |
| `Customer_Type` | Walk-in or Regular |

## Tools and Technologies

| Tool | Use |
|---|---|
| Python 3.9+ | Main programming language |
| Pandas | Data cleaning, grouping and calculations |
| OpenPyXL | Formatted Excel report |
| Microsoft Excel | PivotTables and basic calculations |
| Power BI | Interactive dashboard |
| VS Code and Git/GitHub | Development and version control |

## Project Structure

```
DataScience/
└── Local-Business-Sales-Analysis/
    ├── README.md
    ├── sales_analysis.py                                   # main program
    ├── local_business_sales_analysis_1500_records.csv      # input data
    ├── sales_cleaned.csv                                   # cleaned data (for Power BI)
    ├── sales_summary.xlsx                                  # formatted Excel report
    └── output/
        ├── 1_Total_Sales.csv
        ├── 2_Best_Selling_Products.csv
        ├── 3_Category_wise_Sales.csv
        ├── 4a_Sales_Trend_Weekly.csv
        ├── 4b_Sales_Trend_Monthly.csv
        ├── 5_Top_Revenue_Products.csv
        ├── 6_Quantity_Sold.csv
        └── 7_Recommendations.txt
```

## Methodology

1. **Data collection:** studied the shop's sales records and their columns.
2. **Data cleaning:** checked missing values, duplicate records, inconsistent entries and data formats. The category "Dairy & Eggs" was merged into "Dairy", text was trimmed and dates were converted to date format.
3. **Data preparation:** added calculated columns (`Year_Month`, `Week_Day`, `Gross_Sales`, `Discount_Amount`) and verified that every total matches Quantity x Price x (1 - Discount%).
4. **Exploratory analysis:** compared sales across products, categories, weeks, months, weekdays, payment methods and customer types.
5. **Reporting:** generated the reports and saved each as a separate file.
6. **Visualisation:** built the Power BI dashboard from `sales_cleaned.csv`.
7. **Recommendations:** produced suggestions for sales and inventory management from the results.

## How to Run

**Requirements:** Python 3.9 or higher.

```bash
# 1. Clone the repository
git clone https://github.com/ram-golhar-33/DataScience.git
cd DataScience/Local-Business-Sales-Analysis

# 2. Install the libraries
pip install pandas openpyxl

# 3. Run the program
python sales_analysis.py
```

> The program reads the data from `D:\DS\local_business_sales_analysis_1500_records.csv`.
> If your files are in another folder, change `DATA_PATH`, `MAIN_DIR` and `OUT_DIR` at the top of `sales_analysis.py`.

## Output Files

| File | Location | Contents |
|---|---|---|
| `sales_cleaned.csv` | project folder | Cleaned dataset with calculated columns |
| `sales_summary.xlsx` | project folder | One formatted sheet per report plus recommendations |
| `1_Total_Sales.csv` ... `6_Quantity_Sold.csv` | `output/` | One file for each report (the trend report has weekly and monthly files) |
| `7_Recommendations.txt` | `output/` | Recommendations written from the data |

## Key Findings

Based on the 1,500 records analysed (3 July 2026 to 20 September 2026):

| Measure | Value |
|---|---|
| Total sales | Rs. 3,82,218.88 |
| Total discount given | Rs. 4,612.50 |
| Total invoices | 1,500 |
| Total quantity sold | 4,358 units |
| Average invoice value | Rs. 254.81 |

- **Top revenue products:** Rice 5kg (18.00% of sales), Wheat Flour 5kg (10.83%), Toor Dal 1kg, Moong Dal 1kg and Tea 250g. The top 10 products together bring in about 64.6% of all sales.
- **Best-selling products (by invoices):** Potato 1kg, Onion 1kg and Curd 500g (74 invoices each), followed by Salt 1kg and Milk 1L (68 each).
- **Most units sold:** Potato 1kg (233 units), Rice 5kg (214) and Onion 1kg (202).
- **Strongest category:** Grains with 28.82% of sales, followed by Pulses (11.53%), Beverages (10.33%) and Dairy (8.09%).
- **Lowest revenue products:** Turmeric Powder, Bath Soap, Salt 1kg, Biscuits Pack and Instant Noodles.
- **Monthly trend (average daily sales):** July Rs. 5,174, August Rs. 4,384 and September Rs. 4,813.
- **Weekday pattern:** Monday has the highest average daily sales and Tuesday the lowest.
- **Payments:** UPI is the most used method (46.9% of sales).
- **Customers:** walk-in customers give about 73% of sales.

## Recommendations

1. Keep the top revenue products always in stock: Rice, Wheat Flour, Toor Dal, Moong Dal and Tea.
2. Protect the supply and pricing of the Grains category, the biggest earner.
3. Increase stock before Monday, the highest-selling weekday, and keep lower stock on Tuesday.
4. Offer bundle deals or discounts on slow products such as Turmeric Powder, Bath Soap, Salt, Biscuits and Instant Noodles.
5. Plan extra stock for strong weeks (such as the first week of July) and reduce orders in weak weeks.
6. Start loyalty offers to turn walk-in customers into regular customers.
7. Promote UPI and other digital payments for faster billing.
8. Reorder class A products weekly, class B every two weeks and class C monthly.

## Power BI Dashboard

Load `sales_cleaned.csv` into Power BI Desktop and add these measures:

```
Total Sales    = SUM(sales_cleaned[Total_Sales_INR])
Total Quantity = SUM(sales_cleaned[Quantity])
Total Invoices = DISTINCTCOUNT(sales_cleaned[Invoice_ID])
Average Invoice = DIVIDE([Total Sales], [Total Invoices])
```

Suggested visuals: KPI cards, weekly or daily sales line chart, top 10 products bar chart, category donut chart, weekday column chart and payment method pie chart, with slicers for Month, Category and Customer_Type.

> Add a dashboard screenshot to the repository (for example `dashboard/dashboard.png`) and show it here:
> `![Dashboard](dashboard/dashboard.png)`

## Future Scope

- Forecast future sales using time-series models.
- Add automatic low-stock alerts based on sales speed.
- Analyse profit by adding purchase cost data.
- Build a simple web dashboard for the shop owner.

## Acknowledgement

We thank our mentor for the guidance given throughout this field project, and the shop owner for providing the sales records.

---

*This project was prepared for academic purposes as part of a field project.*
