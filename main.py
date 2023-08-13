from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df_airports = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv"
)

app = Dash(__name__)
#app.title("SR Test App")

server = app.server

app.layout = html.Div(
    [
        dcc.Graph(id="graph"),
        html.P(
            "Enter the type of graph you want to plot: (scatter_geo or scatter_mapbox)"
        ),
        dcc.Dropdown(
            id="type",
            options=["scatter_mapbox", "scatter_geo"],
            value="scatter_mapbox",
            clearable=False,
        ),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("type", "value"),
)
    
def generate_chart(values):
    fig = px.scatter_mapbox(
        df_airports,
        lat="lat",
        lon="long",
        hover_data=["airport", "city", "state", "cnt"],
        size="cnt",
        color="cnt",
        zoom=3 )
    fig.update_layout(mapbox_style="open-street-map")
    
    # Set the size of the plot
    fig.update_layout(width=1000, height=1000)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
