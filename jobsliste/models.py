from jobsliste import db, db1

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    beruf = db.Column(db.String(), nullable=False)
    firma = db.Column(db.String(), nullable=False)
    ort = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Item {self.beruf}'

class Item1(db1.Model):
    id = db1.Column(db.Integer(), primary_key=True)
    beruf = db1.Column(db1.String(), nullable=False)
    firma = db1.Column(db1.String(), nullable=False)
    ort = db1.Column(db1.String(), nullable=False)
    link = db1.Column(db1.String(), nullable=False)

    def __repr__(self):
        return f'Item1 {self.beruf}'



