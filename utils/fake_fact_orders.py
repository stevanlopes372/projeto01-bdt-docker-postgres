from typing import Optional
import pandas as pd
import random
from faker import Faker
import csv
import argparse

fake = Faker()

def generate_fake_data(users_file: str, orders_file: str, num_orders = 50):
    """
    Gera tabela de pedidos garantindo que todo user_id exista na tabela de usuarios.
    """
    try:
        # 1. Carregar apenas a coluna necessaria para economizar RAM
        # Se o arquivo de users for gigante, o pandas 'usecols' ajuda muito
        df_users = pd.read_csv(users_file, usecols=['id'])
        user_ids = df_users['id'].tolist()
        
        if not user_ids:
            raise ValueError("A tabela de usuarios esta vazia!")

        headers = ['id_pedido', 'id_cliente', 'valor', 'status', 'data_pedido']
        statuses = ['created', 'in_progress', 'in_delivery', 'closed', 'cancelled']
        
        with open(orders_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            
            for _ in range(num_orders):
                writer.writerow({
                    headers[0]: fake.uuid4(),
                    headers[1]: random.choice(user_ids),
                    headers[2]: round(random.uniform(10.0, 500.0), 2),
                    headers[3]: random.choice(statuses),
                    headers[4]: fake.date_between(start_date='-2y'),
                })
                
        print(f"Sucesso: {num_orders} pedidos gerados vinculados a {len(user_ids)} usuarios.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {users_file} nao foi encontrado. Gere os usuarios primeiro!")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de execucao:
# generate_orders('usuarios.csv', 'pedidos.csv', 5000)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de CSV Fake Pro")
    
    # Argumentos da CLI
    parser.add_argument("--file", type=str, default="output_fact_orders.csv", help="Nome do arquivo de saida")
    parser.add_argument("--users_file", type=str, default="output_dim_user.csv", help="Nome do arquivo dim_users")


    args = parser.parse_args()
    
    generate_fake_data(users_file=args.users_file, orders_file=args.file)