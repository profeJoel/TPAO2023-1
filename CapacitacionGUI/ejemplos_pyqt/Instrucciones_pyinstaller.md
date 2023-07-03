# Instrucciones para uso de PyInstaller

1.- Instalar pyInstaller
> pip install pyinstaller

2.- Ejecutar PyInstaller
> pyinstaller --onefile --noconsole nombre_archivo.py

3.- El ejecutable estará en el directorio /dist
4.- Puede empotrar el software en cualquier parte del computador ej. C://Archivos de Programas/

Observaciones:
- Importante cuidar las rutas absolutas o relativas al momento de crear el ejecutable y entender donde se ejecutará el software una vez empotrado.
- Al usar PyInstaller se crea un ejecutable para el sistema operativo utilizado, ej. Windows. (archivo.exe)