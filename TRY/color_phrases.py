from app import app, db, models_test
import re

#phr = 'по полной программе'
phr = ['по полной программе', 'на всю катушку', 'хоть отбавляй',
       'более менее','постольку-поскольку',
       'пруд пруди']
for e in phr:
        p = models_test.Phrase.query.filter_by(phras=e).first()
        print(p)
        periods = models_test.Period.query.filter_by(phrase_id=p.id)
        for pr in periods:
                nm = models_test.Phrase.query.filter_by(id=pr.phrase_id).first().phras
                #print(nm)
                #print(type('Type nm === '+ nm))
                new = r'<span class="text-primary">' + nm + r'</span>'
                #print(pr.examples)
                #print(type('Type new === ' + new))
                #print(type('Type pr.examples === ' + pr.examples))
                pr.examples = re.sub(nm, new, pr.examples)
                db.session.add(pr)
                db.session.commit()
print(pr.examples)
