# Stock_AP

A Python-based stock dashboard built with Streamlit for market analysis and future price prediction.

## Overview

This project provides a simple web application that helps users explore stock information, visualize historical trends, and forecast future prices for selected companies. It uses Yahoo Finance for live market data and Plotly for interactive charts.

The dashboard is organized into three main navigation pages:
- Home
- Stock Analysis
- Stock Prediction

## Features

- Home landing page with company list and stock codes
- Stock analysis dashboard with date filters and technical indicators
- Stock prediction page with forecast generation
- Interactive Plotly charts
- Financial data retrieval using Yahoo Finance
- Time-series forecasting utilities
- Clean Streamlit-based UI

## Repository Structure

```text
Stock_AP/
├── app.py
├── Home.py
├── README.md
├── requirements.txt
├── pic.jpg
├── pages/
│   ├── .gitkeep
│   ├── __init__.py
│   ├── Stock_Analysis.py
│   ├── Stock_Prediction.py
│   └── utils/
│       ├── .gitkeep
│       ├── __init__.py
│       ├── model_training.py
│       └── plotly_fig.py
├── screenshots/           
│   ├── .gitkeep   
|   ├── home.png
│   ├── stock-analysis.png
│   └── stock-prediction.png
└── .gitignore

## Project Modules

### `app.py`
This is the main Streamlit app file. It controls navigation between the pages and loads the Home page as the default screen.

### `Home.py`
This page acts as the landing/dashboard overview. It includes:
- a welcome header
- the project image
- a scrollable company table with ticker codes
- a short description of the available features
- navigation buttons to the Stock Analysis and Stock Prediction pages

### `pages/Stock_Analysis.py`
This page lets users:
- select a company ticker
- choose a date range
- view company summary information
- check financial metrics
- explore trends with indicators such as SMA, EMA, RSI, and MACD
- display historical stock data and chart views

### `pages/Stock_Prediction.py`
This page provides forecasting capabilities by:
- selecting a stock ticker
- choosing forecast length in days
- fetching recent prices
- applying model-based forecasting logic
- displaying a forecast chart and preview table

### `pages/utils/model_training.py`
This file contains the core data-processing and prediction logic, including:
- stock data loading
- smoothing
- model configuration
- scaling and inverse scaling
- evaluation and forecast generation

### `pages/utils/plotly_fig.py`
This file contains reusable Plotly helper functions for:
- line charts
- candlestick charts
- moving averages
- RSI
- EMA
- MACD
- forecast visualization

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Stock_AP
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install project dependencies:
```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit app locally:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:
```text
http://localhost:8501
```

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Yahoo Finance
- Statsmodels
- Scikit-learn
- pmdarima

## Data Sources

The project fetches market data using Yahoo Finance (`yfinance`), which provides:
- historical prices
- company metadata
- financial indicators
- ticker-based stock data

## Example Stocks Included

The dashboard includes the following sample companies and ticker codes:

| Company | Code |
|--------|------|
| Apple | AAPL |
| Tesla | TSLA |
| Microsoft | MSFT |
| Amazon | AMZN |
| Alphabet | GOOGL |
| Meta | META |
| NVIDIA | NVDA |
| JPMorgan Chase | JPM |
| Visa | V |
| UnitedHealth | UNH |

## Screenshots

Add screenshots of the app in your GitHub repository to showcase the features.

### Home Page
```text
Place your home page screenshot here
```

### Stock Analysis Page
```text
Place your stock analysis screenshot here
```

### Stock Prediction Page
```text
Place your stock prediction screenshot here
```

> Recommended image names:
> - `screenshots/home.png`
> - `screenshots/stock-analysis.png`
> - `screenshots/stock-prediction.png`

## GitHub Upload Guide

Upload these files and folders to your GitHub repository:

```text
Stock_AP/
├── app.py
├── Home.py
├── README.md
├── requirements.txt
├── pic.jpg
├── pages/
│   ├── __init__.py
│   ├── Stock_Analysis.py
│   ├── Stock_Prediction.py
│   └── utils/
│       ├── __init__.py
│       ├── model_training.py
│       └── plotly_fig.py
├── screenshots/           # optional but recommended for GitHub showcase
│   ├── home.png
│   ├── stock-analysis.png
│   └── stock-prediction.png
└── .gitignore
```

### Recommended upload steps

1. Create a new GitHub repository.
2. Open the project folder in GitHub Desktop or Git Bash.
3. Add all project files.
4. Commit the changes.
5. Push to the remote repository.

### Example Git commands

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

## Future Improvements

- Add more investment metrics and valuation analysis
- Include buy/sell recommendation logic
- Add stock comparison across multiple tickers
- Support more advanced forecasting models
- Show backtesting and model performance analysis
- Add authentication and user-specific watchlists

## License

This project is intended for educational and portfolio-analysis use. Add your preferred license if you plan to publish it publicly.

## Contributor Notes

If you want to extend the project:
- keep the Streamlit page structure simple and modular
- place reusable functions in `pages/utils`
- update this README whenever adding features or new pages
