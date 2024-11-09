
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', sep = ',')
df.rename(columns ={'Unnamed: 0': 'sample №'}, inplace=True)


description = pd.DataFrame({'Name': ['2 days MPa','R 008, %', 'SO₃, %',
'additive 1', 'additive 2', 't, cement, ° С',  'moisture,%',
'Free_lime,%','limestone,%', 'Eq.Na2O,%', 'LOI, %', 'C3S,%', 'C3A,%'],

'Description' :['2 days compressive strength, the quality target parameter',\
'sieve residue, cement fineness  indicator','SO3 content in cement','quality improver\
(dosage g/t), additive  with the ability to increase 2D compressive strength',\
'cement additive-grinding  aid, trialed over several days' ,\
'temperature collected after mill outlet', 'cement moisture measured on collected\
 samples', 'free lime of clinker', 'filler, supplementary material',
'alkali content', 'lost of ignition', 'tricalcium silicate', 'tricalcium aluminate'
]})

content = html.Div(style=dict(textAlign='center', border='1px'),children=[

    html.H2(id='intro-div'),
    html.Br(),html.Hr([], className = "divider py-0.5 bg-primary"),
    html.Div([html.H4('Cement quality parameters and cement additives')], className ='py-2'),

html.Div([
     dbc.Card( dbc.CardBody([

         html.P("The data used was collected\
                    from an existing decommissioned cement\
                    plant. The dataset is prepared for analysis, and missing parameters\
                    are replaced by mean values. Cement type produced – CEM I 42,5N.The plants main\
                    quality target is 2 days compressive strength.", style = dict(textAlign ="left"))]) ) ]),


    html.Div([( html.H6 ('The dataset:'))],className = 'row mx-auto py-2'),

    html.Div([dash_table.DataTable(id = 'id', data = df.to_dict("records"),
     columns = [{"id": c, "name": c, "selectable": True} for c in  df.columns],
    style_header={ "backgroundColor": "#1E90FF", "fontWeight": "bold","color": "white",
    'textAlign': 'center'
    },  fixed_rows={"headers": True},style_cell={"width": "70px", "fontSize": "8pt",
    'textAlign': 'center'},

        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 5,
)]),

    html.Div([html.H6('This is description of each parameter : ')], className
     = 'row mx-auto py-2'),
    html.Div([dash_table.DataTable(id = 'id2', data = description.to_dict("records"),
     columns = [{"id": c, "name": c, "selectable": True} for c in  description.columns],
    style_header={ "backgroundColor": "#1E90FF", "fontWeight": "bold","color"
    : "white",'textAlign':'center'
    },fixed_rows={"headers": True},style_cell={"width": "70px", 'textAlign': 'left'},
)]),

   html.Div(style = dict(textAlign ='left'), children = [
        html.P('Further there are other variables that can also influence\
                cement hydration kinetics. The data for these parameters was not\
                available in the dataset used for building these models.'),

  ], className = 'row mx-auto py-2'),
])
