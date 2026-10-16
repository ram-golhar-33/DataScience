import os
import sys

import pandas as pd
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

# ----------------------------- CONFIGURATION -----------------------------
DATA_PATH = r"D:\DS\local_business_sales_analysis_1500_records.csv"
MAIN_DIR = r"D:\DS"
OUT_DIR = r"D:\DS\output"
TOP_N = 10

pd.set_option("display.width", 170)
pd.set_option("display.max_rows", 100)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")


# ------------------------------- FUNCTIONS -------------------------------
def load_data(path: str) -> pd.DataFrame:
    """Read the sales records file."""
    if not os.path.exists(path):
        sys.exit(f"Data file not found: {path}")
    return pd.read_csv(path, encoding="utf-8-sig")      # utf-8-sig removes the hidden BOM


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates, fix text and dates, and add calculated columns."""
    df = df.drop_duplicates().copy()
    for col in ["Product_Name", "Category", "Payment_Method", "Customer_Type"]:
        df[col] = df[col].str.strip()
    df["Category"] = df["Category"].replace({"Dairy & Eggs": "Dairy"})
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year_Month"] = df["Date"].dt.to_period("M").astype(str)
    df["Week_Day"] = df["Date"].dt.day_name()
    df["Gross_Sales"] = df["Quantity"] * df["Unit_Price_INR"]
    df["Discount_Amount"] = df["Gross_Sales"] - df["Total_Sales_INR"]
    return df


def total_sales_report(df: pd.DataFrame) -> pd.DataFrame:
    """1. Total Sales - key business figures."""
    items = {
        "Total Sales (Rs.)": df["Total_Sales_INR"].sum(),
        "Gross Sales before Discount (Rs.)": df["Gross_Sales"].sum(),
        "Total Discount Given (Rs.)": df["Discount_Amount"].sum(),
        "Total Invoices": df["Invoice_ID"].nunique(),
        "Total Quantity Sold": df["Quantity"].sum(),
        "Average Invoice Value (Rs.)": df["Total_Sales_INR"].mean(),
        "Number of Products": df["Product_Name"].nunique(),
        "Period From": str(df["Date"].min().date()),
        "Period To": str(df["Date"].max().date()),
    }
    out = pd.DataFrame({"Metric": list(items), "Value": list(items.values())})
    return out.set_index("Metric")


def best_selling_report(df: pd.DataFrame) -> pd.DataFrame:
    """2. Best-Selling Products - ranked by number of invoices (how often sold)."""
    t = df.groupby("Product_Name").agg(Invoices=("Invoice_ID", "nunique"),
                                       Quantity_Sold=("Quantity", "sum"),
                                       Total_Sales=("Total_Sales_INR", "sum"))
    t = t.sort_values(["Invoices", "Quantity_Sold"], ascending=False).head(TOP_N)
    t.insert(0, "Rank", range(1, len(t) + 1))
    return t.round(2)


def category_report(df: pd.DataFrame) -> pd.DataFrame:
    """3. Category-wise Sales."""
    t = df.groupby("Category").agg(Total_Sales=("Total_Sales_INR", "sum"),
                                   Quantity_Sold=("Quantity", "sum"),
                                   Invoices=("Invoice_ID", "nunique"))
    t = t.sort_values("Total_Sales", ascending=False)
    t["Share_%"] = t["Total_Sales"] / t["Total_Sales"].sum() * 100
    t.insert(0, "Rank", range(1, len(t) + 1))
    return t.round(2)


def weekly_trend_report(df: pd.DataFrame) -> pd.DataFrame:
    """4a. Sales Trend (weekly) - 7-day blocks counted from the first date in the data."""
    daily = df.groupby("Date")["Total_Sales_INR"].sum().reset_index()
    daily["Week_No"] = (daily["Date"] - df["Date"].min()).dt.days // 7 + 1
    t = daily.groupby("Week_No").agg(Week_Start=("Date", "min"), Week_End=("Date", "max"),
                                     Days=("Date", "count"), Total_Sales=("Total_Sales_INR", "sum"))
    t["Avg_Daily_Sales"] = t["Total_Sales"] / t["Days"]
    t["Change_%_vs_Previous_Week"] = t["Avg_Daily_Sales"].pct_change() * 100
    t["Week_Start"] = t["Week_Start"].dt.strftime("%Y-%m-%d")
    t["Week_End"] = t["Week_End"].dt.strftime("%Y-%m-%d")
    return t.round(2)


def monthly_trend_report(df: pd.DataFrame) -> pd.DataFrame:
    """4b. Sales Trend (monthly) - average daily sales is used because July and September are part months."""
    daily = df.groupby(["Year_Month", "Date"])["Total_Sales_INR"].sum().reset_index()
    t = daily.groupby("Year_Month").agg(Days=("Date", "count"), Total_Sales=("Total_Sales_INR", "sum"))
    t["Avg_Daily_Sales"] = t["Total_Sales"] / t["Days"]
    t["Change_%_vs_Previous_Month"] = t["Avg_Daily_Sales"].pct_change() * 100
    return t.round(2)


def top_revenue_report(df: pd.DataFrame) -> pd.DataFrame:
    """5. Top Revenue Products - with share and cumulative share of total sales."""
    s = df.groupby("Product_Name")["Total_Sales_INR"].sum().sort_values(ascending=False)
    t = s.to_frame("Total_Sales")
    t["Share_%"] = t["Total_Sales"] / s.sum() * 100
    t["Cumulative_Share_%"] = t["Share_%"].cumsum()
    t.insert(0, "Rank", range(1, len(t) + 1))
    return t.round(2).head(TOP_N)


def quantity_report(df: pd.DataFrame) -> pd.DataFrame:
    """6. Quantity Sold - all products."""
    q = df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False)
    t = q.to_frame("Quantity_Sold")
    t["Share_%"] = t["Quantity_Sold"] / q.sum() * 100
    t.insert(0, "Rank", range(1, len(t) + 1))
    return t.round(2)


def recommendations(df, categories, weekly) -> str:
    """Data-driven recommendations for sales and inventory management."""
    total = df["Total_Sales_INR"].sum()
    sales_by_product = df.groupby("Product_Name")["Total_Sales_INR"].sum().sort_values(ascending=False)
    top5 = ", ".join(sales_by_product.head(5).index)
    low5 = ", ".join(sales_by_product.tail(5).index)
    daily = df.groupby("Date")["Total_Sales_INR"].sum()
    weekday = daily.groupby(daily.index.day_name()).mean()
    pay = df.groupby("Payment_Method")["Total_Sales_INR"].sum()
    walk_in = df[df["Customer_Type"] == "Walk-in"]["Total_Sales_INR"].sum() / total * 100
    full_weeks = weekly[weekly["Days"] == 7]
    best_w, low_w = full_weeks["Avg_Daily_Sales"].idxmax(), full_weeks["Avg_Daily_Sales"].idxmin()
    return (
        "RECOMMENDATIONS\n"
        f"1. Keep the top revenue products always in stock: {top5}.\n"
        f"2. {categories.index[0]} is the strongest category "
        f"({categories['Share_%'].iloc[0]:.1f}% of sales); protect its supply and pricing.\n"
        f"3. Increase stock before {weekday.idxmax()} (highest average daily sales); keep lower stock on {weekday.idxmin()}.\n"
        f"4. Offer bundle deals or discounts on slow products: {low5}.\n"
        f"5. Plan extra stock for strong weeks like Week {best_w} ({weekly.loc[best_w, 'Week_Start']} to "
        f"{weekly.loc[best_w, 'Week_End']}) and reduce orders in weak weeks like Week {low_w}.\n"
        f"6. Walk-in customers give {walk_in:.1f}% of sales; start loyalty offers to make them regular.\n"
        f"7. {pay.idxmax()} is the most used payment method ({pay.max() / pay.sum() * 100:.1f}%); promote digital payments.\n"
        "8. Reorder class A products weekly, class B every two weeks and class C monthly."
    )


def style_workbook(writer) -> None:
    """Apply a professional look to every sheet of the Excel report."""
    header_fill = PatternFill("solid", fgColor="1F4E78")
    thin = Side(style="thin", color="BFBFBF")
    for ws in writer.book.worksheets:
        for cell in ws[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column):
            for cell in row:
                cell.border = Border(top=thin, bottom=thin, left=thin, right=thin)
                if isinstance(cell.value, float):
                    cell.number_format = "#,##0.00"
        for idx, col in enumerate(ws.columns, 1):
            width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
            ws.column_dimensions[get_column_letter(idx)].width = min(max(width + 3, 12), 60)
        ws.freeze_panes = "A2"


# ---------------------------------- MAIN ----------------------------------
def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    raw = load_data(DATA_PATH)
    print(f"Records loaded: {len(raw)}  |  Duplicates: {raw.duplicated().sum()}  |  "
          f"Missing values: {raw.isnull().sum().sum()}")

    df = clean_data(raw)
    df.to_csv(os.path.join(MAIN_DIR, "sales_cleaned.csv"), index=False, encoding="utf-8-sig")

    reports = {
        "1_Total_Sales": total_sales_report(df),
        "2_Best_Selling_Products": best_selling_report(df),
        "3_Category_wise_Sales": category_report(df),
        "4a_Sales_Trend_Weekly": weekly_trend_report(df),
        "4b_Sales_Trend_Monthly": monthly_trend_report(df),
        "5_Top_Revenue_Products": top_revenue_report(df),
        "6_Quantity_Sold": quantity_report(df),
    }
    advice = recommendations(df, reports["3_Category_wise_Sales"], reports["4a_Sales_Trend_Weekly"])

    # print every report and save it as its own file
    for name, table in reports.items():
        print("\n" + "=" * 72 + f"\n{name.replace('_', ' ')}\n" + "=" * 72)
        print(table.to_string())
        table.to_csv(os.path.join(OUT_DIR, f"{name}.csv"), encoding="utf-8-sig")
    print("\n" + "=" * 72 + "\n" + advice)
    with open(os.path.join(OUT_DIR, "7_Recommendations.txt"), "w", encoding="utf-8") as f:
        f.write(advice)

    # one professional Excel workbook: a sheet per report + recommendations
    xlsx_path = os.path.join(MAIN_DIR, "sales_summary.xlsx")
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        for name, table in reports.items():
            table.to_excel(writer, sheet_name=name[:31])
        pd.DataFrame({"Recommendations": advice.split("\n")[1:]}).to_excel(
            writer, sheet_name="7_Recommendations", index=False)
        style_workbook(writer)

    print("\n" + "=" * 72)
    print("DONE")
    print(f"  {MAIN_DIR}\\sales_cleaned.csv")
    print(f"  {MAIN_DIR}\\sales_summary.xlsx")
    print(f"  {OUT_DIR}\\  ->  " + ", ".join(f"{n}.csv" for n in reports) + ", 7_Recommendations.txt")


if __name__ == "__main__":
    main()