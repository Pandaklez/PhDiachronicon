from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
period = Table('period', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('examples', VARCHAR(length=300)),
    Column('prd', VARCHAR(length=120)),
    Column('phrase_id', INTEGER),
    Column('prd_int', INTEGER),
)

history = Table('history', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('phr', String(length=120)),
    Column('phrase_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['period'].drop()
    post_meta.tables['history'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['period'].create()
    post_meta.tables['history'].drop()
