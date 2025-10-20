import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados do arquivo CSV
try:
    df = pd.read_csv('dados_plano_inclinado.csv')

    # 2. Limpeza e preparação dos dados
    
    df = df.rename(columns=lambda column: column.strip())

    # Converte as colunas de texto para números para que possam ser plotadas.
    # 'errors='coerce'' transforma qualquer valor que não seja um número em 'NaN' (Not a Number).
    for col in ['POSIÇÃO (x)', 'INTERVALO DE TEMPO (∆t)', 'VEL. MÉDIA (v)']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove linhas que contenham valores não numéricos para evitar erros no gráfico.
    df.dropna(inplace=True)

    # 3. Criar o Gráfico de Posição vs. Tempo
    plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
    plt.scatter(df['INTERVALO DE TEMPO (∆t)'], df['POSIÇÃO (x)'], color='blue', label='Dados Experimentais')
    plt.title('Posição versus Tempo', fontsize=16)
    plt.xlabel('Tempo (s)', fontsize=12)
    plt.ylabel('Posição (cm)', fontsize=12)
    plt.grid(True) # Adiciona uma grade ao fundo para facilitar a leitura
    plt.legend()
    # Salva o gráfico como uma imagem PNG.
    plt.savefig('posicao_vs_tempo.png')
    print("Gráfico 'posicao_vs_tempo.png' foi salvo com sucesso.")


    # 4. Criar o Gráfico de Velocidade vs. Tempo
    plt.figure(figsize=(10, 6)) # Cria uma nova figura para o segundo gráfico
    plt.scatter(df['INTERVALO DE TEMPO (∆t)'], df['VEL. MÉDIA (v)'], color='red', label='Dados Experimentais')
    plt.title('Velocidade Média versus Tempo', fontsize=16)
    plt.xlabel('Tempo (s)', fontsize=12)
    plt.ylabel('Velocidade Média (cm/s)', fontsize=12)
    plt.grid(True)
    plt.legend()
    # Salva o segundo gráfico como uma imagem PNG.
    plt.savefig('velocidade_vs_tempo.png')
    print("Gráfico 'velocidade_vs_tempo.png' foi salvo com sucesso.")


except FileNotFoundError:
    print("Erro: O arquivo 'dados_plano_inclinado.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")