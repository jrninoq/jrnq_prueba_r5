import pandas as pd
from sqlalchemy import create_engine

# Paso 1: Leer el conjunto de datos
df = pd.read_csv("C:/Users/dell/Downloads/Prueba_Tecnica_R5/dataset.csv")

# Paso 2: Conectarse a la base de datos MySQL
db_user = 'root'
db_password = 'Rvb3nch0'
db_host = 'localhost'
db_name = 'jrnq_prueba_r5'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Paso 3: Escribir los datos en las tablas

# Compras (fact)
df_fact = df[['num_documento_cliente', 'codigo_tienda', 'fecha_compra', 'total_compra']]
df_fact.to_sql('compras', con = engine, if_exists = 'replace', index=False)

# Tabla Tiendas (dim1)
df_dim1 = df[['codigo_tienda', 'tipo_tienda', 'latitud_tienda', 'longitud_tienda', 'id_barrio']]
df_dim1 = df_dim1.drop_duplicates()  # Eliminar duplicados si es necesario
df_dim1.to_sql('tiendas', con = engine, if_exists = 'replace', index=False)

# Tabla Barrios (dim2)
df_dim2 = df[['id_barrio', 'nombre_barrio']]
df_dim2 = df_dim2.drop_duplicates()  # Eliminar duplicados si es necesario
df_dim2.to_sql('barrios', con = engine, if_exists = 'replace', index=False)

# Tabla Clientes (dim3)
df_dim3 = df[['num_documento_cliente', 'tipo_documento_cliente', 'id_barrio']]
df_dim3 = df_dim3.drop_duplicates()  # Eliminar duplicados si es necesario
df_dim3.to_sql('clientes', con = engine, if_exists = 'replace', index=False)

# Paso 4: Cerrar la conexión a la base de datos
engine.dispose()

print("¡Datos cargados exitosamente en las tablas del Data Warehouse!")
