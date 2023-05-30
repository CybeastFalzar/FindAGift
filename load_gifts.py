from database import db
from filter import filter_data, filter_data_api, get_category
import os

class gifts(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column(db.String(300))
    name = db.Column(db.String(300))
    seller = db.Column(db.String(300))
    price = db.Column(db.Float)
    buy_link = db.Column(db.String(300))
    img_link = db.Column(db.String(300))
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
    print(1)
    # db.drop_all()
    # db.create_all()

    # directory = "gifts"
    # for filename in os.listdir(directory):
    #     f = os.path.join(directory, filename)
    #     if os.path.isfile(f):
    #         age = 0
    #         cond1 = get_category(str(filename)) == "nickelodeon"
    #         cond2 = get_category(str(filename)) == "basketball"
    #         cond3 = get_category(str(filename)) == "baseball"
    #         cond4 = get_category(str(filename)) == "star wars"
    #         cond5 = get_category(str(filename)) == "graphic tees"
    #         if (cond1):
    #             age = 3
    #         elif cond2:
    #             age = 4
    #         elif cond3:
    #             age = 4
    #         elif cond4:
    #             age = 2
    #         elif cond5:
    #             age = 4
    #         else:
    #             age = 4
    #         new_entry = gifts(filter_data(f), get_category(str(filename)), age)
    #         db.session.add(new_entry)
    # db.session.commit()


if __name__ == '__main__':
    init_db()
