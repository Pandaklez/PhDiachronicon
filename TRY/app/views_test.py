from flask import render_template, redirect, url_for, request, flash
from app import app, db
from .models_test import Phrase

import json
import os.path

#global base
@app.route('/')
def home():
    redirc = url_for('table')
    ssearch = url_for('search')
    return render_template('base.html',
                           redirect=redirc,
                           ssearch=ssearch)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('notfound.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/table')
def table():
    #global base
    f = open('base.json', 'w', encoding = 'utf-8')
    base = [
        {
            'name' : 'на всю катушку',
            'definition': 'intensificator',
            'examples': ['Beautiful day in Portland! Rock!1! На всю катушку']
        },
        {
            'name' : 'в полной мере',
            'definition': 'intensificator',
            'examples': ['The Avengers movie впечатлило меня в полной мере!']
        }
    ]
    bs = json.dumps(base, ensure_ascii = False)
    f.write(bs)
    f.close()
    return render_template('table.html',
                           title='Table',
                           base=base)

@app.route('/simplesearch')
def search():
    f = open('base.json', 'r', encoding = 'utf-8')
    s = f.read()
    f.close()
    base = json.loads(s)
    i = 0
    global names #это потом надо убрать
    names = []
    while i < len(base):
        for key in base[i]:
            if key == 'name':
                names.append(base[i][key])
        i += 1
    if not os.path.exists('history.txt'):
        f = open('history.txt', 'w', encoding = 'utf-8')
        f.close()
    if request.args:
        global phr
        phr = request.args['phrase']
        f = open('history.txt', 'a', encoding = 'utf-8')
        hs = phr
        f.write('\n' + hs)
        f.close()
        if phr in names:
            return redirect(url_for('result'))
        else:
            return render_template('notfound.html')
    return render_template('search_form.html',
                           title='Search')

@app.route('/result')
def result():
    return render_template('result.html',
                           title='Results',
                           phrase = phr)
