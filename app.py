from flask import flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/Items')
def get_Items():
    items = Items.query.all()

    output = []
    for item in Items:
        item_data = {'name': Items.name, 'description': Items.description}
        output.append(item_data)

    return {"Items": output}

@app.route('/Items/<id>')
def get_Item(id):
    item = Items.query.get_or_404(id)
    return {"name": Items.name, "description": Items.description}

@app.route('/Items', methods=['POST'])
def add_items():
    item = Item(name=request.json['name'], description=request.json['description'])
    db.session.add('item')
    db.session.commit()
    return {'id': item.id}
