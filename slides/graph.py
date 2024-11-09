import dash
import pandas as pd
import numpy as np
from app import app
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
from dash.dependencies import Input, Output

df = pd.read_csv('data.csv', sep = ',')
df.rename(columns ={'Unnamed: 0': 'sample №'}, inplace=True)
available_indicators = df.columns

content = html.Div(style=dict(textAlign='center', border='1px'),children=[
    html.H2(id='intro-div'),
    html.Br(),html.Hr([], className = "divider py-0.5 bg-primary"),
    html.Div([html.H4('Cement quality parameters correlation with the compressive\
     strength. Why these parameters selected for predictions?')] ),


    html.Div([
         dbc.Card( dbc.CardBody([

    html.P("The predictors are selected based on correlation coefficient (Pearson\
            correlation), assuming that all parameters are normally distributed,\
            except the dosages of additives. The correlation coefficient tells us\
            about the strength and direction of the linear relationship between\
            independent and target variables. But correlation does not imply\
            causation. Predictors selection requires in-depth knowledge of\
            cement production and cement chemistry as well.", style = dict(textAlign ="left"))]) ) ]),


html.Div([html.H6('Quality  parameaters and trend lines')], className ='row mx-auto py-2'),
html.Div([
    dbc.Col(
    html.Div(
            dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value='SO₃, %'
        )), width={"size": 3, "order": "last", "offset": 12} ),

    dbc.Col(
    html.Div(
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value='2 days MPa'
        )), width={"size": 3, "order": "first", "offset": 3})
], className ="row py-2"),
dcc.Graph(id='indicator-graphic'),

html.Div([html.P("Correlation(absolute values) < 0,1 - no correlation, <0,2-03 - small\
               correlation, <0,3-0,7 - moderate, > 0,7 - strong correlation."
)]),

html.Div([html.H6('Correlation matrix, select parameters:')], className = 'row py-2 mx-auto'),
html.Div ([
 dcc.Checklist(
        id='corrvalues',
        options=[{'label': x, 'value': x} for x in df.columns],
        value=df.columns.tolist(),
        inputStyle={"margin-right": "20px", "margin-left": "20px" }
    ),
    dcc.Graph(id="graph")
])
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'))

def update_graph(xaxis_column_name, yaxis_column_name):
    corr = round( df[xaxis_column_name].corr(df[yaxis_column_name]),3)
    fig = px.scatter(df,x= xaxis_column_name, y=yaxis_column_name, trendline
     = "lowess", color = yaxis_column_name )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode
    ='closest')
    fig.update_xaxes(title=xaxis_column_name)
    fig.update_yaxes(title=yaxis_column_name)
    fig.add_annotation( xref="x domain",
    yref="y domain", x =0.1, y = 0.90, text = (f"correlation coefficient:{corr}"),
      showarrow=False, font=dict(family="Courier New, monospace",size=16,
            color="#0275d8"),
        align="center",
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="white",
        opacity=0.8)
    return fig

@app.callback(
    Output("graph", "figure"),
    [Input("corrvalues", "value")])
def filter_heatmap(cols):
    z = round( df[cols].corr(),2)
    fig = ff.create_annotated_heatmap(z.values, x = z.columns.to_list(),
    y =z.index.to_list(),colorscale='Viridis')
    return fig
