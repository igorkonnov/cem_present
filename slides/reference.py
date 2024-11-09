# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
###

content = html.Div(style=dict(textAlign='center'),children=[
    dbc.Card(style = dict(backgroundColor ='#e8f4ff', marginTop ="8rem"), children = [
    dbc.Card(dbc.CardBody([
    html.Div([html.H4("References :")], className = 'py-2'),

   html.Div(style=dict(textAlign='left', fontSize = 20), children = [

       html.A("1.The application framework.", href = 'https://plotly.com/dash/',  className='row'),
       html.A("2.The idea of interactive presentation.", href =' https://github.com/russellromney/dash-slides', className='row'),
       html.A("3.ML model.", href='https://scikit-learn.org/stable/', className = 'row'),
       html.A("4.Hosting.", href=' https://www.digitalocean.com/',className = 'row'),
       html.A ("5.Manual how to serve the application.", href = 'https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04', className='row'),
       html.A("6.Chemistry cement and concrete.", href ='https://play.google.com/books/reader?id=v1JVu4iifnMC&pg=GBS.PP1', className='row'),
       html.A("7.Because Data is the new oil and gold, I don't share the dataset :(",
       href ='https://www.hindustantimes.com/india-news/data-is-the-new-oil-new-gold-says-pm-modi-in-houston/story-SphHDPQadvF1dJRMXHCkwK.html',className='row'),
       html.A("BR Konnov I", className='row')




   ])  ], ))  ], className = 'shadow-lg p-3 mb-2  rounded')
]),
