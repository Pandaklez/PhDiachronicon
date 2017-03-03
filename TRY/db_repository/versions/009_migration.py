from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
phrase = Table('phrase', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('phras', String(length=60)),
    Column('definition', String(length=120)),
    Column('comments', String(length=400)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['phrase'].columns['comments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['phrase'].columns['comments'].drop()
