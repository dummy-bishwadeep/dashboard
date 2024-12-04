import os

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import create_database, database_exists

from scripts.config.app_configurations import DBConf
from scripts.utils.db_name_util import get_db_name
from fastapi import Depends
from sqlalchemy.orm import Session

Base = declarative_base()


def get_assistant_db(request_data: Request):
    # project_id = 'project_130'
    project_id = request_data.cookies.get("projectId", request_data.cookies.get("project_id"))
    postgres_uri = DBConf.ASSISTANT_DB_URI
    db_name = os.path.basename(postgres_uri)
    db = (
        get_db_name(project_id=project_id, database=db_name)
        if not DBConf.pg_remove_prefix
        else db_name
    )
    engine = create_engine(
        f"{os.path.dirname(postgres_uri)}/{db}",
        pool_size=int(os.getenv("PG_POOL_SIZE")),
        poolclass=QueuePool,
        pool_timeout=int(os.getenv("PG_TIMEOUT", default=30)),
        max_overflow=int(os.getenv("PG_MAX_OVERFLOW")),
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    inspector = Inspector.from_engine(engine)
    if DBConf.pg_schema not in inspector.get_schema_names():
        engine.execute(CreateSchema(DBConf.pg_schema, quote=True))
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = session_local()
    try:
        yield db
    finally:
        db.close()
        engine.dispose()
