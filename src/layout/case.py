from layout.buttons import create_buttons
import dash_bootstrap_components as dbc

def estrutura():
    return dbc.Container(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Badge(children='CALCULATOR',color='white',text_color='dark'),
                        dbc.Input(type='text', class_name='center'),
                        dbc.Label(''),
                        dbc.Col(
                        [
                        dbc.Col(dbc.ButtonGroup([dbc.Button('7'),dbc.Button('8'),dbc.Button('9'),dbc.Button('/')],class_name='w-100 p-1')),
                        dbc.Col(dbc.ButtonGroup([dbc.Button('4'),dbc.Button('5'),dbc.Button('6'),dbc.Button('*')],class_name='w-100 p-1')),
                        dbc.Col(dbc.ButtonGroup([dbc.Button('1'),dbc.Button('2'),dbc.Button('3'),dbc.Button('-')],class_name='w-100 p-1')),
                        dbc.Col(dbc.ButtonGroup([dbc.Button('0'),dbc.Button('.'),dbc.Button('='),dbc.Button('+')],class_name='w-100 p-1')),
                        ],className='g-2',
                        create_buttons()
                        ),
                        
                        
                    ],
                    
                    class_name='bg-light d-flex flex-column'
                ),
                class_name='bg-dark p-2',
                style={'width': '300px'}
            ),  
        ],
        class_name='d-flex justify-content-center mt-5'
    )
