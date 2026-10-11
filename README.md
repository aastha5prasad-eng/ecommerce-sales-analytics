# E-Commerce Sales Analytics Dashboard 📊

An interactive dashboard built with Python to analyze e-commerce sales performance, explore business trends, and generate filtered sales reports.

## 🚀 Project Overview

The E-Commerce Sales Analytics Dashboard helps users understand sales performance through interactive charts, key performance indicators (KPIs), and customizable filters. Users can explore sales across regions and product categories and download filtered data for further analysis.

## ✨ Features

- **Sales Performance KPIs:** Total Sales, Average Order Value, Total Orders, and Total Customers.
- **Interactive Filters:** Filter data by region and product category.
- **Product Category Analysis:** Compare sales across product categories.
- **Customer Segment Analysis:** Understand sales distribution by customer segment.
- **Monthly Sales Trend:** Track revenue over time.
- **CSV Report Download:** Export filtered sales data.
- **Interactive Visualizations:** Explore charts built with Plotly.
- **Dark Theme:** Clean, dark dashboard interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## 📁 Project Structure

```text
ecommerce-sales-analytics/
├── analysis/
│   └── analyze_data.py
├── dashboard/
│   └── app.py
├── data/
│   └── global_ecommerce_sales-selected-columns.csv
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### Prerequisites

Install Python and make sure it is available from your terminal.

### 1. Clone the repository

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-sales-analytics
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
streamlit run dashboard/app.py
```

Open the local URL displayed in the terminal to access the dashboard.

## 📊 Dataset

The project uses a CSV dataset containing e-commerce sales information. Available fields support analysis of regions, product categories, order dates, quantities, prices, and other sales-related metrics.

## 💡 Skills Demonstrated

- Data analysis using Pandas
- Interactive dashboard development
- Data visualization with Plotly
- Data filtering and CSV export
- Business performance reporting

## 🔮 Future Improvements

- Date-range filters
- Profit and sales growth analysis
- Automated data refresh
- Online dashboard deployment
- Additional business insights

## 👩‍💻 Author

Created as a data analytics portfolio project using Python and Streamlit.
