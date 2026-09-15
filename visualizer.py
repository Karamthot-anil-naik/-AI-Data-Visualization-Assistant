import plotly.express as px


def clean_layout(fig):
    """
    Apply a consistent, clean style to all charts.
    """

    fig.update_layout(
        template="plotly_white",
        height=500,

        # Chart title
        title={
            "font": {
                "size": 20,
                "family": "Arial",
                "weight": "normal"
            }
        },

        # Axis titles
        xaxis={
            "title": {
                "font": {
                    "size": 14,
                    "family": "Arial",
                    "weight": "normal"
                }
            },
            "tickfont": {
                "size": 12,
                "family": "Arial"
            }
        },

        yaxis={
            "title": {
                "font": {
                    "size": 14,
                    "family": "Arial",
                    "weight": "normal"
                }
            },
            "tickfont": {
                "size": 12,
                "family": "Arial"
            }
        },

        # Legend
        legend={
            "font": {
                "size": 12,
                "family": "Arial"
            }
        },

        # Margins
        margin={
            "l": 60,
            "r": 30,
            "t": 70,
            "b": 60
        }
    )

    return fig


def scatter_plot(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        title=f"{y} vs {x}",
        trendline="ols"
    )

    return clean_layout(fig)


def bar_chart(df, x, y):

    grouped = (
        df.groupby(x, dropna=False)[y]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        grouped,
        x=x,
        y=y,
        title=f"Average {y} by {x}"
    )

    return clean_layout(fig)


def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}",
        marginal="box"
    )

    return clean_layout(fig)


def box_plot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"Distribution of {column}"
    )

    return clean_layout(fig)


def category_box_plot(df, x, y):

    fig = px.box(
        df,
        x=x,
        y=y,
        title=f"{y} Distribution by {x}"
    )

    return clean_layout(fig)


def line_chart(df, x, y):

    sorted_df = df.sort_values(x)

    fig = px.line(
        sorted_df,
        x=x,
        y=y,
        title=f"{y} over {x}"
    )

    return clean_layout(fig)


def correlation_heatmap(df):

    correlation = df.select_dtypes(
        include="number"
    ).corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        title="Correlation Matrix",
        aspect="auto"
    )

    return clean_layout(fig)