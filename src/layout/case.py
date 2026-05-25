from layout.buttons import create_buttons
import dash_bootstrap_components as dbc

def estrutura():
    return dbc.Container(
                dbc.Card(
                    dbc.CardBody([
                        dbc.Badge(children='CALCULATOR',color='primary',text_color='dark'),
                        dbc.Row([
                            dbc.Col(
                                dbc.Input(id="text", class_name='d-flex justify-content-left',value='',placeholder='0', readonly=True)
                            ),
                            dbc.Col(
                                dbc.Button('C', id="clear", color="danger",)
                            )
                        ]),
                        create_buttons()
                    ], class_name='bg-primary d-flex flex-column'),  
                    class_name='bg-dark p-2',
                    style={'width': '300px'}
                ),
                class_name='d-flex justify-content-center mt-5'
            )
