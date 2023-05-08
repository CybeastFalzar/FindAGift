from app import db

class gifts(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    name = db.Column(db.String(100))
    seller = db.Column(db.String(100))
    price = db.Column(db.Integer)
    buy_link = db.Column(db.String(100))
    img_link = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, category, name, seller, price, buy_link, img_link, age):
        self.category = category
        self.name = name
        self.price = price
        self.buy_link = buy_link
        self.seller = seller
        self.img_link = img_link
        self.age = age

def init_db():
    db.create_all()
    pringles = gifts("Snack", "Pringle", "Walgreens", 10, "link", "link2", 2)
    pringles2 = gifts("Snack", "Pringle", "Target", 5, "link", "link2", 10)
    db.session.add(pringles)
    db.session.add(pringles2)
    db.session.commit()


if __name__ == '__main__':
    init_db()
