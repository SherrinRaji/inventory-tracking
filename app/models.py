from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(250), index=True, nullable=False)
    product_description = db.Column(db.String(250), index=True, nullable=False)


class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, ForeignKey('product.id'))
    location = db.Column(db.Integer, index=True, nullable=False)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey('product.id'))
    warehouse_id = db.Column(db.Integer, ForeignKey('warehouse.id'))
    qty = db.Column(db.Integer, index=True, nullable=False)
    product = relationship("Product")
    warehouse = relationship("Warehouse")
