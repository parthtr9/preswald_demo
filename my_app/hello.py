import pandas as pd
import plotly.express as px
from preswald import get_df, plotly, table, text

text("# My Data Analysis App")

data = pd.read_csv('data/sample.csv')
data["value"] = pd.to_numeric(data["value"], errors="coerce")
data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")

text("# All of the sample data")

table(data)

filtered_data = data[data["value"] > 50]

text("# Filtered Data (Value > 50)")

table(filtered_data)

text("# Data Analysis Visualizations: scatter and bar plots")
text("## Item Value Comparison Bar Plot")
# Bar plot: Item vs VALUE
fig_value = px.bar(
    filtered_data,
    x="item",
    y="value",
    title="Item Value Comparison",
    color="value",
    text="value",
)
plotly(fig_value)

text('# Now with new data: train.csv from titanic dataset')

train_data = pd.read_csv('data/train.csv')

table(train_data)



text("## Age Distribution Histogram")
fig_age = px.histogram(
    train_data,
    x="Age",
    title="Age Distribution of Passengers",
    nbins=30,
)
plotly(fig_age)

text("# Titanic Dataset Analysis")
text("## Passenger Class Distribution Bar Plot")
fig_class = px.bar(
    train_data,
    x="Pclass",
    title="Passenger Class Distribution",
    color="Pclass",
    text="Pclass",
)
plotly(fig_class)

# Query: Show all female passengers who survived and are under 30 years old
query_result = train_data.query("Sex == 'female' and Survived == 1 and Age < 30")
text("## Female Survivors Under 30")
table(query_result)

