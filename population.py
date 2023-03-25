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


    html.Br(),
    html.H3("Evolution de la population masculine en France en temps réel : ",  style = {"color":"blue"}),
    html.Div(id="data-update-m", style = {"color":"blue", 'font-weight': 'bold'}),
    dcc.Graph(id="graph-update-m"), 

    html.Br(),
    html.H4("Evolution de la population féminine en France en temps réel : ",  style = {"color":"blue"}),
    html.Div(id="data-update-f", style = {"color":"blue", 'font-weight': 'bold'}),
    dcc.Graph(id="graph-update-f"),
    
    html.Br(),
    html.Div(id="data-update-bytd", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-btoday", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-dytd", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-dtoday", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-mytd", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-mtoday", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-pgytd", style = {"color":"blue", 'font-weight': 'bold'}),
    html.Div(id="data-update-pop-growth", style = {"color":"blue", 'font-weight': 'bold'}),



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


# Population masculine 
@app.callback(
    dash.dependencies.Output("data-update-m", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_m(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop_m']]
    last_pop = df['pop_m'].iloc[-1]
    return f'Dernière population masculine enregistrée : {last_pop}'

@app.callback(
    dash.dependencies.Output("graph-update-m", "figure"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def graph_update_m(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop_m']]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    fig=px.line(df, x="timestamp", y="pop_m")
    fig.update_layout(template="ggplot2")
    return fig

# Population féminine 
@app.callback(
    dash.dependencies.Output("data-update-f", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_f(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop_f']]
    last_pop = df['pop_f'].iloc[-1]
    return f'Dernière population féminine enregistrée : {last_pop}'

@app.callback(
    dash.dependencies.Output("graph-update-f", "figure"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def graph_update_f(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'pop_f']]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    fig=px.line(df, x="timestamp", y="pop_f")
    fig.update_layout(template="ggplot2")
    return fig

# Nombre de naissances depuis l'année dernière
@app.callback(
    dash.dependencies.Output("data-update-bytd", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_bytd(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'bytd']]
    last_pop = df['bytd'].iloc[-1]
    return f'Nombre de naissances enregistrées depuis 1 an : {last_pop}'

# Nombre de naissances aujourd'hui
@app.callback(
    dash.dependencies.Output("data-update-btoday", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_btoday(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'btoday']]
    last_pop = df['btoday'].iloc[-1]
    return f"Nombre de naissances aujourd'hui : {last_pop}"

# Nombre de morts depuis l'année dernière

@app.callback(
    dash.dependencies.Output("data-update-dytd", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_dytd(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'dytd']]
    last_pop = df['dytd'].iloc[-1]
    return f"Nombre de morts depuis l'année dernière : {last_pop}"

# Nombre de morts aujourd'hui 

@app.callback(
    dash.dependencies.Output("data-update-dtoday", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_dtoday(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'dtoday']]
    last_pop = df['dtoday'].iloc[-1]
    return f"Nombre de morts aujourd'hui : {last_pop}"

# Migration depuis l'année dernière

@app.callback(
    dash.dependencies.Output("data-update-mytd", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_mytd(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'mytd']]
    last_pop = df['mytd'].iloc[-1]
    return f"Migrations depuis l'année dernière : {last_pop}"

# Migrations aujourd'hui 

@app.callback(
    dash.dependencies.Output("data-update-mtoday", "children"),
    dash.dependencies.Input("interval-component", "n_intervals")
)

def data_retrieval_mtoday(n):
    df = pd.read_csv('data.csv')
    df = df.loc[:, ['timestamp', 'mtoday']]
    last_pop = df['mtoday'].iloc[-1]
    return f"Migrations aujourd'hui : {last_pop}"


# Exécution du dashboard  
if __name__ == '__main__':
   app.run_server(host='0.0.0.0', port=8050, debug=True)


# Exécution du dashboard  
if __name__ == '__main__':
   app.run_server(host='0.0.0.0', port=8050, debug=True)


