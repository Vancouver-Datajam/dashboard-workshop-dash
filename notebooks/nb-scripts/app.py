
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def graph_region(region_df, graph_type: str, dimension1: str, dimension2: str) -> None:
    """
    Parameters
    ----------
        region_df: (dataframe object) reshaped data frame object with mortage, delinquency and population data
        graph_type: (string) "box", "violin", "scatter", "line"
        dimension1: (str) one of 'Time' or 'Geography'
        dimension2: (str) one of 'AverageMortgageAmount', 'AverageMortgageAmount' or 'PopulationSize'
        
    Returns:
    --------
        None
    """
    
    plot_dict = {'box': px.box,'violin': px.violin, 'scatter': px.scatter, 'line':px.line}
        
    try:
        # Initialize function
        fig = plot_dict[graph_type](region_df, 
                                    x=dimension1, 
                                    y=dimension2, 
                                    color = "Geography",
                                   hover_name = "Time")
        # Format figure 
        title_string = f'Chart: {graph_type} plot of {dimension1} and {dimension2} by Geography'
        fig.update_layout(title = title_string)
        fig.update_xaxes(tickangle=-45)
        return fig
    
    except KeyError:
        print("Key not found. Make sure that 'graph_type' is in ['box','violin', 'scatter', 'line']")
    except ValueError:
        print("Dimension is not valid. dimension1 is one of 'Time' or 'Geography'")
        print("dimension2 is one of 'AverageMortgageAmount', 'DelinquencyRate', 'PopulationSize'")
        
# ----------------------------------------------------------------------------------#
# Read data

url = 'https://raw.githubusercontent.com/Vancouver-Datajam/dashboard-workshop-dash/main/data/delinquency_mortgage_population_2021_2020.csv'
data_pop_del_mort_df = pd.read_csv(url, index_col=0)

# ----------------------------------------------------------------------------------#
# App section        
        

# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# ----------------------------------------------------------------------------------#
# A dropdown menu and a chart

app.layout = html.Div([
             # This div contains a header H1, a dropdown to select the kind of plot and the plot
            html.H1("Different kinds of plots"),
            dcc.Dropdown(
                        id='graph-type',
                        options=[{'label': 'Violin plot', 'value': 'violin'},
                                {'label': 'Box plot', 'value': 'box'}],
                        value= 'box'),
            dcc.Graph(id='graph-render')

        
])

@app.callback(
    Output('graph-render', 'figure'),
    Input('graph-type', 'value'))
def update_figure0(selected_graph):
    filtered_df = data_pop_del_mort_df
    fig0 = graph_region(filtered_df, selected_graph, "Geography", "AverageMortgageAmount")
    return fig0
# ----------------------------------------------------------------------------------#

    
# ----------------------------------------------------------------------------------#
# Improving aesthetics, dropdown that changes three graphs

# app.layout = html.Div([
#     html.Div(
#         className="six columns",
#         children = [
#             html.H1("Housing graphs"),
#                 dcc.Dropdown(
#                     id='province',
#                     options=[{'label': i, 'value': i} for i in data_pop_del_mort_df['Geography'].unique()],
#                     value= 'Newfoundland'
#                 ),
            
#             html.Div([
#                    dcc.Graph(id='graph-time-mortgage')
#                     ], className="six columns"),
            
#             html.Div([
#                 dcc.Graph(id='graph-time-del')
#                 ], className="six columns"),
            
#             ]),
    
#     html.Div(
#         className="six columns",
#         children = [
#             html.Div([
#             dcc.Graph(id='scatter-mortgage-del')
#             ]),
#         ])
# ])


    
# @app.callback(
#     Output('graph-time-mortgage', 'figure'),
#     Input('province', 'value'))
# def update_figure1(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]
#     fig1 = graph_region(filtered_df, 'line', "Time", "AverageMortgageAmount")
#     return fig1

# @app.callback(
#     Output('graph-time-del', 'figure'),
#     Input('province', 'value'))
# def update_figure2(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig2 = graph_region(filtered_df, 'line', "Time", "DelinquencyRate")
#     return fig2

# @app.callback(
#     Output('scatter-mortgage-del', 'figure'),
#     Input('province', 'value'))
# def update_figure3(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig3 = graph_region(filtered_df, 'scatter', "AverageMortgageAmount", "DelinquencyRate")
#     return fig3

# ----------------------------------------------------------------------------------#
# text_style = {
#     'textAlign' : 'center',
#     'color' : "black"
# }

# card_text_style = {
#     'textAlign' : 'center',
#     'color' : 'black'
# }
    
# app.layout = html.Div([
#     html.Div([
#         html.H2("Housing Market Trends in Vancouver (quarterly, 2012 - 2020)", style=card_text_style),
#         html.Div([
            
#             dcc.Dropdown(
#                 id='xaxis-column',
#                 options=[{'label': 'Geography', 'value': 'Geography'},
#                          {'label': 'Time', 'value': 'Time'},
#                         {'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='Geography'
#             ),
#             dcc.Dropdown(
#                 id='yaxis-column',
#                 options=[{'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='PopulationSize'
#             ),
            
#         ]),
        
#         html.Div([
#             dcc.Checklist(
#                 id='graph-type',
#                 options=[{'label': 'Violin plot', 'value': 'violin'},
#                          {'label': 'Box plot', 'value': 'box'},
#                         {'label': 'Scatter plot', 'value': 'scatter'},
#                         {'label': 'Line plot', 'value': 'line'}],
#                 value=['violin']
#             )
#         ])
#     ]),

#     dcc.Graph(id='indicator-graphic'),

    
# ])

# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     Input('graph-type', 'value'),
#     Input('xaxis-column', 'value'),
#     Input('yaxis-column', 'value'))
# def update_figure3(selected_graph, xaxis, yaxis):
#     filtered_df = data_pop_del_mort_df
#     fig3 = graph_region(filtered_df, selected_graph[0], xaxis, yaxis)
#     return fig3

# ----------------------------------------------------------------------------------#

if __name__ == '__main__':  
    
    app.run_server(debug=True) 
