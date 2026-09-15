import streamlit as st
import pandas as pd

from analyzer import analyze_dataset

from visualizer import (
    scatter_plot,
    bar_chart,
    histogram,
    box_plot,
    category_box_plot,
    line_chart,
    correlation_heatmap
)

from ai_agent import (
    generate_dataset_insights,
    generate_chart_recommendation,
    explain_chart
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Data Visualization Assistant",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 AI Data Visualization Assistant")
st.write("Upload your dataset and let the AI recommend visualizations and insights.")
st.write("Developed by Karamthot Anil Naik ")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.header("Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)





# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

if uploaded_file is None:

    st.info(
        " Please upload a CSV or Excel dataset ."
    )

    st.stop()


try:

    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_excel(uploaded_file)

except Exception as e:

    st.error(f"Unable to read the dataset: {e}")

    st.stop()


# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.header("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)


# --------------------------------------------------
# ANALYZE DATA
# --------------------------------------------------

analysis = analyze_dataset(df)

profile = analysis["profile"]
column_types = analysis["column_types"]
recommendations = analysis["recommendations"]


# --------------------------------------------------
# DATASET METRICS
# --------------------------------------------------

st.header("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Rows</div>
        <div class="metric-value">{profile["rows"]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Columns</div>
        <div class="metric-value">{profile["columns"]}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Missing Values</div>
        <div class="metric-value">{profile["missing_values"]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Duplicate Rows</div>
        <div class="metric-value">{profile["duplicate_rows"]:,}</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# COLUMN TYPES
# --------------------------------------------------

st.header("🔍 Column Analysis")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Numerical")

    st.write(
        column_types["numerical"]
    )

with col2:

    st.subheader("Categorical")

    st.write(
        column_types["categorical"]
    )

with col3:

    st.subheader("Datetime")

    st.write(
        column_types["datetime"]
    )


# --------------------------------------------------
# MISSING VALUES
# --------------------------------------------------

if not analysis["missing_values"].empty:

    st.header("⚠️ Missing Values")

    st.dataframe(
        analysis["missing_values"],
        use_container_width=True
    )

else:

    st.success("No missing values detected.")


# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

st.header("🤖 Recommended Visualizations")

for recommendation in recommendations:

    st.info(
        f"""
**{recommendation['chart']}**

{recommendation['reason']}
"""
    )


# --------------------------------------------------
# AUTOMATIC CHARTS
# --------------------------------------------------

st.header("📈 Automatic Visualizations")

numerical = column_types["numerical"]
categorical = column_types["categorical"]
datetime_columns = column_types["datetime"]


# Scatter
if len(numerical) >= 2:

    st.subheader(
        f"🔵 {numerical[1]} vs {numerical[0]}"
    )

    fig = scatter_plot(
        df,
        numerical[0],
        numerical[1]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Histogram
if len(numerical) >= 1:

    st.subheader(
        f"📊 Distribution of {numerical[0]}"
    )

    fig = histogram(
        df,
        numerical[0]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Box plot
if len(numerical) >= 1:

    st.subheader(
        f"📦 Box Plot — {numerical[0]}"
    )

    fig = box_plot(
        df,
        numerical[0]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Category box plot
if len(categorical) >= 1 and len(numerical) >= 1:

    st.subheader(
        f"📦 {numerical[0]} by {categorical[0]}"
    )

    fig = category_box_plot(
        df,
        categorical[0],
        numerical[0]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Bar chart
if len(categorical) >= 1 and len(numerical) >= 1:

    st.subheader(
        f"📊 Average {numerical[0]} by {categorical[0]}"
    )

    fig = bar_chart(
        df,
        categorical[0],
        numerical[0]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Line chart
if len(datetime_columns) >= 1 and len(numerical) >= 1:

    st.subheader(
        f"📈 {numerical[0]} over time"
    )

    fig = line_chart(
        df,
        datetime_columns[0],
        numerical[0]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------------------------
# CORRELATION
# --------------------------------------------------

if len(numerical) >= 2:

    st.header("🔥 Correlation Analysis")

    fig = correlation_heatmap(df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------------------------
# AI INSIGHTS
# --------------------------------------------------

st.header("🧠 AI Dataset Insights")

if st.button("Generate AI Insights"):

    with st.spinner("AI is analyzing your dataset..."):

        try:

            insights = generate_dataset_insights(
                profile,
                recommendations
            )

            st.markdown(insights)

        except Exception as e:

            st.error(
                f"AI error: {e}"
            )


# --------------------------------------------------
# CHAT WITH DATASET
# --------------------------------------------------

st.header("💬 Ask Your Dataset")

question = st.text_input(
    "Example: Show me the relationship between age and salary"
)


if st.button("Generate Visualization"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "AI is understanding your request..."
        ):

            dataset_info = {
                "columns": df.columns.tolist(),
                "numerical_columns": numerical,
                "categorical_columns": categorical,
                "datetime_columns": datetime_columns
            }

            result = generate_chart_recommendation(
                dataset_info,
                question
            )

        st.subheader("🤖 AI Recommendation")

        st.json(result)

        chart_type = result.get("chart_type")
        x = result.get("x")
        y = result.get("y")

        try:

            if chart_type == "scatter":

                fig = scatter_plot(
                    df,
                    x,
                    y
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            elif chart_type == "bar":

                fig = bar_chart(
                    df,
                    x,
                    y
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            elif chart_type == "histogram":

                fig = histogram(
                    df,
                    x
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            elif chart_type == "box":

                fig = box_plot(
                    df,
                    x
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.warning(
                    "The AI returned an unsupported chart type."
                )

        except Exception as e:

            st.error(
                f"Could not generate chart: {e}"
            )