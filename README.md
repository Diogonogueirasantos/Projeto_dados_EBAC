# Relatório de Pesquisa de Mercado
![Animação Ecommerce](https://github.com/Diogonogueirasantos/Ecommerce_Projeto_dados_EBAC/blob/main/recursos/animation%20illustration%20GIF%20by%20Tony%20Babel.gif)

**Arte criada por: https://giphy.com/tonybabel**


## Problema de Negócio

O problema de negócio proposto pelas partes interessadas, se define em encontrar opções de melhores produtos vendedidos e para quais públicos os mesmos se destinam.
Para além disso também houve o interesse sobre a **sazonalidade** dos produtos, com isso, também há a questão de encontrar um padrão de compra dada à época do ano.


### Processos utilizados
Toda a pesquisa foi dividida em três partes, sendo a primeira delas voltada para o **pré-processamento** dos dados (para mais informações sobre a decisão de tratamento dos dados consulte [Dicionário de Dados](https://github.com/Diogonogueirasantos/Ecommerce_Projeto_dados_EBAC/blob/main/dicionario.xlsx)). Já a segunda etapa do processo envolveu utilizar o processo EDA para encontrar padrões associados aos três melhores produtos e
compras dados certos períodos do ano. Quanto a terceira é última etapa, esta consistiu em utilizar os achados da análise descritiva para definir através do **modelo de regressão Random Forest** quais produtos, quantidades e públicos-alvo
foram apresentados pelo modelo.


### Achados

A seguir os resultados da pesquisa.

- Três melhores produtos
![Três melhores Produtos](https://github.com/Diogonogueirasantos/Ecommerce_Projeto_dados_EBAC/blob/main/recursos/top_3produtos.png)

- Top três marcas mais representativas
<div align="center">
  <img src="https://github.com/Diogonogueirasantos/Ecommerce_Projeto_dados_EBAC/blob/main/recursos/proporcao_marcas.png" alt="Top Três marcas mais representativas" width="520px">
</div>

- Marcas e seus públicos-alvo
<div align="center">
  <img src="https://github.com/Diogonogueirasantos/Ecommerce_Projeto_dados_EBAC/blob/main/recursos/publico_alvo.png" alt="Público-alvo" width="720px">
</div>

****

### Padrões de Compras em relação a época do ano
Por fim, uma tabela com agrupamentos de dados permitiu entender que, períodos do ano com maior temperatura influênciam um padrão de compra voltada para artigos **fitness**.
Entretando, não há um comportamento de compra para a categória abordada, quanto a climas mais frios.

**Tabela:Padrão comportamental por períodos do ano**
| Produto (Período)                                                                             | count | mean | min | max |
|:----------------------------------------------------------------------------------------------|------:|-----:|----:|----:|
| ('10 Shorts Ginástica Moda Fitness Roupas Femininas Atacado', '6 meses maior temperatura')    |     2 | 190.8| 190.8| 190.8|
| ('2 Conjuntos Ciclista Liso + Top Roupas Femininas Academia', '6 meses maior temperatura')    |     1 | 68.49| 68.49| 68.49|
| ('2 Shorts Iguais Casal Praia 5 Estampas Roupa Combinando', '6 meses maior temperatura')      |     1 | 128.61| 128.61| 128.61|
| ('3 Conjuntos Fitness Feminino Top + Short Roupas Academia A11', '6 meses maior temperatura') |     1 | 104.66| 104.66| 104.66|
| ('4 Short Bermuda Masculina Esporte Dry Fit Academia Plus', '6 meses maior temperatura')      |     1 | 134.92| 134.92| 134.92|
| ('5 Bermudas Fitness Feminina Tapa Bumbum Roupas Academia B05', '6 meses maior temperatura')  |     1 | 132.97| 132.97| 132.97|
| ('5 Shorts Canelado Feminino Shortinho Soltinho Verão Atacado', '6 meses maior temperatura')  |     1 | 69.45| 69.45| 69.45|
| ('5 Shorts De Dormir Algodão Masculino Com Estampas Discreta', 'demanda regular')             |     1 | 122.93| 122.93| 122.93|
| ('Bermuda Esportiva Compressão Anti Assadura Térmica Lupo', '6 meses maior temperatura')      |     1 | 74.93| 74.93| 74.93|
| ('Bermuda Infantil Jeans Masculino Roupa Short Menino', '6 meses maior temperatura')          |     1 | 37.61| 37.61| 37.61|
| ('Bermuda Jeans Stretch Lycra Masculina Plus Size 58 Ao 62', '6 meses maior temperatura')     |     1 | 72.97| 72.97| 72.97|
| ('Bermuda Juvenil Jeans Masculino Roupa Short Menino', '6 meses maior temperatura')           |     1 | 46.42| 46.42| 46.42|
| ('Bermuda Short Jeans Masculino Plus Size 36 Ao 56 Elastano', '6 meses maior temperatura')    |     1 | 74.7 | 74.7 | 74.7 |
| ('Bermuda Slim Curves Leve Compressão Dilady 105203', 'demanda regular')                      |     1 | 42.6 | 42.6 | 42.6 |
| ('Bermuda Térmica Anti Assadura Feminina Shorts Esporte Novo', '6 meses maior temperatura')   |     2 | 37.63| 33.89| 41.37|
| ('Bermuda Térmica Masculina Esportiva Corrida, Academia Treino', '6 meses maior temperatura') |     4 | 36.89| 36.88| 36.92|
| ('Blusa + Calça Térmica Treino Futebol Criança Infantil Fleece', '6 meses menor temperatura') |     1 | 74.13| 74.13| 74.13|
| ('Bolero De Plush Com Tiara Bebe Menina Infantil Várias Cores', '6 meses menor temperatura')  |     1 | 39.81| 39.81| 39.81|
| ('Calça Branca Jeans Feminina Skinny Cintura Alta Com Lycra', '6 meses menor temperatura')    |     1 | 56.15| 56.15| 56.15|
| ('Calça Branca Plus Size Enfermagem Com Lycra Feminina Sarja', '6 meses menor temperatura')   |     1 | 68.42| 68.42| 68.42|
| ('Calça Feminina Jeans Boot Índigo Sawary', '6 meses menor temperatura')                      |     1 | 111.29| 111.29| 111.29|
| ('Calça Feminina Jogger Malha De Viscolycra Esportiva Cós Alto', 'demanda regular')           |     1 | 58.68| 58.68| 58.68|
| ('Calça Feminina Lycra Cintura Alta Empina Bumbum', '6 meses maior temperatura')              |     1 | 67.04| 67.04| 67.04|
| ('Calça Feminina Pantalona Cintura Alta Cós Largo Duna Moda', '6 meses menor temperatura')    |     1 | 59.34| 59.34| 59.34|
| ('Calça Feminina Sarja Mom - 274383 Verde Sawary', '6 meses menor temperatura')               |     1 | 141.35| 141.35| 141.35|
| ('Calça Jeans Cigarrete Feminina Índigo Índigo Sawary Oferta', '6 meses maior temperatura')   |     1 | 73.25| 73.25| 73.25|
| ('Calça Jeans Feminina Boot Cut Índigo Sawary', '6 meses maior temperatura')                  |     1 | 120.34| 120.34| 120.34|
| ('Calça Jeans Feminina Cintura Alta Com Lycra Levanta Bumbum', '6 meses menor temperatura')   |     1 | 140.99| 140.99| 140.99|
| ('Calça Jeans Feminina Flare Cós Alto Levanta Bumbum Hot Pants', '6 meses menor temperatura') |     1 | 65.27| 65.27| 65.27|
| ('Calça Jeans Feminina Plus Size Flare Com Lycra Cintura Alta', '6 meses menor temperatura')  |     1 | 71.52| 71.52| 71.52|
| ('Calça Jeans Feminina Super Lipo Sawary Roupas Femininas', '6 meses menor temperatura')      |     2 | 160.92| 159.67| 162.16|
| ('Calça Jeans Infantil Juvenil Masculina C/ Elastano Mzocokids', '6 meses menor temperatura') |     1 | 56.73| 56.73| 56.73|
| ('Calça Jeans Infantil Masculina Roupa Brim Meninos', 'demanda regular')                      |     1 | 41.67| 41.67| 41.67|
| ('Calça Jeans Infantil Wideleg Destroyed Menina Blogueirinha', '6 meses maior temperatura')   |     1 | 107.6| 107.6| 107.6|
| ('Calça Jeans Original Sawary Com Lycra Roupas Femininas Dins', '6 meses menor temperatura')  |     1 | 150.6| 150.6| 150.6|

