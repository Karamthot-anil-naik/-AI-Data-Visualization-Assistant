# 📊 AI Data Visualization Assistant

An AI-powered data visualization assistant that allows users to upload CSV or Excel datasets, automatically analyze the data, recommend suitable visualizations, generate interactive charts, and ask questions about their dataset using natural language.

## AI API setup

The app uses Ollama Cloud and does not require a local Ollama installation or a downloaded model.

Install dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
OLLAMA_API_KEY=your_ollama_api_key_here
OLLAMA_MODEL=gpt-oss:20b
```

Start the app:

```bash
streamlit run app.py
```

Set `OLLAMA_MODEL` to another model available in your Ollama Cloud account when needed.



# 📌 Project Overview

Data visualization is an important part of data analysis. However, selecting the right visualization and understanding a new dataset can take significant time.

The **AI Data Visualization Assistant** automates this process.

Users can upload a dataset and the application automatically:

- Profiles the dataset
- Detects column types
- Identifies missing values
- Detects duplicate rows
- Recommends suitable visualizations
- Generates interactive charts
- Performs correlation analysis
- Generates AI-powered dataset insights
- Accepts natural-language questions about the dataset
- Generates visualizations from natural-language requests

The project combines **Data Science, Generative AI, LLMs, Pandas, Plotly, and Streamlit** into one application.

---

# ✨ Features

## 📁 1. Dataset Upload

The application supports:

- CSV files
- Excel files (`.xlsx`)

Users can upload their dataset directly through the Streamlit interface.

---

## 🔍 2. Automatic Dataset Profiling

The application automatically analyzes:

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Memory usage
- Column data types

Example:

```text
Rows: 24
Columns: 10
Missing Values: 8
Duplicate Rows: 0
```

---

## 🔍 3. Column Type Detection

The application automatically identifies different types of columns:

### Numerical Columns

Examples:

```text
Order ID
Quantity
Unit Price
Total Sales
```

### Categorical Columns

Examples:

```text
Product
Category
Customer
Region
Payment Method
```

### Datetime Columns

Examples:

```text
Date
```

This information is used to determine which visualizations are suitable for the dataset.

---

## 🤖 4. AI-Powered Visualization Recommendations

The system analyzes the dataset structure and recommends suitable visualizations.

Supported visualizations include:

- Scatter Plot
- Histogram
- Box Plot
- Bar Chart
- Category Box Plot
- Line Chart
- Correlation Analysis

Example:

```text
Numerical + Numerical
        ↓
   Scatter Plot

Categorical + Numerical
        ↓
     Bar Chart

Datetime + Numerical
        ↓
     Line Chart

Numerical Distribution
        ↓
    Histogram
```

---

## 📊 5. Automatic Visualizations

The application automatically generates interactive Plotly visualizations from the uploaded dataset.

Supported charts include:

- Scatter Plot
- Histogram
- Box Plot
- Bar Chart
- Category Box Plot
- Line Chart
- Correlation Heatmap

The generated charts are interactive and allow users to:

- Hover over data points
- Zoom
- Pan
- Explore values
- Reset the view

---

## 📈 6. Correlation Analysis

The application performs correlation analysis between numerical variables.

This helps identify relationships between variables and can help users understand which features may have stronger or weaker relationships.

Example:

```text
Quantity
   ↕
Total Sales

Unit Price
   ↕
Total Sales
```

A correlation heatmap can be generated to visualize these relationships.

---

## 🧠 7. AI-Powered Dataset Insights

The application can generate AI-powered insights based on the uploaded dataset.

The AI can provide:

- Dataset summaries
- Important patterns
- Relationships between variables
- Data-quality observations
- Potential outliers
- Visualization suggestions
- Further analysis recommendations

Example:

```text
The dataset contains 24 records and 10 columns.

Total Sales varies across different categories.
Quantity and Total Sales can be further analyzed
using a scatter plot to identify their relationship.
```

---

## 💬 8. Ask Your Dataset

Users can interact with their dataset using natural language.

Example questions:

```text
Show me the relationship between Quantity and Total Sales.
```

```text
Show sales by Category.
```

```text
What is the distribution of Unit Price?
```

```text
Compare Total Sales across different Regions.
```

The AI interprets the question and selects an appropriate visualization.

### Natural Language Visualization Pipeline

```text
User Question
      ↓
AI / LLM
      ↓
Understand User Intent
      ↓
Identify Dataset Columns
      ↓
Select Visualization
      ↓
Validate Request
      ↓
Plotly
      ↓
Interactive Chart
```

---

# 🏗️ Project Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │    Streamlit    │
                  │      app.py     │
                  └────────┬────────┘
                           │
                           ▼
                  Upload CSV / Excel
                           │
                           ▼
                  ┌─────────────────┐
                  │   analyzer.py   │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
         Data Profiling  Statistics  Column Detection
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                  Visualization Logic
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      ┌────────────────┐       ┌────────────────┐
      │ visualizer.py  │       │  ai_agent.py   │
      │                │       │                │
      │     Plotly     │       │     Ollama     │
      └────────┬───────┘       └────────┬───────┘
               │                        │
               └───────────┬────────────┘
                           ▼
                 Interactive Visualizations
                           +
                     AI Dataset Insights
```

---

# 📂 Project Structure

```text
ai-data-visualization-assistant/
│
├── app.py
├── analyzer.py
├── visualizer.py
├── ai_agent.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── AI Dataset Insights.png
├── Ask Your Dataset.png
├── Correlation Analysis.png
├── Recommended Visualizations.png
├── automatic-visualization1.png
├── automatic-visualization2.png
├── automatic-visualization3.png
├── automatic-visualization4.png
├── automatic-visualization5.png
├── automatic-visualization6.png
├── dataset overview.png
├── dataset preview.png
└── upload dashboard.png
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Plotly

## Generative AI

- Ollama
- Large Language Model

## Web Application

- Streamlit

## Excel Processing

- OpenPyXL

## Statistical Analysis

- Statsmodels

---

# 📦 Requirements

The main dependencies used in this project are:

```text
streamlit
pandas
numpy
plotly
openpyxl
statsmodels
ollama
python-dotenv
```

These dependencies are also included in:

```text
requirements.txt
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-data-visualization-assistant.git
```

Navigate to the project directory:

```bash
cd ai-data-visualization-assistant
```

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you are using `uv`:

```bash
uv pip install -r requirements.txt
```

---

# 🤖 Ollama Setup

The AI features use **Ollama Cloud** through the Ollama API. A local Ollama installation and model download are not required.

## 1. Create an Ollama API key

Create an API key in your Ollama account, then add it to the `.env` file in the project root:

```env
OLLAMA_API_KEY=your_ollama_api_key_here
OLLAMA_MODEL=gpt-oss:20b
```

Set `OLLAMA_MODEL` to another model available in your Ollama Cloud account if needed. The application sends requests to `https://ollama.com` using the API key.

---

# ▶️ Run the Application

After installing the dependencies, run:

```bash
streamlit run app.py
```

Or with `uv`:

```bash
uv run streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🔄 Application Workflow

```text
1. Upload Dataset
        ↓
2. Preview Dataset
        ↓
3. Analyze Dataset
        ↓
4. Detect Column Types
        ↓
5. Check Missing Values
        ↓
6. Check Duplicate Rows
        ↓
7. Recommend Visualizations
        ↓
8. Generate Interactive Charts
        ↓
9. Generate AI Insights
        ↓
10. Ask Questions About Dataset
```

---

# 📸 Screenshots

## 🏠 Dashboard & Dataset Upload

Upload CSV or Excel files directly into the application.

![Upload Dashboard](upload%20dashboard.png)

---

## 📋 Dataset Preview

Preview the uploaded dataset before performing analysis.

![Dataset Preview](dataset%20preview.png)

---

## 🔍 Dataset Overview

The application provides an overview of the dataset including:

- Rows
- Columns
- Missing values
- Duplicate rows
- Numerical columns
- Categorical columns
- Datetime columns

![Dataset Overview](dataset%20overview.png)

---

## 🤖 Recommended Visualizations

The application recommends suitable visualizations based on the dataset.

![Recommended Visualizations](Recommended%20Visualizations.png)

---

## 📊 Automatic Visualization 1

![Automatic Visualization 1](automatic-visualization1.png)

---

## 📊 Automatic Visualization 2

![Automatic Visualization 2](automatic-visualization2.png)

---

## 📊 Automatic Visualization 3

![Automatic Visualization 3](automatic-visualization3.png)

---

## 📊 Automatic Visualization 4

![Automatic Visualization 4](automatic-visualization4.png)

---

## 📊 Automatic Visualization 5

![Automatic Visualization 5](automatic-visualization5.png)

---

## 📊 Automatic Visualization 6

![Automatic Visualization 6](automatic-visualization6.png)

---

## 📈 Correlation Analysis

Analyze relationships between numerical variables.

![Correlation Analysis](Correlation%20Analysis.png)

---

## 🧠 AI Dataset Insights

Generate AI-powered insights from the uploaded dataset.

![AI Dataset Insights](AI%20Dataset%20Insights.png)

---

## 💬 Ask Your Dataset

Ask questions about your dataset using natural language.

Example:

```text
Show me the relationship between Quantity and Total Sales.
```

![Ask Your Dataset](Ask%20Your%20Dataset.png)

---

# 🧪 Example Use Case

Suppose a user uploads:

```text
sales_data.xlsx
```

The application analyzes the dataset:

```text
Rows: 24
Columns: 10

Numerical:
- Order ID
- Quantity
- Unit Price
- Total Sales

Categorical:
- Product
- Category
- Customer
- Region
- Payment Method

Datetime:
- Date
```

The application can then recommend:

```text
Scatter Plot
Histogram
Box Plot
Bar Chart
Line Chart
Correlation Analysis
```

The user can also ask:

```text
Show me the relationship between Quantity and Total Sales.
```

The AI processes the request and generates an appropriate visualization.

---

# 🧠 AI Visualization Generation

The AI does not directly generate or execute Python plotting code.

Instead, the LLM produces a structured visualization request.

Example:

```json
{
    "chart_type": "scatter",
    "x": "Quantity",
    "y": "Total Sales"
}
```

The application validates the requested columns and then uses the visualization engine to generate the chart.

This approach helps separate:

```text
AI Reasoning
      ↓
Structured Request
      ↓
Validation
      ↓
Visualization Engine
      ↓
Plotly Chart
```

---

# 🔐 Security

Important project security practices include:

- API keys should not be hardcoded
- `.env` files should not be uploaded to GitHub
- `.venv` should not be committed
- AI-generated requests should be validated before being used
- Dataset columns should be checked before visualization generation

Example `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
.env
.streamlit/
```

---

# 🚀 Future Improvements

Future versions could include:

- [ ] Automatic dashboard generation
- [ ] More visualization types
- [ ] Advanced statistical analysis
- [ ] Automatic outlier detection
- [ ] AI-powered anomaly detection
- [ ] AI-powered feature engineering suggestions
- [ ] Download charts as PNG
- [ ] Export analysis as PDF
- [ ] Export charts as HTML
- [ ] Dataset comparison
- [ ] Chat history
- [ ] User authentication
- [ ] Support for larger datasets
- [ ] Cloud LLM support
- [ ] Improved visualization recommendations
- [ ] Automated EDA reports

---

# 🎯 Use Cases

This application can be useful for:

- Data Analysts
- Data Scientists
- Business Analysts
- Students
- Researchers
- Beginners learning Data Science
- Exploratory Data Analysis

The goal is to reduce the time required to understand a new dataset and select useful visualizations.

---

# ⭐ Key Highlights

```text
✔ CSV and Excel support
✔ Automated dataset profiling
✔ Column type detection
✔ Missing-value analysis
✔ Duplicate detection
✔ AI visualization recommendations
✔ Interactive Plotly charts
✔ Correlation analysis
✔ AI-generated dataset insights
✔ Natural-language dataset interaction
✔ Natural-language visualization generation
✔ Local LLM support using Ollama
✔ Streamlit web application
```

---

# 📊 Skills Demonstrated

This project demonstrates practical experience with:

- Python
- Pandas
- NumPy
- Data Analysis
- Exploratory Data Analysis
- Data Visualization
- Plotly
- Streamlit
- Generative AI
- LLM Integration
- Natural Language Processing
- Prompt Engineering
- Data Profiling
- Statistical Analysis

---

# 👨‍💻 Author

## Karamthot Anil Naik

**B.Tech Computer Science & Engineering**

### Areas of Interest

- Data Science
- Machine Learning
- Generative AI
- NLP
- Data Analytics
- Python
- SQL
- Power BI

---

# ⭐ If You Find This Project Useful

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
