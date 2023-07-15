import pandas as pd
from sqlalchemy import create_engine

# Establecer la conexión con la base de datos MySQL
db_user = 'root'
db_password = 'Rvb3nch0'
db_host = 'localhost'
db_name = 'jrnq_prueba_r5'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Consulta SQL
query = '''
    SELECT codigo_tienda, COUNT(DISTINCT num_documento_cliente) AS num_clientes
    FROM compras
    GROUP BY codigo_tienda
    HAVING COUNT(DISTINCT num_documento_cliente) >= 100;
'''

# Ejecutar la consulta y obtener los resultados en un DataFrame
df_result = pd.read_sql(query, con=engine)

# Cerrar la conexión a la base de datos
engine.dispose()

# Imprimir los resultados
print("Tiendas con compras de al menos 100 clientes diferentes:")
print(df_result)
