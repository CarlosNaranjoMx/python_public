#!/bin/env python
import argparse
import os
import chardet

def search_word_in_files(directory, word):
    print(word)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']
                    if encoding is None:
                        encodings_to_try = ['utf-8', 'latin-1']  # Codificaciones a probar si no se detecta
                    else:
                        encodings_to_try = [encoding]
                    
                    content = None
                    for encoding_to_try in encodings_to_try:
                        try:
                            content = raw_data.decode(encoding_to_try)
                            break
                        except UnicodeDecodeError:
                            pass

                    if content is not None and word.lower() in content.lower():
                        relative_path = os.path.relpath(file_path, directory)
                        print(f'{relative_path}')
            except IOError:
                print(f'Error al abrir el archivo: {file_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buscador de coincidencias en archivos')
    parser.add_argument('directory', help='Ruta del directorio a buscar')
    parser.add_argument('words', nargs='+', help='Lista de palabras a buscar')
    args = parser.parse_args()

    for word in args.words:
        search_word_in_files(args.directory, word)
