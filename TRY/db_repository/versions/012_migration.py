from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
period = Table('period', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('examples', Text),
    Column('prd', String(length=40)),
    Column('interval', String(length=11)),
    Column('comment', String(length=400)),
    Column('phrase_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['period'].columns['comment'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['period'].columns['comment'].drop()
