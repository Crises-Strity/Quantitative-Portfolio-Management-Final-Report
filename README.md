# <font color=blue>Final Report</font>
## Quantitative Portfolio Management with **GEC Academy**
***
<font size='5'>Session Outline</font>
* Data Mining
* Strategy Construction 
* Backtesting of Performance
* Measuring Risk and Size Position
* Assessing Impact of Transaction Cost

## What’s inside
- `Final_Report.ipynb` — the primary analysis notebook.
- `data/monthly.csv` — the original dataset used by the notebook.
- `requirements.txt` — Python dependencies inferred from the notebook.
- `LICENSE` — MIT license.
- `.gitignore` — ignores Python/Jupyter/OS cruft.

## Getting started
1. **Clone or download** this repository.
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch Jupyter**:
   ```bash
   jupyter lab  # or: jupyter notebook
   ```
5. Open `Final_Report.ipynb` and run the cells top-to-bottom.

> If your environment is managed (e.g., conda/mamba/poetry), feel free to install the packages listed in `requirements.txt` with your preferred tool.

## Data
Original data lives in `data/monthly.csv`.

### Columns
**AAPL**, **MSFT**, **AMZN**:, **GOOGL**, **META**, **TSLA**, **NVDA**, **BABA**, **TCEHY**, **INTC**, **ADBE**, **NFLX**, **CRM**, **PYPL**, **AMD**, **BIDU**, **CSCO**, **QCOM**, **SQ**, **JD**,  **TWTR**, **TEAM**, **SHOP**, **NOW**, **WDAY**, **SPLK**, **MU**, **NTES**, **VEEV**, **ADSK**, 

### Quick profile (from the uploaded file)
- **Unnamed: 0** — count=92, unique=92
- **AAPL** — count=91, mean=84.9063, std=54.3069, min=21.5044, max=193.9700
- **MSFT** — count=91, mean=164.3259, std=93.4940, min=44.8140, max=340.5400
- **AMZN** — count=91, mean=98.6429, std=44.6812, min=27.6260, max=175.3535
- **GOOGL** — count=91, mean=76.0730, std=32.8083, min=35.1765, max=148.0460
- **META** — count=91, mean=197.6801, std=68.6393, min=93.1600, max=379.3800
- **TSLA** — count=91, mean=109.6666, std=114.9110, min=12.3440, max=381.5867
- **NVDA** — count=91, mean=108.2090, std=97.4387, min=7.1505, max=425.0300
- **BABA** — count=91, mean=153.4145, std=58.5100, min=63.5800, max=304.6900
- **TCEHY** — count=91, mean=43.0979, std=14.7142, min=16.5225, max=81.7784
- **INTC** — count=91, mean=40.0426, std=9.6319, min=24.0825, max=59.3891
- **ADBE** — count=91, mean=313.6151, std=156.3607, min=85.1500, max=669.8500
- **NFLX** — count=91, mean=320.5000, std=150.1768, min=90.0300, max=690.3100
- **CRM** — count=91, mean=157.8815, std=59.9950, min=67.7500, max=299.6900
- **PYPL** — count=91, mean=110.3485, std=69.4017, min=36.1400, max=291.4800
- **AMD** — count=91, mean=50.4298, std=40.6740, min=2.1400, max=158.3700
- **BIDU** — count=91, mean=166.4188, std=46.2169, min=76.5700, max=283.4600
- **CSCO** — count=91, mean=39.3129, std=9.8396, min=18.7946, max=60.0400
- **QCOM** — count=91, mean=86.7659, std=40.2713, min=36.1903, max=176.7582
- **SQ** — count=91, mean=85.7852, std=70.4734, min=8.7700, max=268.0700
- **JD** — count=91, mean=44.6881, std=19.7203, min=20.1338, max=90.2990
- **TWTR** — count=82, mean=34.2287, std=14.7086, min=14.6200, max=77.0600
- **TEAM** — count=91, mean=139.7714, std=101.4136, min=20.7700, max=458.1300
- **SHOP** — count=91, mean=45.9975, std=44.8500, min=2.2380, max=152.4780
- **NOW** — count=91, mean=313.3601, std=188.9914, min=54.9900, max=697.7600
- **WDAY** — count=91, mean=163.9390, std=59.8495, min=60.4500, max=289.9800
- **SPLK** — count=91, mean=109.6031, std=41.8171, min=43.6000, max=219.3300
- **MU** — count=91, mean=48.4573, std=20.9414, min=10.3231, max=92.0708
- **NTES** — count=91, mean=65.8731, std=24.5525, min=24.0166, max=113.9803
- **VEEV** — count=91, mean=149.9126, std=89.7014, min=24.1000, max=332.7100
- **ADSK** — count=91, mean=171.0060, std=72.8014, min=46.8200, max=321.1300

> Note: The above profile is basic and intended as a quick reference. For fuller EDA, see the notebook.

## Notebook
The notebook is designed to be run as-is. If you encounter missing packages, please add them to `requirements.txt` and reinstall.

## Reproducibility tips
- Run cells in order without skipping.
- If the notebook writes output files, they will appear in subfolders created at runtime.
- For exact results, use the same package versions as captured in `requirements.txt`.


## Source code

Reusable functions/classes have been extracted into `src/utils.py`. In your notebook you can do:

```python
from src.utils import load_data  # and any other functions/classes
df = load_data()  # reads data/monthly.csv
```

## License
Released under the MIT License (see `LICENSE`).

## Acknowledgments
If you use this work, please cite the repository or link back to it. Contributions via pull requests are welcome.
