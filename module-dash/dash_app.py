import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample DataFrame
df = pd.read_csv('gapminder_edited.csv')
# ON ne garde que les valeurs de l'année 2007
df = df[df['year'] == 2007]
# Trier le DataFrame par population de manière décroissante
df = df.sort_values(by="pop", ascending=False)

# Initialize Dash app
app = dash.Dash(__name__)

# Create a list of unique continents
continents = df['continent'].unique()

# Layout
app.layout = html.Div([
    html.H1("Histogram Example"),
    # Dropdown for selecting continent
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': continent, 'value': continent} for continent in continents],
        value=continents[0],  # Default value
        clearable=False
    ),
    dcc.Graph(id="histogram"),
])

# Callback to update the histogram based on selected continent
@app.callback(
    dash.dependencies.Output('histogram', 'figure'),
    [dash.dependencies.Input('continent-dropdown', 'value')]
)
def update_histogram(selected_continent):
    # Filter the DataFrame by the selected continent
    filtered_df = df[df['continent'] == selected_continent]
    # Create the histogram
    return px.histogram(filtered_df, x="country", y="pop", title=f"Population by countries in {selected_continent}")

# Run app
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
