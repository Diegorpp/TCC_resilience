import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('./hpa_data.csv') # Teste_1
# df = pd.read_csv('./hpa_data_exp01_1000s.csv') # Teste_2
df = pd.read_csv('./hpa_data_exp02_1200s.csv') # Teste_2


path_imgs = './resultados_graficos/'
nome=grafico_consumo = path_imgs+'teste_3_consume_plot.png'
nome_grafico_instancias = path_imgs+'teste_3_instancias_consume_plot.png'

def gera_grafico_instancia_atual():
    # Extract the timestamp and consume columns from your DataFrame
    Time = df['Time']
    Instâncias = df['Instâncias atuais']

    # Create a line plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(Time, Instâncias, marker='o', linestyle='-')

    # Customize the plot if necessary (e.g., labels, titles, grid, etc.)
    plt.xlabel('Time')
    plt.ylabel('Instâncias')
    plt.title('Instâncias atuais Over Time')
    plt.grid(True)

    plt.savefig(nome_grafico_instancias)

    # Close the plot to prevent the warning
    plt.close()


def gera_grafico_consumo():
    # Extract the timestamp and consume columns from your DataFrame
    Time = df['Time']
    df['consumo atual'] = df['consumo atual'].str.rstrip('%').astype(int)
    consumo = df['consumo atual']


    # Create a line plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(Time, consumo, marker='o', linestyle='-')

    # Customize the plot if necessary (e.g., labels, titles, grid, etc.)
    plt.xlabel('Time')
    plt.ylabel('consumo')
    plt.title('consumo atuais Over Time')
    plt.grid(True)

    plt.savefig(grafico_consumo)

    # Close the plot to prevent the warning
    plt.close()

if __name__ == '__main__':
    gera_grafico_instancia_atual()
    gera_grafico_consumo()
    # breakpoint()