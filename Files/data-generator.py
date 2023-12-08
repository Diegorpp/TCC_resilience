import subprocess
from datetime import datetime
import pandas as pd
from time import time, sleep

# Por padrão o HPA verifica as métricas a cada 15 segundos. 
def monitora_hpa(duracao: int, intervalo: int):
    """duracao: tempo em segundos que o teste vai durar
       intervalo: tempo em segundos que o script vai pegar as métricas
    """
    
    # command = """kubectl get hpa | grep hpa | awk '{print $3 "\t" $4 "\t" $5}'"""
    inicio = time()
    command = "kubectl get hpa"
    data = []
    while(1):
        output = subprocess.check_output(command, shell=True, text=True)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        lines = output.strip().split('\n')[1:]
            
        for line in lines:
            parts = line.split()
            name = parts[0]
            current_percentage, threshold_percentage = parts[2].split('/')
            current_instances = str(parts[5])
            max_instances = int(parts[4])
            data.append([current_time, name, current_percentage, threshold_percentage, current_instances, max_instances])

        df = pd.DataFrame(data, columns=["Time", "Name", "consumo atual", "% de limiar", "Instâncias atuais", "Instâncias máximas"])
        # print(df)
        fim = time()
        if fim-inicio>duracao:
            break
        else:
            sleep(intervalo)

    return df


def executa_experimento():
    tempo = 1200 # O teste atual roda por 670 segundos, 60 subindo, 10 mantendo e 600 reduzindo
    df = monitora_hpa(tempo,3)
    csv_filename = "hpa_data.csv"
    df.to_csv(csv_filename, index=False)

if __name__ == '__main__':
    executa_experimento()