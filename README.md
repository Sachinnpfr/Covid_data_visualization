# 🦠 COVID-19 Data Visualization

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-purple)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

This project analyzes COVID-19 data using Python and generates insightful visualizations such as:

- 📈 Total Cases (Cumulative)
- 💀 Total Deaths (Cumulative)
- 📊 Daily New Cases
- 🌍 Top 10 Countries by Total Cases
- 🔥 Correlation Heatmap

All graphs are automatically saved inside the `output/` folder.

---

## 📂 Project Structure

```
Covid_data_visualization/
│
├── data/
│   └── covid.csv
│
├── output/
│   ├── total_cases.png
│   ├── total_deaths.png
│   ├── daily_new_cases.png
│   ├── top10_countries.png
│   └── heatmap.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

Clone the repository:

```
git clone https://github.com/Sachinnpfr/Covid_data_visualization.git
cd Covid_data_visualization
```

Install dependencies:

```
pip install -r requirements.txt
```

Or manually:

```
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run

1️⃣ Download the dataset from **Our World in Data**  
👉 https://ourworldindata.org/coronavirus  

2️⃣ Place the CSV file inside:

```
data/covid.csv
```

3️⃣ Run the program:

```
python main.py
```

All visualizations will be saved inside the `output/` folder.

---

## 📷 Output Visualizations

### 📈 Total Cases (Cumulative)
![Total Cases](output/total_cases.png)

### 💀 Total Deaths (Cumulative)
![Total Deaths](output/total_deaths.png)

### 📊 Daily New Cases
![Daily New Cases](output/daily_new_cases.png)

### 🌍 Top 10 Countries by Total Cases
![Top 10 Countries](output/top10_countries.png)

### 🔥 Correlation Heatmap
![Heatmap](output/heatmap.png)

---

## 📊 Data Source

Dataset provided by:  
**Our World in Data**  
https://ourworldindata.org/coronavirus

---

## 👨‍💻 Author

**Sachin Jha**  
GitHub: https://github.com/Sachinnpfr

---

⭐ If you found this project useful, consider giving it a star!
