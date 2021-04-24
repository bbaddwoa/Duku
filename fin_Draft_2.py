# -*- coding: utf-8 -*-
"""

Created on Sat Apr 17 11:45:34 2021

@author: Adwoa Osei-Yeboah

Building A Dashboard to Compare Two Players in One Team 
"""

# Packages imported
import dash
import dash_core_components as dcc   # to add graphs/plots
import dash_html_components as html
from dash.dependencies import Input, Output 
import plotly.express as px
import pandas as pd
import dash_table 


# Setting display parameters for pandas to see the data frames completely when printed 
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 100) 




# Gives background color
stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']  # generic


# pandas dataframe to html table (template that will be used everytime)
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# Initializing a dashboard called app
app = dash.Dash(__name__, external_stylesheets=stylesheet) 
                                # stylesheet gives the color as shown in line 21

# Creating a dataframe from your dataset
team_csv = pd.read_csv('export_team.csv')
df = team_csv
df5 = df.set_index('Player') 

player1_csv = pd.read_csv('export_player1.csv') 
df1 = player1_csv

player2_csv = pd.read_csv('export_player2.csv')
df2 = player2_csv

compare_players = pd.read_csv('ComparePlayers.csv')
df3 = compare_players 

# for dropdown names
name_dict = [{'label' : player, 'value' : player} for player in df.Player]

# for side by side bar plot
bar_df = df[['Player', 'Reb', 'P', 'Ast']]
'''
Reb1 = bar_df['Reb'][0]   #49
Reb2 = bar_df['Reb'][3]   #75
Pnt1 = bar_df['P'][0]     #172
Pnt2 = bar_df['P'][3]     #101
Ast1 = bar_df['Ast'][0]   #29
Ast2 = bar_df['Ast'][3]   #22
'''
for player in df5.index:
    player1 = player
    player2 = player

#u = df.loc[player1, ['Reb', 'P', 'Ast']]


#fig = px.bar(df, x=df.Player, y=df.Min , color = df.Player, title = 'Comparing The 2020 Season Average Minutes Played Per Game For Albany Great Danes Players  ' )


# Dashboard layout     * Div --> 1 division 
app.layout = html.Div([ 
    
    html.H1('Comparing NCAAW Players In A Team ', style={'textAlign': 'center'}),
    
    html.A('Click here to go to NCAAW ', href='https://sports.yahoo.com/college-womens-basketball/',
           target='_blank'),
    
   
    dcc.Graph(
    
    figure={
        'data':[
            {'x' :['Rebounds' , 'Points', 'Assists' ]  ,'y': df5.loc[player1, ['Reb', 'P', 'Ast']] , 'type': 'bar', 'name': player1},
            {'x' :['Rebounds' , 'Points', 'Assists' ]  ,'y': df5.loc[player2, ['Reb', 'P', 'Ast']], 'type': 'bar', 'name': player2},
            ],
        'layout':{
            'title': 'Comparing 2020 Season Average Rebounds, Points & Assist Between Player 1 and Player 2 ',
            'xlabel': 'Date',
            'ylabel': ' Average Rebounds' 
            }
        },
    id = "graph1"
    
    ),

    html.H5("Introduction : "),
    html.P("The National Collegiate Athletic Association (NCAA) Women Division 1 Basketball Tournament has 64 teams. This dashboard is comparing players within a team. The graph is comparing three scores of two players. The table summarizes the scores for these two players." , 
                 style={'width': '50%'} ),    
       
    
      
    html.Div([html.H5("Select Player 1: "),
              dcc.Dropdown(options = name_dict,                          
                           id='my-dropdown1',
                           value='Helene Haegerstrand',
                           style={'width': '64%'}) 
              ]),
    
   html.Div([html.H5("Select Player 2: "),
              dcc.Dropdown(options = name_dict,                           
                           id='my-dropdown2',
                           value='Lucia Decortes',
                           style={'width': '64%'}) 
              ]), 
      
    
    html.Div(id="table_div", style={'width': '70%'}),

    
    html.H5("Reference: "),
    html.P('https://sports.yahoo.com/ncaaw/teams/albany/roster', 
                 style={'width': '45%'} ),    
    
    ])



# defining what is connected on the dash board 
@app.callback(
    Output(component_id='graph1', component_property="figure"),
    [Input(component_id='my-dropdown1', component_property='value'),
     Input(component_id='my-dropdown2', component_property='value')]
    
)
# The function is going to take some value name called text (from  type = text ich is going to be a str)
def update_figure(player1, player2):
    #get data f
    fig={
        'data':[
            {'x' :['Rebounds' , 'Points', 'Assists' ]  ,'y': df5.loc[player1, ['Reb', 'P', 'Ast']] , 'type': 'bar', 'name': player1},
            {'x' :['Rebounds' , 'Points', 'Assists' ]  ,'y': df5.loc[player2, ['Reb', 'P', 'Ast']], 'type': 'bar', 'name': player2},
            ],
        'layout':{
            'title': "Comparing 2020 Season Average Rebounds, Points & Assist for "  + player1 + " and "  + player2 + ".",
            'xlabel': 'Date',
            'ylabel': ' Average Rebounds' 
            }
        }
    return fig # return the string entered and it goes into the output component property box ie Player1 


@app.callback(
    Output(component_id="table_div", component_property="children"),
    [Input(component_id='my-dropdown1', component_property='value'),
     Input(component_id='my-dropdown2', component_property='value')])



def update_table(player1, player2):
    x = df[df.Player.isin([player1, player2])]#.sort_values('df.Player')
    return generate_table(x)

server = app.server 

# running the dashboard. debug = True --> running in debug mode 
if __name__ == '__main__':
    app.run_server(debug=False)  
