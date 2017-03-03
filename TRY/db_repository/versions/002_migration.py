from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
phrase = Table('phrase', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('phrase', VARCHAR(length=60)),
    Column('definition', VARCHAR(length=120)),
    Column('examples', VARCHAR(length=300)),
)

phrase = Table('phrase', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('phras', String(length=60)),
    Column('definition', String(length=120)),
    Column('examples', String(length=300)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['phrase'].columns['phrase'].drop()
    post_meta.tables['phrase'].columns['phras'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['phrase'].columns['phrase'].create()
    post_meta.tables['phrase'].columns['phras'].drop()
