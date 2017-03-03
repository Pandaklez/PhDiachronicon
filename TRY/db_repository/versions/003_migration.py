from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
period = Table('period', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('examples', String(length=300)),
    Column('prd', String(length=120)),
    Column('phrase_id', Integer),
)

phrase = Table('phrase', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('definition', VARCHAR(length=120)),
    Column('examples', VARCHAR(length=300)),
    Column('phras', VARCHAR(length=60)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['period'].create()
    pre_meta.tables['phrase'].columns['examples'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['period'].drop()
    pre_meta.tables['phrase'].columns['examples'].create()
