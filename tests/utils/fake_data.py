import csv
from faker import Faker
import pandas as pd
from datetime import datetime

def generate_fake_data(output_file: str, num_records: int):
    """
    Gera dados sinteticos e salva em CSV de forma eficiente.
    """
    fake = Faker()
    # Definindo o locale se quiser dados brasileiros (ex: Faker('pt_BR'))
    
    headers = ['transaction_id', 'user_name', 'email', 'amount', 'transaction_date']
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            
            for _ in range(num_records):
                writer.writerow({
                    'transaction_id': fake.uuid4(),
                    'user_name': fake.name(),
                    'email': fake.email(),
                    'amount': round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
                    'transaction_date': fake.date_time_between(start_date='-1y', end_date='now').isoformat()
                })
        
        print(f"Sucesso: {num_records} registros gerados em {output_file}")
    except Exception as e:
        print(f"Erro ao gerar arquivo: {e}")

if __name__ == "__main__":
    FILENAME = f"raw_data_{datetime.now().strftime('%Y%m%d')}.csv"
    generate_fake_data(FILENAME, 10000)