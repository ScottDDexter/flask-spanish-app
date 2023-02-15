from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class IrregularConjugation(db.Model):
    __tablename__ = 'irregular_conjugations'
    id = db.Column(db.Integer, primary_key=True)
    infin_id = db.Column(db.Integer, db.ForeignKey('verbs.id'))
    yo = db.Column(db.String(64), nullable=False)
    tu = db.Column(db.String(64), nullable=False)
    el = db.Column(db.String(64), nullable=False)
    ella = db.Column(db.String(64), nullable=False)
    usted = db.Column(db.String(64), nullable=False)
    nosotros = db.Column(db.String(64), nullable=False)
    nosotras = db.Column(db.String(64), nullable=False)
    ellos = db.Column(db.String(64), nullable=False)
    ellas = db.Column(db.String(64), nullable=False)
    ustedes = db.Column(db.String(64), nullable=False)


# db association table for sets and infinitives
class SetVerbs(db.Model):
    __tablename__ = 'set_verbs'
    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey('practice_set.id'))
    verb_id = db.Column(db.Integer, db.ForeignKey('verbs.id'))

    verb = db.relationship('Verb', back_populates='practice_sets')
    practice_set = db.relationship('Practice_Set', back_populates='verbs')


# db association table for sets and verb-tenses
class SetTenses(db.Model):
    __tablename__ = 'set_tenses'
    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey('practice_set.id'))
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.id'))

    tense = db.relationship('Tense', back_populates='practice_sets')
    practice_set = db.relationship('Practice_Set', back_populates='tenses')


# verb table (id, infin, form(fk))
class Verb(db.Model):
    __tablename__ = 'verbs'
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String(64), unique=True)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))

    # relationship
    practice_sets = db.relationship('SetVerbs', back_populates='verb')

    def __repr__(self):
        return f"Verb:'{self.infinitive}', 'Form:{self.form_id}')"


# form [id, label] ("static")
class Form(db.Model):
    __tablename__ = 'forms'
    id = db.Column(db.Integer, primary_key=True)
    form = db.Column(db.String, unique=True)

    # relationship
    infinitives = db.relationship('Verb', backref='form')

    def __repr__(self):
        return f'{self.form}'


# subject [id, label] ("static")
class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f'{self.subject}'


# tense [id, label]
class Tense(db.Model):
    __tablename__ = 'tenses'
    id = db.Column(db.Integer, primary_key=True)
    tense = db.Column(db.String(64), unique=True)

    # relationship
    practice_sets = db.relationship('SetTenses', back_populates='tense')

    def __repr__(self):
        return f'{self.tense}'


# practice_set [id, label]
class Practice_Set(db.Model):
    __tablename__ = 'practice_set'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), unique=True)

    # relationship
    verbs = db.relationship('SetVerbs', back_populates='practice_set')
    tenses = db.relationship('SetTenses', back_populates='practice_set')

    def __repr__(self):
        return f'{self.label}'


if __name__ == '__main__':
    pass
