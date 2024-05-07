from pprint import pprint

from app.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'English Castles',
            'description': 'Let us go back in history and visit UK castles.',
            'price': 649.99,
            'url': 'https://picsum.photos/id/142/360/200'
        },
        {
            'name': 'Greece',
            'description': 'Check out the picturesque locales of Greece.',
            'price': 679.99,
            'url': 'https://picsum.photos/id/49/360/200'
        },
        {
            'name': 'Himalayas (India)',
            'description': 'Explore the highest peaks of the world.',
            'price': 799.99,
            'url': 'https://picsum.photos/id/79/360/200'
        }
    ]




if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    products = Product.all()
    print("FOUND", len(products), "PRODUCTS:")
    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Product.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    product = Product.find(1)
    print(product.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Product.where(name="Strawberries")
    print(len(matches))
    product = matches[0]
    print(product.name)

    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
        "name": "New York",
        "price":599.99,
        "description":"The most buzzing city of the United States",
        "url": "https://picsum.photos/id/43/360/200"
    }
    Product.create(params)
