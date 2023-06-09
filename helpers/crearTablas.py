def crearTabla(dataFreame, nombreTabla):
    archivoHtml = dataFreame.to_html()
    archivo = open(f"./view/{nombreTabla}.html","w", encoding="utf-8")
    archivo.write(archivoHtml)
    archivo.close()
