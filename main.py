import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
DATA_PATH = "data/covid.csv"
OUTPUT_FOLDER = "output"
COUNTRY = "Nepal"   # Change to India, USA, etc.

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

# Filter selected country
country_data = df[df["location"] == COUNTRY].copy()
country_data = country_data.sort_values("date")

# Fill missing values (only for needed columns)
for col in ["total_cases", "total_deaths", "new_cases"]:
    if col in country_data.columns:
        country_data[col] = country_data[col].fillna(0)

# ---------------- Graph 1: Total Cases Over Time (Cumulative) ----------------
plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["total_cases"])
plt.title(f"Total COVID-19 Cases in {COUNTRY} (Cumulative)")
plt.xlabel("Date")
plt.ylabel("Cumulative Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/total_cases.png", dpi=200)
plt.show()

# ---------------- Graph 2: Total Deaths Over Time (Cumulative) ----------------
plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["total_deaths"])
plt.title(f"Total COVID-19 Deaths in {COUNTRY} (Cumulative)")
plt.xlabel("Date")
plt.ylabel("Cumulative Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/total_deaths.png", dpi=200)
plt.show()

# ---------------- Graph 3: Daily New Cases (7-day Average) ----------------
country_data["new_cases_7day_avg"] = country_data["new_cases"].rolling(7).mean()

plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["new_cases_7day_avg"])
plt.title(f"Daily New COVID-19 Cases in {COUNTRY} (7-day Average)")
plt.xlabel("Date")
plt.ylabel("New Cases (7-day Avg)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/daily_new_cases.png", dpi=200)
plt.show()

# ---------------- Graph 4: Top 10 Countries by Total Cases ----------------

# Remove rows where total_cases is missing
valid_data = df[df["total_cases"].notna()].copy()

# Find latest date where data actually exists
latest_date = valid_data["date"].max()

latest_data = valid_data[valid_data["date"] == latest_date].copy()

# Remove zero values
latest_data = latest_data[latest_data["total_cases"] > 0]

# Sort and take top 10
top10 = latest_data.sort_values("total_cases", ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top10["location"], y=top10["total_cases"])
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases (Cumulative)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/top10_countries.png", dpi=200)
plt.show()



# ---------------- Graph 5: Correlation Heatmap ----------------
corr_data = country_data[["total_cases", "total_deaths", "new_cases"]].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr_data, annot=True)
plt.title(f"COVID-19 Correlation Heatmap ({COUNTRY})")
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/heatmap.png", dpi=200)
plt.show()

print("✅ All graphs generated successfully! Check the output folder.")
