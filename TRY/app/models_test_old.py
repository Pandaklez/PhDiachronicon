from app import db, app

#import sys
#if sys.version_info >= (3, 0):
#    enable_search = False
#else:
#    enable_search = True
#    import flask_whooshalchemy as whooshalchemy

#import flask.ext.whooshalchemy

class Phrase(db.Model):
    __searchable__ = ['phrase', 'definition', 'examples']
    
    id = db.Column(db.Integer, primary_key=True)
    phras = db.Column(db.String(60), index=True, unique=True)
    definition = db.Column(db.String(120), index=True, unique=True)
#    examples = db.Column(db.String(300), index=True, unique=True)
    phr = db.relationship('History', backref='author', lazy='dynamic')
#    prd = db.relationship('Period', backref='author', lazy='dynamic')

#    def __init__(self, phras, definition):
#        self.phras = phras
#        self.definition = definition
#        self.examples = examples
        
    
    
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phr = db.Column(db.String(120))
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'))

    def __repr__(self):
        return '<Period %r>' % (self.phr)
    
class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    examples = db.Column(db.String(300))
    prd = db.Column(db.String(120))
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'))

#    def __init__(self, examples, prd)
#        self.examples = examples
#        self.prd = prd

    def __repr__(self):
        return '<Period %r>' % (self.prd)
    
#if enable_search:
#    whooshalchemy.whoosh_index(app, Phrase)
