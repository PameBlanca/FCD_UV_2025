# Función para mostrar información de un DataFrame
def mostrar_info_df(df, nombre):
    print(f"\n--- Información de {nombre} ---")
    print(f"Forma: {df.shape}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeros 5 registros:")
    print(df.head())
    print("-" * 50)