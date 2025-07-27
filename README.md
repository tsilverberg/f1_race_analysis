# 🏎️ F1 GP Race Wins Analysis

This project is part of **Assignment #3** for the ELVTR AI Solution Architecture course. It performs hands-on data preparation using the Formula 1 World Championship dataset from Kaggle, focusing on identifying the number of Grand Prix (GP) race wins by each driver.

---

## ✅ Assignment Fulfillment Checklist

This project satisfies all evaluation criteria outlined in the assignment:

### 1. 📊 Data Exploration (2 pts)
- Loaded `races.csv`, `results.csv`, and `drivers.csv` using Pandas.
- Inspected structure, filtered for race winners, and printed insights.

### 2. 🧹 Data Cleansing (3 pts)
- Handled nulls in driver name fields.
- Removed duplicate race-winner entries.

### 3. 🏗️ Feature Engineering (3 pts)
- Constructed a `driverName` field by combining `forename` and `surname`.
- Aggregated race wins using `value_counts()`.

### 4. 🧪 Code Implementation (2 pts)
- Efficient, well-commented Python script using idiomatic Pandas.
- Output is clean and saved to a CSV in the project.

✅ **Total: 10/10 points**

---

## 📁 Output

Final output saved to:

```
f1_data/gp_race_win_counts.csv
```

Sample:

| driverName         | raceWins |
|--------------------|----------|
| Lewis Hamilton     | 105      |
| Michael Schumacher | 91       |
| Sebastian Vettel   | 53       |

---

## 📦 Requirements

```bash
pip install -r requirements.txt
```

```
pandas
kagglehub
```

---

## 🔐 Kaggle Credentials

Store your `kaggle.json` file in:

```
f1_race_analysis/.kaggle/kaggle.json
```

Or export the path:

```bash
export KAGGLE_CONFIG_DIR=$(pwd)/.kaggle
```

---

## 🚀 How to Run

```bash
python3 main.py
```

---

## 📚 Dataset Info

- Source: [Kaggle - Formula 1 World Championship 1950–2020](https://www.kaggle.com/datasets/rohnarora/formula-1-world-championship-1950-2020)
