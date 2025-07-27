# 🏎️ F1 GP Race Wins Analysis

This project is part of **Assignment #3** for the ELVTR AI Solution Architecture course. It performs hands-on data preparation using the Formula 1 World Championship dataset from Kaggle, focusing on identifying the number of Grand Prix (GP) race wins by each driver.

## 🧠 Assignment Objective

- ✅ Explore and clean real-world racing data
- ✅ Perform feature engineering (e.g. combining driver names)
- ✅ Aggregate race wins per driver
- ✅ Export clean summary data for reporting

## 📁 Output

The final output is saved to:

```
f1_data/gp_race_win_counts.csv
```

Sample:

| driverName         | raceWins |
|--------------------|----------|
| Lewis Hamilton     | 105      |
| Michael Schumacher | 91       |
| Sebastian Vettel   | 53       |

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pandas
kagglehub
```

## 🔐 Kaggle Credentials

To run this script, you'll need a valid `kaggle.json` file with your API key.

Place it in:

```
f1_race_analysis/.kaggle/kaggle.json
```

## 🚀 How to Run

```bash
python3 main.py
```

The script will:
1. Download the dataset via KaggleHub
2. Clean and join race + driver data
3. Count wins per driver
4. Save results to `f1_data/`

## 📚 Dataset Info

- Source: [Kaggle - Formula 1 World Championship 1950–2020](https://www.kaggle.com/datasets/rohnarora/formula-1-world-championship-1950-2020)
