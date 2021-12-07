#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:49:27 2021

@author: sean
"""
import dash
import dash_html_components as html
import pandas as pd
import dash_cytoscape as cyto

nodes_1 = pd.read_csv('data/got-s1-nodes.csv', low_memory=False)
edges_1 = pd.read_csv('data/got-s1-edges.csv', low_memory=False)

def create_cyto_graph(nodeData, edgeData):
    nodes_list = list()
    for i in range(len(nodeData)):
        node = {
                "data": {"id": nodeData.iloc[i,0], 
                         "label": nodeData.iloc[i,1]}
                
            }
        nodes_list.append(node)
    
    edges_list = list()
    for j in range(len(edges_1)):
        edge = {
                "data": {"source": edges_1.iloc[j,0], 
                         "target": edges_1.iloc[j,1],
                         "weight": edges_1.iloc[j,2]}
            }
        edges_list.append(edge)
    
    elements = nodes_list + edges_list
    return elements

elements = create_cyto_graph(nodes_1, edges_1)

default_stylesheet=[
            {'selector': 'node',
                'style': {
                        'width': '20',
                        'height': '20',
                        'background-color': 'blue',
                        'content': 'data(label)',
                        'font-size': '40px',
                        'text-outline-color': 'white',
                        'text-outline-opacity': '1',
                        'text-outline-width': '8px',
                    }
                },
            {'selector': 'edge',
                'style': {
                        'line-color': 'black'
                    }
                }
        ]

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
                cyto.Cytoscape(
                    id='cyto-graph',
                    className='net-obj',
                    elements=elements,
                    style={'width':'80%', 'height':'600px'},
                    layout={'name': 'cose',
                            'padding': '200',
                            'nodeRepulsion': '7000',
                            'gravityRange': '6.0',
                            'nestingFactor': '0.8',
                            'edgeElasticity': '50',
                            'idealEdgeLength': '200',
                            'nodeDimensionsIncludeLabels': 'true',
                            'numIter': '6000',
                            },
                    stylesheet=default_stylesheet
                    )
                ])

if __name__ == "__main__":
    app.run_server(debug=True)