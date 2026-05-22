from layout.buttons import create_buttons
import dash_bootstrap_components as dbc

def estrutura():
    return dbc.Container(
                dbc.Card(
                    dbc.CardBody([
                        dbc.Badge(children='CALCULATOR',color='white',text_color='dark'),
                        dbc.Label(''),
                        dbc.Input(id="text", class_name='d-flex justify-content-end',value=''),
                        create_buttons()
                    ], class_name='bg-light d-flex flex-column'),  
                    class_name='bg-dark p-2',
                    style={'width': '300px'}
                ),
                class_name='d-flex justify-content-center mt-5'
            )
