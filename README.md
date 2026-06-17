# 🎬 Bollywood Box Office Analysis

A Python-based data analysis project exploring Bollywood movie performance from 2000–2024, uncovering trends in box office collections, genre performance, actor success rates, and the relationship between IMDb ratings and commercial success.

## 📊 Project Overview

This project analyzes a dataset of 66 Bollywood movies to answer key questions:
- Which movies, actors, and directors deliver the highest box office returns?
- Does IMDb rating correlate with commercial success?
- Which genres perform best financially?
- How has the industry's box office trended year over year?
- What's the overall Hit-to-Flop ratio?

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data manipulation and aggregation
- **NumPy** — numerical computations and trend analysis
- **Matplotlib & Seaborn** — data visualization
- **Excel/CSV** — data source

## 📁 Project Structure
## 📈 Dashboard Features

The analysis generates a 6-panel dashboard covering:

1. **Top 8 Movies by Collection** — highest grossing films, color-coded by verdict
2. **Hit vs Flop Ratio** — overall success rate pie chart
3. **IMDb Rating vs Collection** — scatter plot with trend line showing rating-revenue correlation
4. **Average Collection by Genre** — which genres perform best
5. **Yearly Box Office Trend** — collection trends across 2000–2024
6. **Top Directors by Hits** — most consistently successful directors

## 🔑 Key Insights

- **65% of movies in the dataset were box office Hits**
- **Drama** emerged as the highest-grossing genre on average
- Positive correlation observed between IMDb rating and box office collection
- Identified top-performing actor-director combinations

## 🚀 How to Run

1. Clone the repository
```bash
   git clone https://github.com/Aditya-pal12/bollywood-box-office-analysis.git
   cd bollywood-box-office-analysis
```

2. Install dependencies
```bash
   pip install pandas numpy matplotlib openpyxl
```

3. Run the analysis
```bash
   python bollywood_final.py
```

4. View the generated `bollywood_dashboard.png` for visual insights

## 📋 Dataset Columns

| Column | Description |
|--------|-------------|
| movie | Movie title |
| year | Release year |
| lead_actor | Lead actor name |
| director | Director name |
| genre | Movie genre |
| budget_cr | Production budget (₹ Crores) |
| collection_cr | Box office collection (₹ Crores) |
| imdb_rating | IMDb rating |
| verdict | Hit / Flop classification |
| release_month | Month of release |
| screens | Number of screens released on |
| roi_percent | Return on investment percentage |

## 👤 Author

**Aditya Pal**  
Freelance AI Trainer & Data Annotator | Data Analyst | SQL | Power BI | Advanced Excel

---

*This project is part of a data analytics portfolio demonstrating skills in EDA, data visualization, and Python-based analysis pipelines.*
