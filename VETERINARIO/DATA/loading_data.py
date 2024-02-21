def loading_data(nombre_archivo):
    
    try:
        return pd.read_csv(nombre_archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la carpeta.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo '{nombre_archivo}': {e}")
        return None

# Ejemplo de uso
nombre_archivo = "Amigos_De_Las_Mascotas_2022_Data_Set.csv" 
df = loading_data(nombre_archivo)
if df is not None:
    print("[+] Archivo CSV cargado correctamente.")
else:
    print("[-] No se pudo cargar el archivo CSV.")
