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

products = []

def create_product():
    print("\nCreate a new product\n")
    name = input("Product name: ")
    description = input("Product description: ")
    price = float(input("Product price: "))

    product = Product(name, description, price)
    products.append(product)
    print("\nProduct created successfully!\n")

    menu()
def menu():
    option = -1
    while option < 0 or option > 4:
        print("\nChoose an option:")
        print("1 - Create product")
        print("2 - List all products")
        print("3 - Update product")
        print("4 - Delete product")
        print("0 - Exit")
        option = int(input("\nOption: "))

        if option == 0:
            break
        elif option == 1:
            create_product()
if __name__ == "__main__":
    menu()
