import kagglehub
import os
import zipfile
import shutil

# Verificar y crear directorios si no existen
raw_data_dir = os.path.join('..', 'data', 'raw')
os.makedirs(raw_data_dir, exist_ok=True)

# Descargar el dataset
print("Descargando datos de Kaggle...")
path = kagglehub.dataset_download("thedevastator/open-university-learning-analytics-dataset")
print("Archivos descargados en:", path)

# Si los datos vienen en un archivo zip, descomprímelos
if path.endswith('.zip'):
    print("Descomprimiendo archivos...")
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(raw_data_dir)
    print("Archivos descomprimidos en:", raw_data_dir)
else:
    # Si no es un zip, asumimos que es un directorio con los archivos
    print("Copiando archivos al directorio del proyecto...")
    files = os.listdir(path)
    for file in files:
        source = os.path.join(path, file)
        destination = os.path.join(raw_data_dir, file)
        shutil.copy2(source, destination)
    print("Archivos copiados a:", raw_data_dir)

print("¡Descarga completada!")