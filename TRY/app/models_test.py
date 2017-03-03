from app import db, app

class Phrase(db.Model):
    __searchable__ = ['phrase', 'definition']
    
    id = db.Column(db.Integer, primary_key=True)
    phras = db.Column(db.String(60), index=True, unique=True)
    definition = db.Column(db.String(120), index=True, unique=True)
#    requests = db.relationship('History', backref='author', lazy='dynamic')
    periods = db.relationship('Period', backref='phr_html', lazy='dynamic')
    comments = db.Column(db.String(400), index=True, unique=True)
    diachron_tip = db.Column(db.String(400), index=True, unique=True)
#    period_id = db.Column(db.Integer, db.ForeignKey('period.id'))

#    def __init__(self, phras, definition):
#        self.phras = phras
#        self.definition = definition

    def __repr__(self):
        return '<Phrase %r>' % (self.phras)
    
    
#class History(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    phr = db.Column(db.String(120))
#    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'))
#    phras = db.relationship('Phrase', backref='author', lazy='joined')
#
#    def __repr__(self):
#        return '<Period %r>' % (self.phr)
    
class Period(db.Model):
    __searchable__ = ['prd']
    
    id = db.Column(db.Integer, primary_key=True)
    examples = db.Column(db.Text)
    prd = db.Column(db.String(40), index=True)
#    phr = db.relationship('Phrase', backref='prd_html', lazy='dynamic')
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'))
#
#    def __init__(self, examples, prd)
#        self.examples = examples
#        self.prd = prd
#
    def __repr__(self):
        return '<Period %r>' % (self.prd)
