# 🤖 AI-Powered Data Analyst

An end-to-end AI-powered data analytics application built with **Python, Pandas, Streamlit, and Generative AI**.

The application helps users transform raw CSV datasets into a structured analytics workflow through an interactive web application.

---

## 🚀 Project Overview

Traditional data analysis often requires multiple separate tools and manual steps for data cleaning, quality checking, profiling, analysis, and insight generation.

This project brings these stages together into a single interactive application.

The user can upload a CSV dataset, process and clean the data, evaluate its quality, perform analysis, generate AI-assisted insights, and download the cleaned dataset.

---

## ✨ Key Features

- 📁 Upload CSV datasets
- 🧹 Automated data cleaning
- 🛡️ Data quality assessment
- 📊 Dataset profiling
- 📈 Statistical analysis
- 📅 Date-based analysis
- 🔎 Categorical analysis
- 💡 AI-assisted insight generation
- 📥 Download cleaned datasets
- 🌐 Interactive web interface
- 🔄 End-to-end analytics workflow

---

## 🏗️ Application Workflow

```text
             CSV Dataset
                  │
                  ▼
          📁 Data Upload
                  │
                  ▼
          🧹 Data Cleaning
                  │
                  ▼
        🛡️ Data Quality Checks
                  │
                  ▼
        📊 Dataset Profiling
                  │
                  ▼
          📈 Data Analysis
                  │
                  ▼
         💡 AI-Assisted Insights
                  │
                  ▼
       📥 Download Cleaned Data
```

---

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/eswar235/AI_Data_Analyst.git
   cd AI_Data_Analyst
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Quick Start

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, visit the URL manually

3. **Start analyzing**
   - Click "Upload Your Dataset"
   - Select a CSV or Excel file
   - Follow the interactive workflow

---

## 📦 Project Structure

```
AI_Data_Analyst/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── src/
│   ├── ai_engine.py         # AI analysis engine
│   ├── insights_engine.py   # Business insights generator
│   ├── data_query_engine.py # Dataset querying
│   ├── date_analysis.py     # Temporal analysis
│   ├── categorical_analysis.py # Category analysis
│   ├── dataset_profiler.py  # Dataset profiling
│   └── ...
└── assets/                   # Images and resources
```

---

## 🎯 Usage Examples

### Example 1: Basic Data Analysis
1. Upload `sample_sales.csv`
2. Click "Clean Dataset"
3. Review statistics and visualizations
4. Ask questions about your data

### Example 2: Generate Insights
1. Upload your dataset
2. Click "Generate Business Insights"
3. Get AI-powered analysis
4. Download cleaned data

---

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the root directory (optional):
```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
```

### Streamlit Configuration
Configuration files are in `.streamlit/config.toml`

---

## 📊 Supported File Types

- CSV (.csv)
- Excel (.xlsx, .xls)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Bethamsetty Eswar**
- GitHub: [@eswar235](https://github.com/eswar235)
- Email: eswarbethamsetty235@gmail.com

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Data processing with [Pandas](https://pandas.pydata.org/)
- Visualizations with [Plotly](https://plotly.com/)

---

## 📧 Support

For support, email eswarbethamsetty235@gmail.com or open an issue on GitHub.

---

## 🚀 Deployment

This app can be deployed on:
- [Streamlit Cloud](https://streamlit.io/cloud) (Free)
- [Heroku](https://www.heroku.com/)
- [AWS](https://aws.amazon.com/)
- [DigitalOcean](https://www.digitalocean.com/)

---

**Made with ❤️ by [Bethamsetty Eswar]**