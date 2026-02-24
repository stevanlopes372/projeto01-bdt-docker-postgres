import csv
from faker import Faker
import pandas as pd
from datetime import datetime

def generate_fake_data(output_file: str, num_records: int):
    """
    Gera dados sinteticos e salva em CSV de forma eficiente.
    """
    fake = Faker('pt_BR')
    # Definindo o locale se quiser dados brasileiros (ex: Faker('pt_BR'))
    
    headers = ['id','nome','email','datacadastro']
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            
            for _ in range(num_records):
                writer.writerow({
                    headers[0]: fake.uuid4(),
                    headers[1]: fake.name(),
                    headers[2]: fake.email(),
                    headers[3]: fake.date_between(start_date='-2y'),
                })
        
        print(f"Sucesso: {num_records} registros gerados em {output_file}")
    except Exception as e:
        print(f"Erro ao gerar arquivo: {e}")

if __name__ == "__main__":
    FILENAME = f"output_dim_user.csv"
    generate_fake_data(FILENAME, 15)