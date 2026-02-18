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
df["date"] = pd.to_datetime(df["date"])

# Filter selected country
country_data = df[df["location"] == COUNTRY].copy()
country_data = country_data.sort_values("date")

# Fill missing values
country_data["total_cases"] = country_data["total_cases"].fillna(0)
country_data["total_deaths"] = country_data["total_deaths"].fillna(0)
country_data["new_cases"] = country_data["new_cases"].fillna(0)

# ---------------- Graph 1: Total Cases Over Time ----------------
plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["total_cases"])
plt.title(f"Total COVID-19 Cases in {COUNTRY}")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/total_cases.png", dpi=200)
plt.show()

# ---------------- Graph 2: Total Deaths Over Time ----------------
plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["total_deaths"])

plt.title(f"Total COVID-19 Deaths in {COUNTRY} (Cumulative)")
plt.xlabel("Date")
plt.ylabel("Cumulative Deaths")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/total_deaths.png", dpi=200)
plt.show()


# ---------------- Graph 3: Daily New Cases ----------------
plt.figure(figsize=(10, 5))
plt.plot(country_data["date"], country_data["new_cases"])
plt.title(f"Daily New COVID-19 Cases in {COUNTRY}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/daily_new_cases.png", dpi=200)
plt.show()

# ---------------- Graph 4: Top 10 Countries by Total Cases ----------------
latest_date = df["date"].max()
latest_data = df[df["date"] == latest_date]

top10 = latest_data.sort_values("total_cases", ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top10["location"], y=top10["total_cases"])
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/top10_countries.png", dpi=200)
plt.show()

# ---------------- Graph 5: Correlation Heatmap ----------------
corr_data = country_data[["total_cases", "total_deaths", "new_cases"]].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr_data, annot=True, cmap="coolwarm")
plt.title(f"COVID-19 Correlation Heatmap ({COUNTRY})")
plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/heatmap.png", dpi=200)
plt.show()

print("✅ All graphs generated successfully! Check the output folder.")

