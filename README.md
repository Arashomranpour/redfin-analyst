<div align="center">

# 🏠 Redfin Real-Estate Analyst

**Upload a Redfin CSV export and get a statistical summary, charts and investment-opportunity flags for each listing.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)

</div>

---

## ✨ Features

- 📤 Upload a CSV downloaded from [Redfin](https://www.redfin.com/).
- 📋 Data preview and `describe()` summary statistics.
- 📈 Charts: days on market (histogram), price (box plot) and price per square foot (histogram).
- 💡 **Feature engineering** that flags opportunities:
  - **Additional bedroom opportunity** - based on square feet per bedroom (e.g. 2 bd ≥ 1300 sqft, 3 bd ≥ 1950 sqft, 4 bd ≥ 2600 sqft for single-family homes).
  - **ADU potential** - based on the lot-size to house-size ratio.
- 💾 Download the featurized dataset.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/redfin-analyst.git
cd redfin-analyst
pip install streamlit pandas numpy plotly
streamlit run st.py
```

## 📁 Project Structure

```
.
└── st.py     # Streamlit app: upload, stats, charts, opportunity features
```

## 🛠️ Tech Stack

`Streamlit` · `pandas` · `NumPy` · `Plotly`
