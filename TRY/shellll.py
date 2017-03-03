Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from app import db, models
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from app import db, models
ImportError: cannot import name 'models'
>>> from app import db, models_test
>>> u = models_test.Phrase(phrase='пруд пруди', definition='N-GEN. ПРУД_ПРУДИ', examples='Медом и маслом хоть пруд пруди… ветер взвивает муку вместо пыли')
>>> u = models_test.query.get(1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    u = models_test.query.get(1)
AttributeError: module 'app.models_test' has no attribute 'query'
>>> u = models_test.Phrase.query.get(1)
>>> u
>>> u
>>> u = models_test.Phrase.query.get(2)
>>> u
>>> users = models_test.Phrase.query.all()
>>> users
[]
>>> db.session.add(u)
Traceback (most recent call last):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\session.py", line 1673, in add
    state = attributes.instance_state(instance)
AttributeError: 'NoneType' object has no attribute '_sa_instance_state'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    db.session.add(u)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\scoping.py", line 157, in do
    return getattr(self.registry(), name)(*args, **kwargs)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\session.py", line 1675, in add
    raise exc.UnmappedInstanceError(instance)
sqlalchemy.orm.exc.UnmappedInstanceError: Class 'builtins.NoneType' is not mapped
>>> u = models_test.Phrase(phrase='пруд пруди', definition='N-GEN. ПРУД_ПРУДИ', examples='Медом и маслом хоть пруд пруди… ветер взвивает муку вместо пыли')
>>> db.session.add(u)
>>> db.session.commit()
>>> users = models_test.Phrase.query.all()
>>> users
[<Phrase 'пруд пруди'>]
>>> u = models_test.Phrase.query.get(1)
>>> u
<Phrase 'пруд пруди'>
>>> u = models_test.Phrase(phrase='хоть отбавляй', definition='N-GEN. ХОТЬ_ОТБАВЛЯЙ', examples='У нас тут этого добра - хоть отбавляй!')
>>> db.session.add(u)
>>> db.session.commit()
>>> users = models_test.Phrase.query.all()
>>> users
[<Phrase 'пруд пруди'>, <Phrase 'хоть отбавляй'>]
>>> type(users)
<class 'list'>
>>> type(u)
<class 'app.models_test.Phrase'>
>>> for post in Phrase.query.all():
	db.session.delete(post)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for post in Phrase.query.all():
NameError: name 'Phrase' is not defined
>>> for post in models_test.Phrase.query.all():
	db.session.delete(post)

	
>>> db.session.commit()
>>> from app.models import Phrase
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    from app.models import Phrase
ImportError: No module named 'app.models'
>>> from app.models_test import Phrase
>>> from app import db
>>> p = Phrase(phrase='хоть отбавляй', definition='N-GEN. ХОТЬ_ОТБАВЛЯЙ', examples='У нас тут этого добра - хоть отбавляй!')
>>> db.session.add(p)
>>> db.session.commit()
>>> p = Phrase(phrase='пруд пруди', definition='N-GEN. ПРУД_ПРУДИ', examples='Медом и маслом хоть пруд пруди… ветер взвивает муку вместо пыли')
>>> db.session.add(p)
>>> db.session.commit()
>>> Phrase.query.whoosh_search('пруд').all()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    Phrase.query.whoosh_search('пруд').all()
AttributeError: 'BaseQuery' object has no attribute 'whoosh_search'
>>> Phrase.query.whoosh_search('пруд').all()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    Phrase.query.whoosh_search('пруд').all()
AttributeError: 'BaseQuery' object has no attribute 'whoosh_search'
>>> q = session.query(Phrase)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    q = session.query(Phrase)
NameError: name 'session' is not defined
>>> q = db.session.query(Phrase)
>>> result = q.whooshee_search(query).all()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    result = q.whooshee_search(query).all()
AttributeError: 'Query' object has no attribute 'whooshee_search'
>>> q.whoosh_search('пруд').all()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    q.whoosh_search('пруд').all()
AttributeError: 'Query' object has no attribute 'whoosh_search'
>>> result = Phrase.query.whoosh_search('пруд')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    result = Phrase.query.whoosh_search('пруд')
AttributeError: 'BaseQuery' object has no attribute 'whoosh_search'
>>> db.session.query(Phrase).filter(Phrase.phrase=='пруд')
<sqlalchemy.orm.query.Query object at 0x03E61110>
>>> q = sess.query(Phrase)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    q = sess.query(Phrase)
NameError: name 'sess' is not defined
>>> for post in models_test.Phrase.query.all():
	db.session.delete(post)

	
>>> db.session.commit()
>>>  import flask.ext.whooshalchemy as whooshalchemy
 
SyntaxError: unexpected indent
>>> import flask.ext.whooshalchemy as whooshalchemy

Warning (from warnings module):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask\exthook.py", line 71
    .format(x=modname), ExtDeprecationWarning
ExtDeprecationWarning: Importing flask.ext.whooshalchemy is deprecated, use flask_whooshalchemy instead.

Warning (from warnings module):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask\exthook.py", line 71
    .format(x=modname), ExtDeprecationWarning
ExtDeprecationWarning: Importing flask.ext.sqlalchemy is deprecated, use flask_sqlalchemy instead.
>>> import flask_whooshalchemy as whooshalchemy
>>>  from app import app
 
SyntaxError: unexpected indent
>>> from app import app
>>> from app.models_test import Phrase
>>> whooshalchemy.whoosh_index(app, Phrase)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    whooshalchemy.whoosh_index(app, Phrase)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 172, in whoosh_index
    _create_index(app, model))
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 192, in _create_index
    schema, primary_key = _get_whoosh_schema_and_primary_key(model)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 215, in _get_whoosh_schema_and_primary_key
    searchable = set(model.__searchable__)
AttributeError: type object 'Phrase' has no attribute '__searchable__'
>>> whooshalchemy.whoosh_index(app, Phrase.phrase)
Traceback (most recent call last):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\sql\elements.py", line 676, in __getattr__
    return getattr(self.comparator, key)
AttributeError: 'Comparator' object has no attribute '__name__'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\attributes.py", line 185, in __getattr__
    return getattr(self.comparator, key)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\util\langhelpers.py", line 840, in __getattr__
    return self._fallback_getattr(key)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\properties.py", line 267, in _fallback_getattr
    return getattr(self.__clause_element__(), key)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\sql\elements.py", line 682, in __getattr__
    key)
AttributeError: Neither 'AnnotatedColumn' object nor 'Comparator' object has an attribute '__name__'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    whooshalchemy.whoosh_index(app, Phrase.phrase)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 171, in whoosh_index
    return app.whoosh_indexes.get(model.__name__,
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\sqlalchemy\orm\attributes.py", line 193, in __getattr__
    key)
AttributeError: Neither 'InstrumentedAttribute' object nor 'Comparator' object associated with Phrase.phrase has an attribute '__name__'
>>> whooshalchemy.whoosh_index(app, Phrase)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    whooshalchemy.whoosh_index(app, Phrase)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 172, in whoosh_index
    _create_index(app, model))
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 192, in _create_index
    schema, primary_key = _get_whoosh_schema_and_primary_key(model)
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask_whooshalchemy.py", line 215, in _get_whoosh_schema_and_primary_key
    searchable = set(model.__searchable__)
AttributeError: type object 'Phrase' has no attribute '__searchable__'
>>> 
=============== RESTART: E:\Anni Docs\ВЫШКА\python\TRY\run.py ===============

Warning (from warnings module):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask\exthook.py", line 71
    .format(x=modname), ExtDeprecationWarning
ExtDeprecationWarning: Importing flask.ext.whooshalchemy is deprecated, use flask_whooshalchemy instead.

Warning (from warnings module):
  File "C:\Users\Anna\AppData\Local\Programs\Python\Python35-32\lib\site-packages\flask\exthook.py", line 71
    .format(x=modname), ExtDeprecationWarning
ExtDeprecationWarning: Importing flask.ext.sqlalchemy is deprecated, use flask_sqlalchemy instead.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
