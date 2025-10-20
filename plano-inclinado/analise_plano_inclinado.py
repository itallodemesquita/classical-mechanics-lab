import pandas as pd
import matplotlib.pyplot as plt
import os

DIRETORIO_DO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
CAMINHO_DO_ARQUIVO_CSV = os.path.join(DIRETORIO_DO_SCRIPT, 'dados_plano_inclinado.csv')

try:
    # 1. Carregar os dados do arquivo CSV
    df = pd.read_csv(CAMINHO_DO_ARQUIVO_CSV)

    # 2. Limpeza e preparação dos dados
    df = df.rename(columns=lambda column: column.strip())
    for col in ['POSIÇÃO (x)', 'INTERVALO DE TEMPO (∆t)', 'VEL. MÉDIA (v)']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(inplace=True)


    # 3. Criar o Gráfico de Posição vs. Tempo (gráfico de linha)
    plt.figure(figsize=(10, 6))

    plt.plot(df['INTERVALO DE TEMPO (∆t)'], df['POSIÇÃO (x)'], color='blue', marker='o', linestyle='-', label='Dados Experimentais')
    plt.title('Posição versus Tempo', fontsize=16)
    plt.xlabel('Tempo (s)', fontsize=12)
    plt.ylabel('Posição (cm)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(DIRETORIO_DO_SCRIPT, 'posicao_vs_tempo_linha.png')) # Nome do arquivo alterado para não sobrescrever o antigo
    print("Gráfico 'posicao_vs_tempo_linha.png' foi salvo com sucesso.")

    # 4. Criar o Gráfico de Velocidade vs. Tempo (gráfico de linha)
    plt.figure(figsize=(10, 6))
    
    plt.plot(df['INTERVALO DE TEMPO (∆t)'], df['VEL. MÉDIA (v)'], color='red', marker='o', linestyle='-', label='Dados Experimentais')
    plt.title('Velocidade Média versus Tempo', fontsize=16)
    plt.xlabel('Tempo (s)', fontsize=12)
    plt.ylabel('Velocidade Média (cm/s)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(DIRETORIO_DO_SCRIPT, 'velocidade_vs_tempo_linha.png')) # Nome do arquivo alterado
    print("Gráfico 'velocidade_vs_tempo_linha.png' foi salvo com sucesso.")


except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado no caminho: {CAMINHO_DO_ARQUIVO_CSV}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")