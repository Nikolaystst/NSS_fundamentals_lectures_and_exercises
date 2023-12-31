class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, prod_name: str):
        self.products.append(prod_name)

    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if x.startswith(first_letter)]

    def __repr__(self):
        sorted_products = sorted(self.products)
        result = ""
        result += f"Items in the {self.name} catalogue:\n"
        result += '\n'.join([x for x in sorted_products])
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
