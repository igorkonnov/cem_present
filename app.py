import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    'cement',
    external_stylesheets=external_stylesheets
)
app.config.suppress_callback_exceptions = True
server = app.server