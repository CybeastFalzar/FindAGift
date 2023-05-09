from app import db
from filter import filter_data, filter_data_api

class gifts(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    name = db.Column(db.String(100))
    seller = db.Column(db.String(100))
    price = db.Column(db.Float)
    buy_link = db.Column(db.String(100))
    img_link = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, result, category, age):
        self.name = result.get("name")
        self.price = result.get("price")
        self.buy_link = result.get("buy_link")
        self.seller = result.get("seller")
        self.img_link = result.get("img_link")
        self.category = category
        self.age = age

    # def __init__(self, category, name, seller, price, buy_link, img_link, age):
    #     self.category = category
    #     self.name = name
    #     self.price = price
    #     self.buy_link = buy_link
    #     self.seller = seller
    #     self.img_link = img_link
    #     self.age = age

def init_db():
    db.drop_all()
    db.create_all()

    # Snacks
    snack_1_pringles = gifts(filter_data("pringles.json"), "Snack", 3)
    snack_2_pringles = gifts(filter_data("pringles.json"), "Snack", 4)
    snack_3_pringles = gifts(filter_data("pringles.json"), "Snack", 4)
    snack_4_pringles = gifts(filter_data("sw.json"), "Star Wars", 4)
    snack_5_pringles = gifts(filter_data("sw.json"), "Star Wars", 4)
   
    snack_6_pringles = gifts(filter_data("sw.json"), "Star Wars", 4)
    # snack_3 = gifts(filter_data_api("https://api.upcitemdb.com/prod/trial/lookup?upc=082686005999"), "Star Wars", 4)
   
    # snack_4 = gifts(filter_data_api("https://api.upcitemdb.com/prod/trial/lookup?upc=082686005999"), "Star Wars", 4)
    # snack_5 = gifts(filter_data_api("https://api.upcitemdb.com/prod/trial/lookup?upc=082686005999"), "Star Wars", 4)


    db.session.add(snack_1_pringles)
    db.session.add(snack_2_pringles)
    db.session.add(snack_3_pringles)
    db.session.add(snack_4_pringles)
    db.session.add(snack_5_pringles)
    db.session.add(snack_6_pringles)
    db.session.commit()


if __name__ == '__main__':
    init_db()
