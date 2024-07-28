from flask import Flask, render_template, request, redirect, url_for
from load_json import load_data, save_data
from owner_management import OwnerManagement

app = Flask(__name__)
owner_management = OwnerManagement()


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/owner')
def owner_page():
    listed_owners = owner_management.list_owners()
    return render_template('owner_page.html', owners=listed_owners)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        new_owner = {
            'owner_name': name,
            'phone_number': phone,
            'pets': []
        }
        owner_management.add_owner(new_owner)
        return redirect(url_for('owner_page'))

    return render_template('add_owner.html')


if __name__ == '__main__':
    app.run(debug=True)