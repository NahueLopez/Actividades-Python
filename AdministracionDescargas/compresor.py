from PIL import Image
import os
import shutil

downloads_folderChrome = r'A:\Descargas Chrome'
downloads_folder = r'C:\Users\Nahue\Downloads'
imagen_folder = r'C:\Users\Nahue\Pictures'
music_folder = r'C:\Users\Nahue\Music'
video_folder = r'C:\Users\Nahue\Videos'
doc_folder = r'C:\Users\Nahue\Documents'

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png", ".avif"]:
            original_path = os.path.join(downloads_folder, filename)
            compressed_path = os.path.join(imagen_folder, "compressed_" + filename)

            try:
                # Abrir la imagen original
                picture = Image.open(original_path)

                # Guardar la imagen comprimida
                picture.save(compressed_path, optimize=True, quality=60)

                # Si la compresión fue exitosa, eliminar el archivo original
                os.remove(original_path)

            except Exception as e:
                print(f'Error comprimiendo {filename}: {e}')

        elif extension in [".gif", "svg"]:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(imagen_folder, filename))

        elif extension in [".mp3"]:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(music_folder, filename))

        elif extension in [".mp4"]:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(video_folder, filename))

        elif extension in [".pdf"]:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(doc_folder, filename))

        print(name + ": " + extension)


    for filename in os.listdir(downloads_folderChrome):
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png", ".avif"]:
            original_path = os.path.join(downloads_folderChrome, filename)
            compressed_path = os.path.join(imagen_folder, "compressed_" + filename)

            try:
                # Abrir la imagen original
                picture = Image.open(original_path)

                # Guardar la imagen comprimida
                picture.save(compressed_path, optimize=True, quality=60)

                # Si la compresión fue exitosa, eliminar el archivo original
                os.remove(original_path)

            except Exception as e:
                print(f'Error comprimiendo {filename}: {e}')

        elif extension in [".gif", ".svg"]:
            shutil.move(os.path.join(downloads_folderChrome, filename), os.path.join(imagen_folder, filename))

        elif extension in [".mp3"]:
            shutil.move(os.path.join(downloads_folderChrome, filename), os.path.join(music_folder, filename))

        elif extension in [".mp4"]:
            shutil.move(os.path.join(downloads_folderChrome, filename), os.path.join(video_folder, filename))

        elif extension in [".pdf"]:
            shutil.move(os.path.join(downloads_folderChrome, filename), os.path.join(doc_folder, filename))

        print(name + ": " + extension)