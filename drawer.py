import argparse
from lsdm import LSystemDrawerMenager

def main():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser(description='Processa um arquivo de configuração de L-System e desenha a representação.')
    parser.add_argument('path',
                        type=str,
                        nargs='?',
                        default='./input_files/in2.txt',
                        help='O caminho para o arquivo de configuração da L-System.'
    )
    parser.add_argument('iterations',
                        type=int,
                        nargs='?',
                        default=3,
                        help='O número de iterações para gerar a sequência do L-System.'
    )
    parser.add_argument('--trace',
                        action='store_false',
                        help='Indica se o desenho deve ser feito passo a passo.'
    )
    
    args = parser.parse_args()
    
    # Inicializar o gerenciador de L-System
    lsdm = LSystemDrawerMenager()
    # Ler o arquivo de configuração
    lsdm.read(args.path)
    # Gerar a sequência do L-System
    lsdm.generate(iterations=args.iterations)
    # Desenhar o L-System
    try:
        lsdm.draw(trace=args.trace)
    except:
        pass

if __name__ == '__main__':
    main()