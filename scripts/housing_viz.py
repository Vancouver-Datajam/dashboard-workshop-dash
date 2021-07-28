import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from jupyter_dash import JupyterDash
import pandas as pd

import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

import data_cleaning  

#------------------------------------ read in the data ---------------------------------------------------
data = "./data/"
level = 'Province'
# mortgage data
data_file = data + "average-value-new-mortgage-loans-ca-prov-cmas-2012-q3-2020-q3-en.xlsx"
df_mortgage = data_cleaning.data_prep(data_file)
df_mortgage_long = data_cleaning.slice_data(df_mortgage, level = level)

# income data
data_income = data + "real-average-household-income-after-taxes-tenure-2006-2018-en.xlsx"
df_income = data_cleaning.data_prep(data_income)
df_income_long = data_cleaning.slice_data(df_income, level = level)

# combine 2 data set
df_mortgage_income = data_cleaning.combine_data(df_mortgage, df_income)

#-------------------------------------- APP section ------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1("Housing graphs"),
        dcc.Dropdown(
            id='province',
            options=[{'label': i, 'value': i} for i in df_mortgage_long['Geography'].unique()],
            value= 'Newfoundland'
        )
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(id='graph-mortgage', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='graph-mortgage-income', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])



@app.callback(
    Output('graph-mortgage', 'figure'),
    Input('province', 'value'))
def update_figure(selected_province):
    df = df_mortgage_long
    filtered_df = df[df['Geography'] == selected_province]

    fig1 = px.line(filtered_df, x="Time", y="value", 
                  title = f'Line plot of mortgage loans in {selected_province}', 
                  hover_name="value")
    fig1.update_xaxes(tickangle=-45)
    fig1.update_layout(transition_duration=500)

    return fig1


@app.callback(
    Output('graph-mortgage-income', 'figure'),
    Input('province', 'value'))
def mortgage_income(selected_province):
    df = df_mortgage_income
        
    fig2 = px.scatter(df.Income[selected_province]/df.Mortgage[selected_province]*100, 
                      title = f'Time series of income/mortgage in {selected_province}',
                     hover_name='value')
    return fig2

#-----------------------------------------------------------------------
if __name__ == '__main__':  
    app.run_server(mode='inline')  # 'inline' so that we don't have to open a new browser
