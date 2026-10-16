# Local Business Sales Analysis

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Excel](https://img.shields.io/badge/Excel-Reports-217346)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A field project that analyses the sales records of a local grocery shop to find best-selling and low-selling products, sales trends and category performance, and to suggest ways to improve sales and inventory management.

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

Small shops record every sale but rarely study the data. This project cleans a grocery shop's sales records and turns them into six clear reports:

| No. | Report | What it shows |
|---|---|---|
| 1 | Total Sales | Revenue, discount, invoices, quantity and average invoice value |
| 2 | Best-Selling Products | Products sold most often (by number of invoices) |
| 3 | Category-wise Sales | Sales, quantity and share of each product category |
| 4 | Sales Trend | Monthly sales, change from the previous month and 3-month moving average |
| 5 | Top Revenue Products | Products that earn the most, with share and cumulative share |
| 6 | Quantity Sold | Units sold for every product |

The program also writes data-driven **recommendations** for the shop owner.

## Problem Statement

The owner of a local grocery shop does not know clearly which products give the most sales, which products sell slowly, and how sales change from month to month and day to day. Without this information, stock decisions are based on guesswork, which can lead to stock-outs of popular items and unsold slow items.

## Objectives

- Collect, clean and organise the sales data of the grocery shop.
- Identify best-selling and low-selling products.
- Study sales trends by month, weekday, category, payment method and customer type.
- Present the findings through tables, Excel reports and a Power BI dashboard.
- Suggest practical ways to improve sales and inventory management.

## Dataset

- **File:** `local_business_sales_analysis_2000_records.csv`
- **Records:** 2,000 invoices
- **Period:** 3 January 2025 to 30 September 2026
- **Products:** 30 products across 14 categories (after cleaning)

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
    ├── local_business_sales_analysis_2000_records.csv      # input data
    ├── sales_cleaned.csv                                   # cleaned data (for Power BI)
    ├── sales_summary.xlsx                                  # formatted Excel report
    └── output/
        ├── 1_Total_Sales.csv
        ├── 2_Best_Selling_Products.csv
        ├── 3_Category_wise_Sales.csv
        ├── 4_Sales_Trend.csv
        ├── 5_Top_Revenue_Products.csv
        ├── 6_Quantity_Sold.csv
        └── 7_Recommendations.txt
```

## Methodology

1. **Data collection:** studied the shop's sales records and their columns.
2. **Data cleaning:** checked missing values, duplicate records, inconsistent entries and data formats. The category "Dairy & Eggs" was merged into "Dairy", text was trimmed and dates were converted to date format.
3. **Data preparation:** added calculated columns (`Year_Month`, `Week_Day`, `Gross_Sales`, `Discount_Amount`) and verified that every total matches Quantity x Price x (1 - Discount%).
4. **Exploratory analysis:** compared sales across products, categories, months, weekdays, payment methods and customer types.
5. **Reporting:** generated the six reports and saved each as a separate file.
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

> The program reads the data from `D:\DS\local_business_sales_analysis_2000_records.csv`.
> If your files are in another folder, change `DATA_PATH`, `MAIN_DIR` and `OUT_DIR` at the top of `sales_analysis.py`.

## Output Files

| File | Location | Contents |
|---|---|---|
| `sales_cleaned.csv` | project folder | Cleaned dataset with calculated columns |
| `sales_summary.xlsx` | project folder | One formatted sheet per report plus recommendations |
| `1_Total_Sales.csv` ... `6_Quantity_Sold.csv` | `output/` | One file for each of the six reports |
| `7_Recommendations.txt` | `output/` | Recommendations written from the data |

## Key Findings

Based on the 2,000 records analysed:

| Measure | Value |
|---|---|
| Total sales | Rs. 5,23,642.50 |
| Total discount given | Rs. 6,268.31 |
| Total invoices | 2,000 |
| Total quantity sold | 5,907 units |
| Average invoice value | Rs. 261.82 |

- **Top revenue products:** Wheat Flour 5kg (16.67% of sales), Rice 5kg (14.04%), Moong Dal 1kg, Sunflower Oil 1L and Toor Dal 1kg. The top 10 products together bring in about 64.5% of all sales.
- **Best-selling products (by invoices):** Wheat Flour 5kg, Onion 1kg, Milk 1L, Butter 100g and Potato 1kg.
- **Most units sold:** Wheat Flour 5kg (335 units), Butter 100g (297) and Onion 1kg (294).
- **Strongest category:** Grains with 30.71% of sales, followed by Pulses (10.09%), Dairy (9.33%) and Beverages (9.05%).
- **Lowest revenue products:** Instant Noodles, Biscuits Pack, Bath Soap, Salt 1kg and Turmeric Powder 200g.
- **Weekday pattern:** Sunday has the highest average daily sales and Thursday the lowest.
- **Payments:** UPI is the most used method (49.5% of sales).
- **Customers:** walk-in customers give about 72% of sales.

## Recommendations

1. Keep the top revenue products always in stock: Wheat Flour, Rice, Moong Dal, Sunflower Oil and Toor Dal.
2. Protect the supply and pricing of the Grains category, the biggest earner.
3. Increase stock before Sunday and weekends, and keep lower stock on Thursday.
4. Offer bundle deals or discounts on slow products such as Instant Noodles, Biscuits and Bath Soap.
5. Plan extra stock before high-sales months and reduce orders in weak months.
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

Suggested visuals: KPI cards, monthly sales line chart, top 10 products bar chart, category donut chart, weekday column chart and payment method pie chart, with slicers for Year, Category and Customer_Type.

> Add a dashboard screenshot to the repository (for example `dashboard/dashboard.png`) and show it here:
> `![Dashboard](dashboard/dashboard.png)`

## Future Scope

- Forecast future sales using time-series models.
- Add automatic low-stock alerts based on sales speed.
- Analyse profit by adding purchase cost data.
- Build a simple web dashboard for the shop owner.

## Acknowledgement

We thank our mentor, **Prof. Shaheen Shaikh**, for her guidance throughout this field project, and the shop owner for providing the sales records.

---

*This project was prepared for academic purposes as part of a field project.*
