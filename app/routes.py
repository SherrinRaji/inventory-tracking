from flask import render_template, request, redirect
from app import app, db
from app.models import Inventory, Product, Warehouse


def get_products():
    return Product.query.all()


def get_product(id):
    product = Product.query.get(id)
    if product:
        return product
    return None


def get_warehouses():
    return Warehouse.query.all()


def get_warehouse(id):
    product = Warehouse.query.get(id)
    if product:
        return product
    return None


@app.route('/')
@app.route('/index')
def index():
    products = Product.query.all()
    inventories = Inventory.query.all()
    warehouses = Warehouse.query.all()
    return render_template('index.html', products=products, inventories=inventories, warehouses=warehouses)


@app.route('/add/inventory', methods=['POST'])
def add_inventory():
    if request.method == 'POST':
        form = request.form
        product_id = form.get('product_id')
        warehouse_id = form.get('warehouse_id')
        qty = form.get('qty')
        if not product_id or qty:
            inventory = Inventory(product_id=product_id,
                                  warehouse_id=warehouse_id, qty=qty)
            db.session.add(inventory)
            db.session.commit()
            return redirect('/')

    return "An error occured"


@app.route('/add/product', methods=['POST'])
def add_products():
    if request.method == 'POST':
        form = request.form
        product_name = form.get('product_name')
        product_description = form.get('product_description')
        if not product_name or product_description:
            product = Product(product_name=product_name,
                              product_description=product_description)
            db.session.add(product)
            db.session.commit()
            return redirect('/')

    return "An error occured"


@app.route('/add/warehouse', methods=['POST'])
def add_warehouse():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        location = form.get('location')
        if not name or location:
            warehouse = Warehouse(name=name, location=location)
            db.session.add(warehouse)
            db.session.commit()
            return redirect('/')

    return "An error occured"


@app.route('/update/inventory/<int:id>')
def update_inventory_route(id):
    products = get_products()
    warehouses = get_warehouses()
    if not id or id != 0:
        inventory = Inventory.query.get(id)
        if inventory:
            return render_template('update_inventory.html', inventory=inventory, products=products, warehouses=warehouses)

    return "An error occured"


@app.route('/update/product/<int:id>')
def update_product_route(id):
    if not id or id != 0:
        product = Product.query.get(id)
        if product:
            return render_template('update_product.html', product=product)

    return "An error occured"


@app.route('/update/inventory/<int:id>', methods=['POST'])
def update_inventory(id):
    if not id or id != 0:
        inventory = Inventory.query.get(id)
        if inventory:
            form = request.form
            product = form.get('product_id')
            warehouse = form.get('warehouse_id')
            qty = form.get('qty')
            inventory.product_id = product
            inventory.warehouse_id = warehouse
            inventory.qty = qty
            db.session.commit()
        return redirect('/')

    return "An error occured"


@app.route('/update/product/<int:id>', methods=['POST'])
def update_product(id):
    if not id or id != 0:
        product = Product.query.get(id)
        if product:
            form = request.form
            name = form.get('product_name')
            description = form.get('product_description')
            product.product_name = name
            product.product_description = description
            db.session.commit()
        return redirect('/')

    return "An error occured"


@app.route('/delete/warehouse/<int:id>')
def delete_warehouse(id):
    if not id or id != 0:
        warehouse = Warehouse.query.get(id)
        if warehouse:
            db.session.delete(warehouse)
            db.session.commit()
        return redirect('/')

    return "An error occured"


@app.route('/delete/product/<int:id>')
def delete_product(id):
    if not id or id != 0:
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return redirect('/')

    return "An error occured"


@app.route('/delete/inventory/<int:id>')
def delete_inventory(id):
    if not id or id != 0:
        inventory = Inventory.query.get(id)
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
        return redirect('/')

    return "An error occured"
