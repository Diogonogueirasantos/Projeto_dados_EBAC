from ansi2html.style import color
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from plotly.graph_objs.bar import Insidetextfont


class First_Dash:

    def __init__(self):
        self.df = pd.read_csv('ecommerce_estatistica_V1.csv')
        self.graphs_creator()
        self.dash_creator()


    def graphs_creator(self):
        eixo_x = [1834920, 775200, 5394000]
        marca = ['Celi', 'Menina Linda', 'Lupo']

        top3_marcas = ['lupo:masculino', 'stillger jeans:Feminino', 'celi:Unissex']
        top3_marcas_vl = [31, 16, 15]

        self.pie = px.pie(values=eixo_x, names=marca, title='Top Três Marcas Encontradas', hole=0.5,
                          color_discrete_sequence=px.colors.sequential.Purples[4:])
        self.pie.update_traces(
            textposition='outside',
            textinfo='percent+label',
            insidetextfont=dict(color='white', size=14)
        )
        self.bar  = px.bar(x=top3_marcas, y=top3_marcas_vl, color=top3_marcas, title='Representatividade das Marcas',
                           color_discrete_sequence=px.colors.sequential.Purples[4:])

        self.pie.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            font_color='white'
        )

        self.bar.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            font_color='white'
        )


    def dash_creator(self):
        self.app = Dash(__name__)
        self.app.layout = html.Div(className="fundo-cyberpunk",
                                   children=[
            html.H1("Resumo do Relatório: Ecommerce", className="titulo"),
            html.P("Todas as pesquisas do mercado se destinam a busca dos melhores produtos para investimento de mercado!", className="paragrafo"),

            dcc.Graph(
                figure= self.pie,
                id="Top_tres_marcas"
            ),

            dcc.Graph(
                figure=self.bar,
                id="Representatividade_marcas"
            )
       ] )

        self.app.run(debug=True, port=8050)


if __name__ == "__main__": #
    program = First_Dash()
