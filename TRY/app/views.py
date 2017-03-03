from flask import render_template, redirect, url_for, request, flash
from app import app, db, models_test
from .models_test import *

import json
import os.path

@app.route('/')
def home():
    redirc = url_for('table')
    ssearch = url_for('search')
    xsearch = url_for('xsearch')
    history = url_for('history')
    return render_template('home.html',
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('notfound.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/table')
def table():
    xsearch = url_for('xsearch')
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
# That is just a new commit to the table. We need it only once by now.
#    u1= models_test.Phrase(phras='на всю катушку',
#                            definition='V НА_ВСЮ_КАТУШКУ')
#    db.session.add(u1)
#    u2 = models_test.Phrase(phras='хоть отбавляй',
#                            definition='N-GEN. ХОТЬ_ОТБАВЛЯЙ')
#    db.session.add(u2)
#    db.session.commit()
    bs = models_test.Phrase.query.all()
    return render_template('table.html',
                           title='Table',
                           base=bs,
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.route('/simplesearch')
def search():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')
    
    bs = models_test.Phrase.query.all()
#    b = models_test.History.query.all()
    flash('%s' % bs)
#    flash('%s' % b)
    if not os.path.exists('history.txt'):
        f = open('history.txt', 'w', encoding = 'utf-8')
        f.close()
        
    if request.args:
        global p
        phr = request.args['phrase']
#        This is the next step: making history page
#        db.session.add(phr)
#        db.session.commit()
        p = Phrase.query.filter_by(phras=phr).first()
        if p != None:
            return redirect(url_for('result'))
        else:
            return render_template('notfound.html',
                                   redirect=redirc,
                                   ssearch=ssearch,
                                   xsearch=xsearch,
                                   history=history)
    return render_template('search_form.html',
                           title='Search',
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)
#        for ele in bs:
#            flash('%s' % ele.phras)
#            if phr == ele.phras:
#                f = open('history.txt', 'a', encoding = 'utf-8')
#                hs = phr
#                f.write('\n' + hs)
#                f.close()
#                global p
#                p = Phrase.query.filter_by(phras=phr).first()
#                return redirect(url_for('result'))
#            else:
#                return render_template('notfound.html')
#    return render_template('search_form.html',
#                           title='Search')

@app.route('/result')
def result():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')
    periods = Period.query.filter_by(phrase_id=p.id)
    
#bs = models_test.Phrase.query.all()
    return render_template('result.html',
                           title='Results',
                           periods=periods,
                           phrase=p,
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.route('/extended_search')
def xsearch():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')
    m_s = url_for('models')
    
    bs = models_test.Period.query.all()
    flash('%s' % bs)
        
    if request.args:
        global dt
        dat = request.args['dates']
        dt = Period.query.filter_by(prd=dat)
        if dt != None:
            return redirect(url_for('xresult'))
        else:
            return render_template('notfound.html',
                                   redirect=redirc,
                                   ssearch=ssearch,
                                   xsearch=xsearch,
                                   history=history)
#    if request.args:
#        global defi
#        defin = request.args['defin']
#        defi = Phrase.query.filter_by(definintion=defin)
#        if defi != None:
#            return redirect(url_for('x1result'))
#        else:
#            return render_template('notfound.html',
#                                   redirect=redirc,
#                                   ssearch=ssearch,
#                                   xsearch=xsearch,
#                                   history=history)
    return render_template('xsearch_form.html',
                           title='Search',
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           m_s=m_s,
                           history=history)

@app.route('/xresult')
def xresult():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')

    return render_template('xresult.html',
                           title='Results of extended search',
                           dates=dt,
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.route('/models_search')
def models():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')

    if request.args:
        global mdl
        model = request.args['defin']
        mdl = Phrase.query.filter_by(definition=model)
        if mdl != None:
            return redirect(url_for('mresult'))
        else:
            return render_template('notfound.html',
                                   redirect=redirc,
                                   ssearch=ssearch,
                                   xsearch=xsearch,
                                   history=history)
    return render_template('msearch_form.html',
                           title='Models search form',
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.route('/mresult')
def mresult():
    redirc = url_for('table')
    ssearch = url_for('search')
    history = url_for('history')
    xsearch = url_for('xsearch')
    
    #periods = Period.query.filter_by(phrase_id=mdl.id)

    return render_template('mresult.html',
                           title='Results of extended search',
                           definitions=mdl,
                           #periods=periods,
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)

@app.route('/history')
def history():
    redirc = url_for('table')
    ssearch = url_for('search')
    xsearch = url_for('xsearch')
    history = url_for('history')
    
    bs = models_test.Phrase.query.all()
    
    f = open('history.txt', 'r', encoding = 'utf-8')
    hs = f.readlines()
    f.close()
    
    s = []
    for el in hs[1:9]:
        el = el.strip('\n')
        s.append(el)
    return render_template('history.html',
                           title='Search history',
                           ss=s,
                           redirect=redirc,
                           ssearch=ssearch,
                           xsearch=xsearch,
                           history=history)
