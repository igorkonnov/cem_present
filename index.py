# main.py

import importlib
import os
import sys

from dash import dcc, html  # Updated import for Dash components
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app  # Import the initialized Dash app
from presentation import slide_order  # Import slide order from your presentation module

# -----------------------------------
# Dynamically Import Slide Modules
# -----------------------------------

# Path to the 'slides' directory
slides_path = os.path.join(os.getcwd(), 'slides')

# Iterate through all Python files in the 'slides' directory
for filename in os.listdir(slides_path):
    slide_name, ext = os.path.splitext(filename)
    if slide_name in slide_order and ext == '.py':  # Ensure only relevant Python files are imported
        module_name = f'slides.{slide_name}'
        if module_name not in sys.modules:
            globals()[f'slide_{slide_name}'] = importlib.import_module(module_name)
            print(f"Imported {module_name}")
        else:
            print(f"Module {module_name} already imported")

# -----------------------------------
# Helper Functions
# -----------------------------------

def slide_dict():
    """
    Create a mapping from slide name to its index.
    Includes a mapping for the root path '/'.
    """
    return {v: k for k, v in enumerate(slide_order)} | {'/': 0}

nav_style = {
    'textAlign': 'center',
}

def nav_button_div(text):
    """
    Helper function to create navigation buttons with consistent styling.
    """
    return html.Div(
        children=[
            dbc.Button(
                html.H4(text),
                style={'width': '100%'},
                color='primary',
                outline=True,
            )
        ],
        className="shadow-lg rounded mb-2"
    )

# -----------------------------------
# Layout Definition
# -----------------------------------

app.layout = html.Div(
    style={'background-image': 'url("/assets/6.jpg")', 'background-size': 'cover'},  # Ensure background image covers the entire div
    children=[
        dbc.Container(
            children=html.Div([
                # URL component to handle page routing
                dcc.Location(id='url', refresh=False),

                # Navigation Bar
                dbc.Container(
                    fluid=True,
                    children=[
                        # Hidden div to store the current slide state
                        html.Div(id='current-slide', style={'display': 'none'}, children=''),

                        # Navigation Row
                        dbc.Row(
                            style={'height': 'auto', 'position': 'sticky', 'top': 0, 'margin': '10px'},  # Added 'top' for sticky positioning
                            children=[
                                # Previous Button
                                dbc.Col(
                                    width=4,
                                    style=nav_style,
                                    children=[
                                        dcc.Link(
                                            id='previous-link',
                                            href='',
                                            children=nav_button_div('<< Previous'),
                                        ),
                                    ]
                                ),

                                # Slide Count Dropdown
                                dbc.Col(
                                    width=4,
                                    style={'textAlign': 'center'},
                                    children=[
                                        dbc.DropdownMenu(
                                            label='Select Slide',  # Improved label for better UX
                                            id='slide-count',
                                            children=[
                                                dbc.DropdownMenuItem(
                                                    s,
                                                    href='/' + s,
                                                )
                                                for s in slide_order
                                            ]
                                        )
                                    ]
                                ),

                                # Next Button
                                dbc.Col(
                                    width=4,
                                    style=nav_style,
                                    children=[
                                        dcc.Link(
                                            id='next-link',
                                            href='',
                                            children=nav_button_div('Next >>'),
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    style={'position': 'relative', 'zIndex': '10000'}  # Ensure the navbar stays on top
                ),

                # Slide Content Area
                html.Div(id='page-content'),

                # Footer Section
                html.Div(
                    html.Footer(html.Hr(className="divider bg-primary")),
                    style={'marginTop': '35rem'}
                ),

                # Optional Debug Output (Uncomment if using the debug callback)
                # html.Div(id='debug-output')  # Ensure this div is present if using the debug callback

            ])
        )
    ]
)

# -----------------------------------
# Callback Definitions
# -----------------------------------

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')],
)
def change_slide(pathname):
    """
    Display the content of the current slide based on the URL pathname.
    Returns '404 - Slide Not Found' if the slide does not exist.
    """
    if pathname in [None, '/', '/' + slide_order[0]]:
        return globals()[f'slide_{slide_order[0]}'].content
    else:
        try:
            slide_name = pathname.strip('/').split('/')[0]
            return globals()[f'slide_{slide_name}'].content
        except KeyError:
            return '404 - Slide Not Found'

@app.callback(
    [Output('next-link', 'href'),
     Output('previous-link', 'href')],
    [Input('current-slide', 'children')],
    [State('url', 'pathname')]
)
def navigate(current_slide, pathname):
    """
    Update the 'Next' and 'Previous' navigation links based on the current slide.
    """
    slides = slide_dict()
    current_order = slides.get(current_slide, 0)
    num_slides = len(slide_order) - 1

    # Determine previous slide
    if current_order > 0:
        previous_slide = slide_order[current_order - 1]
    else:
        previous_slide = slide_order[0]  # Stay on the first slide if at the beginning

    # Determine next slide
    if current_order < num_slides:
        next_slide = slide_order[current_order + 1]
    else:
        next_slide = slide_order[-1]  # Stay on the last slide if at the end

    previous_href = '/' + previous_slide
    next_href = '/' + next_slide

    return next_href, previous_href

@app.callback(
    Output('current-slide', 'children'),
    [Input('url', 'pathname')]
)
def set_slide_state(pathname):
    """
    Update the hidden 'current-slide' div based on the URL pathname.
    """
    if pathname is None:
        return '/'
    return pathname.strip('/') if pathname != '/' else '/'

@app.callback(
    Output('slide-count', 'label'),
    [Input('current-slide', 'children')]
)
def update_slide_count(current_slide):
    """
    Update the label of the slide count dropdown to show the current slide number out of the total.
    """
    slides = slide_dict()
    total = len(slide_order)
    current = slides.get(current_slide, 0) + 1
    return f'{current}/{total}'

# -----------------------------------
# Optional: Debugging Callback
# -----------------------------------

# Uncomment the following callback and the corresponding div in the layout if you wish to use debugging features.

# @app.callback(
#     Output('debug-output', 'children'),
#     [Input('url', 'pathname')]
# )
# def debug_callbacks(pathname):
#     """
#     Debugging function to display registered callbacks.
#     """
#     callback_info = []
#     for callback_id, callback in app.callback_map.items():
#         outputs = callback['outputs']
#         if isinstance(outputs, list):
#             output_ids = [output['id'] for output in outputs]
#         else:
#             output_ids = [outputs['id']]
#         callback_info.append(f"Callback '{callback_id}' outputs to {output_ids}")
#     return html.Pre('\n'.join(callback_info))

# -----------------------------------
# Run the Dash App
# -----------------------------------

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8052))
    app.run_server(
        host='0.0.0.0',
        port=port,
        debug=False,  # Set to False in production
        dev_tools_ui=True,
        dev_tools_props_check=True
    )
