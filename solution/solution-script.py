import hashlib
import json

def calculate_md5sum(file_path, block_size=65536):
    md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            for bloque in iter(lambda: file.read(block_size), b''):
                md5.update(bloque)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

hashes_file = 'json_hashes.json'
folder_pyj = '../PyJ Systems'

with open(hashes_file, 'r') as file:
    hashes = json.load(file)

for file, hash_json in hashes["files"].items():
    ruta_archivo = f'{folder_pyj}/{file}'

    hash_result = calculate_md5sum(ruta_archivo)

    if hash_result != hash_json:
        print(f"El archivo '{file}' fue adulterado, el hash anterior es '{hash_json}. El hash generado es '{hash_result}'")
