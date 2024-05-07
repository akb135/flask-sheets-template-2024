from pprint import pprint

from app.db import BaseModel

class Destination(BaseModel):

    SHEET_NAME = "destinations"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'English Castles',
            'description': 'Check out the grand old castles of the United Kingdom.',
            'price': 649.95,
            'url': 'https://picsum.photos/id/142/360/200'
        },
        {
            'name': 'Greece',
            'description': 'Enjoy the picturesque beauty of Greece.',
            'price': 679.95,
            'url': 'https://picsum.photos/id/49/360/200'
        },
        {
            'name': 'New York',
            'description': 'Visit the melting pot of the world, the busiest city of the United States.',
            'price': 549.95,
            'url': 'https://picsum.photos/id/43/360/200'
        }
    ]




if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    destinations = Destination.all()
    print("FOUND", len(destinations), "DESTINATIONS:")
    if any(destinations):
        for destination in destinations:
            #breakpoint()
            pprint(dict(destination))
    else:
        #if input("Seed destinations? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Destination.seed()
        print("SEEDING RECORDS...")
        Destination.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    destination = Destination.find(1)
    print(destination.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Destination.where(name="Greece")
    print(len(matches))
    destination = matches[0]
    print(destination.name)

    print("------------")
    print("CREATING NEW DESTINATION...")
    params = {
        "name": "Himalayas (India)",
        "price":799.95,
        "description":"Explore some of the highest peaks of the world, the mountain range of Himalayas in India.",
        "url": "https://picsum.photos/id/79/360/200"
    }
    Destination.create(params)
