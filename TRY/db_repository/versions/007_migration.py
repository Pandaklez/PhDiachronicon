from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
period = Table('period', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('examples', TEXT),
    Column('prd', VARCHAR(length=40)),
    Column('phrase_id', INTEGER),
)

phrase = Table('phrase', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('phras', String(length=60)),
    Column('definition', String(length=120)),
    Column('period_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['period'].columns['phrase_id'].drop()
    post_meta.tables['phrase'].columns['period_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['period'].columns['phrase_id'].create()
    post_meta.tables['phrase'].columns['period_id'].drop()
