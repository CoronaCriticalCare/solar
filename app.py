from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from services.analyzer import *
from api.nasa import *


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Solar Weather"), width=15, className="text-center my-5")
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Classes", className="card-title text-center"),
                    dcc.Graph(id="classification")
                ])
            ])
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Strongest Flare", className="card-title text-center"),
                    html.Div(id="strongest")
                ])
            ])
        ])

    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Events for the past 30 days", className="card-title text-center"),
                    html.Div(id="event_count")
                ])
            ])
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Flare Information", className="card-title text-center"),
                    dag.AgGrid(
                        id="flare_table",
                        columnDefs=[
                            {"field": "classType", "headerName": "Class"},
                            {"field": "beginTime", "headerName": "Begin Time"},
                            {"field": "peakTime", "headerName": "Peak Time"},
                            {"field": "endTime", "headerName": "End Time"}
                        ],
                        defaultColDef={
                            "sortable": True,
                            "filter": True,
                            "resizable": True,
                        },
                        style={
                            "height": "400px",
                            "width": "100%"
                        }
                    )
                ])
            ])
        ], width=12)
    ])
])

@app.callback(
    Output("classification", "figure"),
    Input("classification", "id")
)

def update_classification(_):
    data = get_solar()
    classes = get_flare_classes(data)
    class_counts = pd.Series(classes).value_counts()

    fig = px.bar(
        x=class_counts.index,
        y=class_counts.values,
        labels={
            "x": "Flare Class",
            "y": "Number of Events"
        }
    )

    return fig

@app.callback(
    Output("strongest", "children"),
    Input("strongest", "id")
)

def update_strongest(_):
    data = get_solar()
    strongest = get_strongest(data)

    return dbc.Card(
        dbc.Card([
            html.H1(
                strongest["classType"],
                className="text-center"
            ),
            html.H5(
                strongest["flrID"],
                strongest["sourceLocation"],
                className="text-center"
            ),
            html.Hr(),
            html.P(
                f"Peak Time: {strongest['peakTime']}",
                className="text-center"
            )
        ])
    )

@app.callback(
    Output("event_count", "children"),
    Input("event_count", "id")
)

def update_event_count(_):
    data = get_solar()

    return dbc.Card(
        dbc.CardBody([
            html.H1(
                str(len(data)),
                className="text-center"
            ),
            html.H5("Total Linked Events",
                    className="text-center"
            )
        ])
    )

@app.callback(
    Output("flare_table", "rowData"),
    Input("flare_table", "id")
)

def update_flare_table(_):
    data = get_solar()

    return data

if __name__ == "__main__":
    app.run(debug=True)