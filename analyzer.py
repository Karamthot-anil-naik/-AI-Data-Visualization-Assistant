import pandas as pd
import numpy as np


def get_column_types(df):
    """
    Identify numerical, categorical and datetime columns.
    """

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    datetime_columns = df.select_dtypes(
        include=["datetime64[ns]", "datetime64[ns, UTC]"]
    ).columns.tolist()

    return {
        "numerical": numerical_columns,
        "categorical": categorical_columns,
        "datetime": datetime_columns
    }


def dataset_profile(df):
    """
    Generate basic dataset profiling information.
    """

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage": round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )
    }

    return profile


def missing_value_summary(df):
    """
    Return missing-value information.
    """

    missing = df.isnull().sum()

    missing_df = pd.DataFrame({
        "column": missing.index,
        "missing_count": missing.values,
        "missing_percentage": (
            missing.values / len(df) * 100
        ).round(2)
    })

    missing_df = missing_df[
        missing_df["missing_count"] > 0
    ]

    return missing_df


def numerical_summary(df):
    """
    Generate statistical summary for numerical columns.
    """

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    if len(numerical_columns) == 0:
        return pd.DataFrame()

    return df[numerical_columns].describe().T


def correlation_matrix(df):
    """
    Generate correlation matrix for numerical columns.
    """

    numerical_df = df.select_dtypes(
        include=np.number
    )

    if numerical_df.shape[1] < 2:
        return pd.DataFrame()

    return numerical_df.corr()


def detect_outliers(df):
    """
    Detect outliers using IQR method.
    """

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    results = []

    for column in numerical_columns:

        series = df[column].dropna()

        if len(series) == 0:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = series[
            (series < lower_bound) |
            (series > upper_bound)
        ]

        results.append({
            "column": column,
            "outliers": len(outliers),
            "outlier_percentage": round(
                len(outliers) / len(series) * 100,
                2
            )
        })

    return pd.DataFrame(results)


def recommend_visualizations(df):
    """
    Recommend visualizations based on column types.
    """

    types = get_column_types(df)

    numerical = types["numerical"]
    categorical = types["categorical"]
    datetime = types["datetime"]

    recommendations = []

    # Numerical vs numerical
    if len(numerical) >= 2:

        recommendations.append({
            "chart": "Scatter Plot",
            "reason": "Useful for analyzing relationships between two numerical variables.",
            "x": numerical[0],
            "y": numerical[1]
        })

    # Numerical distribution
    if len(numerical) >= 1:

        recommendations.append({
            "chart": "Histogram",
            "reason": "Useful for understanding the distribution of numerical values.",
            "column": numerical[0]
        })

        recommendations.append({
            "chart": "Box Plot",
            "reason": "Useful for detecting spread and potential outliers.",
            "column": numerical[0]
        })

    # Categorical vs numerical
    if len(categorical) >= 1 and len(numerical) >= 1:

        recommendations.append({
            "chart": "Bar Chart",
            "reason": "Useful for comparing a numerical measure across categories.",
            "x": categorical[0],
            "y": numerical[0]
        })

        recommendations.append({
            "chart": "Category Box Plot",
            "reason": "Useful for comparing numerical distributions across categories.",
            "x": categorical[0],
            "y": numerical[0]
        })

    # Date vs numerical
    if len(datetime) >= 1 and len(numerical) >= 1:

        recommendations.append({
            "chart": "Line Chart",
            "reason": "Useful for analyzing numerical trends over time.",
            "x": datetime[0],
            "y": numerical[0]
        })

    return recommendations


def analyze_dataset(df):

    return {
        "profile": dataset_profile(df),
        "column_types": get_column_types(df),
        "missing_values": missing_value_summary(df),
        "numerical_summary": numerical_summary(df),
        "correlation": correlation_matrix(df),
        "outliers": detect_outliers(df),
        "recommendations": recommend_visualizations(df)
    }