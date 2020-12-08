class Product:
    __id: int
    __name: str
    __description: str
    __price: float
    __weight: float
    __width: float
    __height: float
    __depth: float

    def __init__(self, name: str, description: str, price: float, weight: float, width: float, height: float, depth: float) -> None:
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_weight(weight)
        self.set_width(width)
        self.set_height(height)
        self.set_depth(depth)

    def set_id(self) -> None:
        if len(products) == 0:
            self.__id = 1
        else:
            self.__id = products[-1].get_id() + 1

    def get_id(self) -> int:
        return self.__id
        
    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_description(self, description: str) -> None:
        if len(description) >= 20:
            self.__description = description
        else:
            raise ValueError("Description lenght must be at least 20 characters!") 

    def get_description(self) -> str:
        return self.__description

    def set_price(self, price: float) -> None:
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be positive!")

    def get_price(self) -> float:
        return self.__price

    def set_weight(self, weight: float) -> None:
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Weight must be positive!")

    def get_weight(self) -> float:
        return self.__weight

    def set_width(self, width: float) -> None:
        if width> 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive!")

    def get_width(self) -> float:
        return self.__width

    def set_height(self, height: float) -> None:
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive!")

    def get_height(self) -> float:
        return self.__height

    def set_depth(self, depth: float) -> None:
        if depth > 0:
            self.__depth = depth
        else:
            raise ValueError("Depth must be positive!")

    def get_depth(self) -> float:
        return self.__depth

    def print_product(self) -> None:
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Description: {self.get_description()}")
        print(f"Price: R${self.get_price()}")
        print(f"Weight: {self.get_weight()} kg")
        print(f"Width: {self.get_width()} m")
        print(f"Height: {self.get_height()} m")
        print(f"Depth: {self.get_depth()} m\n")

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

def find_product(id: int) -> int:
    index = -1
    for product in products:
        if product.get_id() == id:
            index = products.index(product)
            break
    
    return index

def print_product(index: int) -> None:
        print(f"ID: {products[index].get_id()}")
        print(f"Name: {products[index].get_name()}")
        print(f"Description: {products[index].get_description()}")
        print(f"Price: R${products[index].get_price()}\n")

def list_products():
    if len(products) == 0:
        print("\nNo products yet!\n")
    else:
        print("\nProducts created:\n")
        for product in products:
            print(f"ID: {product.get_id()}")
            print(f"Name: {product.get_name()}")
            print(f"Description: {product.get_description()}")
            print(f"Price: R${product.get_price()}\n")

    menu()

def list_product_by_id():
    print("\nList product by ID\n")
    id = int(input("Product ID: "))

    index = find_product(id)

    if index >= 0:
        print("\nProduct found!\n")
        print_product(index)
    else:
        print("\nProduct not found!\n")
    
    menu()

def update_product():
    print("\nUpdate a product\n")
    id = int(input("Product ID: "))

    index = find_product(id)

    if index >= 0:
        print("\nProduct found!\n")
        print_product(index)

        name = input("New product name: ")
        description = input("New product description: ")
        price = float(input("New product price: "))

        products[index].set_name(name)
        products[index].set_description(description)
        products[index].set_price(price)

        print("\nProduct updated succesfully!\n")
    else:
        print("\nProduct not found!\n")

    menu()

def delete_product():
    print("\nDelete a product\n")
    id = int(input("Product ID: "))

    index = find_product(id)

    if index >= 0:
        print("\nProduct found!\n")
        print_product(index)
        
        option = input("Are you sure you want to delete this product? (Y/N) ").upper()
        
        if option == "Y":
            products.pop(index)
            print("\nProduct deleted successfully!\n")
    else:
        print("\nProduct not found!\n")

    menu()

def menu():
    option = -1
    while option < 0 or option > 4:
        print("\nChoose an option:")
        print("1 - Create product")
        print("2 - List all products")
        print("3 - List product by ID")
        print("4 - Update product")
        print("5 - Delete product")
        print("0 - Exit")
        option = int(input("\nOption: "))

        if option == 0:
            break
        elif option == 1:
            create_product()
        elif option == 2:
            list_products()
        elif option == 3:
            list_product_by_id()
        elif option == 4:
            update_product()
        elif option == 5:
            delete_product()

if __name__ == "__main__":
    menu()
