from layout.buttons import create_buttons
import dash_bootstrap_components as dbc

def estrutura():
    content=dbc.Container(
        dbc.Card(
            dbc.CardBody([
                dbc.Badge(children='CALCULATOR',color='primary',text_color='dark',class_name='d-flex justify-content-left m-1 p-1'),
                dbc.Row([
                    dbc.Col(dbc.Input(id="text", class_name='w-100 d-flex justify-content-left me-1',value='',placeholder='0', readonly=True), width=8),
                    dbc.Col(dbc.Button('C', id="clear", color="danger",class_name='w-100'), width=4)
                ]),
                create_buttons()
            ], class_name='bg-primary d-flex flex-column'),  
            class_name='bg-dark p-1',
            style={'width': '300px'}
        ),
        class_name='d-flex justify-content-center mt-4'
    )
    return content

