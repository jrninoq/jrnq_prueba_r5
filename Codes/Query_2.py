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
    SELECT b.nombre_barrio, COUNT(DISTINCT c.num_documento_cliente) AS num_clientes
    FROM compras AS c
    JOIN tiendas AS t ON c.codigo_tienda = t.codigo_tienda
    JOIN barrios AS b ON t.id_barrio = b.id_barrio
    WHERE t.tipo_tienda = 'Tienda Regional'
    GROUP BY b.nombre_barrio
    ORDER BY num_clientes DESC
    LIMIT 5
'''

# Ejecutar la consulta y obtener los resultados en un DataFrame
df_result = pd.read_sql(query, con=engine)

# Cerrar la conexión a la base de datos
engine.dispose()

# Imprimir los resultados
print("Los 5 barrios donde la mayor cantidad de clientes únicos realizan compras en tiendas tipo 'Tienda Regional':")
print(df_result)
