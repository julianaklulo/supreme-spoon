class Product:
    __id: int
    __name: str
    __description: str
    __price: float

    def __init__(self, name: str, description: str, price: float) -> None:
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)

    def set_id(self) -> None:
        self.__id = len(products) + 1

    def get_id(self) -> int:
        return self.__id
        
    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_description(self) -> str:
        return self.__description

    def set_price(self, price: float) -> None:
        self.__price = price

    def get_price(self) -> float:
        return self.__price
