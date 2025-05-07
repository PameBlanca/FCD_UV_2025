import pandas as pd

# Función para mostrar información de un DataFrame
def mostrar_info_df(df, nombre):
    print(f"\n--- Información de {nombre} ---")
    print(f"Forma: {df.shape}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeros 5 registros:")
    print(df.head())
    print("-" * 50)


# Función para verificar datos faltantes
def verificar_datos_faltantes(df, nombre):
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_df = pd.DataFrame({
        'Valores Faltantes': missing_values,
        'Porcentaje (%)': missing_percentage
    })
    
    # Filtrar solo columnas con valores faltantes
    missing_df = missing_df[missing_df['Valores Faltantes'] > 0]
    
    print(f"\n--- Análisis de datos faltantes en {nombre} ---")
    
    if missing_df.empty:
        print("No hay valores faltantes.")
    else:
        print(f"Total de filas en el DataFrame: {len(df)}")
        print(missing_df)
    
    print("-" * 50)