📋 Fase 1: A Fundação (Infraestrutura)
Antes de pensar em modelagem, view ou carga incremental, a gente precisa de um chão de fábrica estável.

Sua primeira tarefa é montar o ambiente. Eu quero que você escreva o docker-compose.yml e o Dockerfile (se necessário) para subir essa brincadeira.

Requisitos da sua entrega (PR 01):

1. O Banco (Postgres):

	- Quero persistência de dados. Se eu derrubar o container, não quero perder minhas tabelas. Use volumes.
	- Defina as credenciais via variáveis de ambiente (environment variables). AVISO DO TIO: Se eu ver senha hardcoded no YAML ou commitada no Git, a gente vai ter uma conversa séria. Use um .env.

2. O Executor (DBT):
	
	- O dbt deve rodar isolado num container. Nada de instalar pip install dbt-postgres na sua máquina local (host). A gente quer isolamento de dependência.
	- Como você vai desenvolver? Você vai precisar editar os arquivos SQL na sua máquina (VS Code, imagino) e o dbt tem que ler isso dentro do container. Dica: Bind Mounts.
	- O container do dbt precisa enxergar o container do Postgres. Lembre-se que localhost dentro do container do dbt é o próprio container, não o seu PC. Configure a rede (network) direito.

3. Estrutura de Pastas:
	- Me mostre como você vai organizar a raiz do projeto. Onde ficam os dados? Onde fica o dbt? Onde fica o script de init do banco?

---

O Desafio:

Não vou te dar o código. Abre aí seu editor e monta o esqueleto.

1. Crie a estrutura de pastas.
2. Crie o docker-compose.yml com os serviços postgres e dbt (ou um container python que a gente instala o dbt).
3. Crie um .gitignore decente (lembra do .env e da pasta target/ do dbt).
4. Manda bala no código aí e cola aqui pra eu fazer o Code Review. Vou ser chato com indentação e boas práticas, hein?
