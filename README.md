# Machine Learning Engineer Nanodegree
# Capstone Project
## Categorização de Produtos

### Instalação

Este projeto utiliza **Python** e necessita das seguintes bibliotecas instaladas:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)
- [missingno](https://github.com/ResidentMario/missingno)

Também é necessário ter instalado um software que possa executar um [Jupyter Notebook](http://ipython.org/notebook.html). Recomenda-se o pacote [Anaconda](https://www.anaconda.com/download/).

### Código

O código está na pasta `\notebook`:
- `product_categorization.ipynb`: o notebook propriamente dito.
- `graphics.py`: módulo para gráficos.
- `HierarchicalClassifier.py`: classificador hierárquico.
- `SingleClassClassifier.py`: classificador para classe única.
- `stopwords.py`: stop words para pt-br (não utilizado no trabalho).

### Execução

Em um terminal ou prompt de comando, navegue até o diretório `\notebook` e execute um dos seguintes comandos:

```bash
ipython notebook product_categorization.ipynb
```  
or
```bash
jupyter notebook product_categorization.ipynb
```

Isto abrirá o software Jupyter Notebook software e o arquivo do projeto no seu navegador.

### Dados

Os dados originais, disponibilizados pela [Best Buy](https://github.com/BestBuy/api-playground), estão em `\data`,  no formato sqlite.

Por conveniência, os dados transformados em csv foram movidos para `\notebook\products.csv`.

### Relatório

O relatório final se encontra em `\doc`, com o nome `Capstone Project - Machine Learning Engineer Nanodegree.pdf`.

Neste diretório pode ser encontrado também a proposta inicial (`proposal.pdf`) e arquivos de suporte.