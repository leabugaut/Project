#!/usr/bin/env python3

import numpy as np
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
from pathlib import Path
import subprocess
import datetime as dt
import plotly.express as px

# Création de l'interface dashboard
app = dash.Dash(__name__)
app.title = "Population française"

# Layout du dashboard
app.layout = html.Div(children=[
    html.H1("Population française", style={"text-align": "center", "color":"blue"}),
    html.P("Pendant l'année 2023, la population française devrait augmenter de 297 388 personnes pour atteindre 66 383 596 au début de l'année 2024. L'augmentation naturelle devrait être positive, car le nombre de naissances dépassera le nombre de décès de 228 658. Si la migration externe reste au même niveau que l'année précédente, la population augmentera de 68 730 en raison de raisons liées à la migration. Cela signifie que le nombre de personnes qui s'installent en France (et qui ne sont pas originaires du pays) en tant que résidents permanents (immigrants) l'emportera sur le nombre de personnes qui quittent le pays pour s'installer définitivement dans un autre pays (émigrants)"), 
    html.Div(id="data-update", style = {"color":"blue", 'font-weight': 'bold'}),
    dcc.Interval(id="interval-component", interval=60*1000, n_intervals=0),
    html.H2("Evolution de la population française en temps réel : ", style = {"color":"blue"}),
    dcc.Graph(id="graph-update"),


], style={'backgroundColor': '#B0E0E6'})


# Fonction pour mettre à jour les données du dashboard 
@app.callback(
    dash.dependencies.Output("data-update", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)


# Lecture du fichier csv pour récupérer les dernières données 
def data_retrieval(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop']]
    last_pop = df['pop'].iloc[-1]
    return f'Dernière population enregistrée : {last_pop}'

@app.callback(
    dash.dependencies.Output("graph-update", "figure"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

# Mise à jour du graph
def graph_update(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop']]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    fig=px.line(df, x="timestamp", y="pop")
    fig.update_layout(template="ggplot2")
    return fig


# Exécution du dashboard  
if __name__ == '__main__':
   app.run_server(host='0.0.0.0', port=8050, debug=True)


