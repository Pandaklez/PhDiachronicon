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
    examples = db.Column(db.String(300), index=True, unique=True)

    def __init__(self, phras, examples, definition):
        self.phras = phras
        self.definition = definition
        self.examples = examples
        
    def __repr__(self):
        return '<Phrase %r>' % (self.phras)
    
class Period(db.Model):
    __searchable__ = ['phras', 'prd', 'examples']
    
    id = db.Column(db.Integer, primary_key=True)
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'))
    phras = db.relationship('Phrase', backref='author', lazy='dynamic')
    prd = db.Column(db.String(120), index=True, unique=True)
    examples = db.Column(db.String(300), index=True, unique=True)

    def __repr__(self):
        return '<Period %r>' % (self.prd)    
#if enable_search:
#    whooshalchemy.whoosh_index(app, Phrase)
