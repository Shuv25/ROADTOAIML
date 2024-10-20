from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/Shop'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Assocation Table
Customer_Product=db.Table(
    "customer_product",
    db.Column("customer_id",db.Integer,db.ForeignKey("customers.id")),
    db.Column("product_id",db.Integer,db.ForeignKey("products.id"))
)


class Customer(db.Model):
    __tablename__='customers'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    items=db.relationship("Product",backref="oweners",secondary=Customer_Product)

    def __repr__(self):
        return f"Customer( Name '{self.name}', Email '{self.email}')"

class Product(db.Model):
    __tablename__='products'
    id= db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product( Name '{self.product}', Price '{self.price}')"

if __name__ == '__main__':
    app.run(debug=True)
