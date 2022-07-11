class Product:
    def __init__(self, name, price, image=None):
        self.name: str = name
        self.price: float = price
        self.image: str = image
