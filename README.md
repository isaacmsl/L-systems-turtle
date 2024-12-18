# L-System Drawer Manager

Este projeto implementa um sistema para desenhar L-Systems (sistemas de Lindenmayer) usando a biblioteca turtle do Python.

## Requisitos
- Python 3.x
- turtle
- ipykernel (opcional)

## Instalação

    $ git clone https://github.com/isaacmsl/L-systems-turtle.git
    $ cd L-systems-turtle

Instale os requisitos do projeto, execute o comando:

    $ pip install -e requiriments.txt

## Como usar?
#### Tutorial mostrando como utilizar o pacote `lsdm`
Consulte o arquivo, `tutorial.ipynb`

#### Usando pelo terminal 
O script `drawer.py` permite que você gere e desenhe uma **L-System** a partir de um arquivo de entrada e de parâmetros especificados na linha de comando.

Parâmetros de Linha de Comando
- **file**: Caminho para o arquivo de entrada que contém a definição da L-System.
- **iterations**: Número de iterações para gerar a cadeia da L-System.
- **trace**: Indica se o usuário deseja ver o desenho sendo feito (opcional, padrão é False).

**Exemplos**

1. Executando com parâmetros
```sh
$ python drawer.py --path <lsys-path> --iterations 3
```

2. Executando sem parâmetros
```sh
$ python drawer.py <lsys-path> 3
```

3. Executando sem parâmetros e configurando para ver o desenho sendo feito
```sh
$ python drawer.py <lsys-path> 3 --trace
```