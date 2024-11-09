# Necessary imports - do not change, and include on every slide
from dash import html, dcc
from app import app
import dash_bootstrap_components as dbc

###

content = html.Div(
    style={"textAlign": "center"},
    children=[
        dbc.Card(
            style={"backgroundColor": "#e8f4ff", "marginTop": "6rem"},
            children=[
                dbc.CardBody(
                    [
                        html.Div([html.H4("Introduction")], className="py-2"),

                        html.Div(
                            style={"textAlign": "left", "fontSize": 17},
                            children=[
                                html.P(
                                    "Artificial Intelligence (AI) has long been utilized across various industries. "
                                    "Even the traditionally conservative construction industry is adopting AI for control "
                                    "and process optimization."
                                ),
                                html.P(
                                    "However, AI remains a somewhat exotic tool for widespread use. Its sporadic application "
                                    "and slow implementation are likely due to misunderstandings and misinterpretations of AI "
                                    "and Machine Learning (ML). Marketers and journalists often exaggerate the complexity and "
                                    "capabilities of machine learning algorithms, making modern AI seem far from being "
                                    "self-learning and self-developing intelligence."
                                ),
                                html.P(
                                    "ML is merely a subset of AI, primarily used for prediction and classification. Despite its "
                                    "complexity, ML offers unique opportunities for cement producers, such as predicting cement "
                                    "quality. Currently, engineers largely rely on rules of thumb and manual calculations in Excel. "
                                    "ML enables more accurate predictions of cement quality by minimizing human error. There's no "
                                    "need to be an IT expert; training a model can involve just a single line of Python code or a "
                                    "node in a KNIME app. However, parameter selection, data cleaning, analysis, and model tuning are "
                                    "more complex, requiring knowledge of cement production, statistics, and the ML paradigm."
                                ),
                                html.P(
                                    "While there are numerous articles and discussions about using machine learning to predict cement "
                                    "quality, there hasn't been a complete online application available. To pursue ML certification, "
                                    "I developed this web application to demonstrate how different models predict outcomes using a real "
                                    "dataset and apply these predictions to the cement additives business."
                                ),
                            ],
                        ),
                    ]
                )
            ],
            className="shadow-lg p-3 rounded",
        )
    ],
)
