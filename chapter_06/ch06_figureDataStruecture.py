if __name__ == "__main__":
    
    from dash import Dash, dcc, html, Input, Output
    import plotly.express as px
    import json

    fig = px.line(
        x=["rubin", "jiyoung", 'kiwon'],  y=[95, 98, 99],       # replace with my own data source
        title ="Python Exam Score", height=325
    )
    
    app = Dash(__name__)

    app.layout = html.Div([
        html.H4("Displaying figure structure as JSON"),
        dcc.Graph(id="graph", figure=fig),
        dcc.Clipboard(target_id="structure"),
        html.Pre(
            id = 'structure',
            style={
                'boarder' : 'thin lightgrey solid',
                'overflow' : 'scroll',
                'height' : '275px'
            }
        )
    ])

    @app.callback(
        Output("structure", "children"),
        Input("graph", "figure"))
    def display_structure(fig_json):
        return json.dumps(fig_json, indent=2)

    app.run_server(debug=True)