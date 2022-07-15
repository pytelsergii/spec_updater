class SpecItem:
    def __init__(self, name, price, image_url):
        self.name: str = name
        self.price: float = price
        self.image_url: str = image_url

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.image_url == other.image_url
