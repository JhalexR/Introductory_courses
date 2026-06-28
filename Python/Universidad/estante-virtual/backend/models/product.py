class Product:

    def __init__(
        self,
        id,
        titulo,
        autor,
        descripcion,
        precio,
        stock,
        categoria_id,
        isbn,
        imagen_url
    ):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.isbn = isbn
        self.imagen_url = imagen_url