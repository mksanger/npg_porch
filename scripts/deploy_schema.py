#!/usr/bin/env python

# Replace with Alembic in due course

import os
import sqlalchemy
from sqlalchemy import text

from npg_porch.db.models import Base

db_url = os.environ.get("DB_URL")
schema_name = os.environ.get("DB_SCHEMA")
if schema_name is None:
    schema_name = "npg_porch"

print(f"Deploying npg_porch tables to schema {schema_name}")

engine = sqlalchemy.create_engine(
    db_url, connect_args={"options": f"-csearch_path={schema_name}"}
)

Base.metadata.schema = schema_name
Base.metadata.create_all(
    engine,
    tables=[
        table for name, table in Base.metadata.tables.items() if name != "latest_event"
    ],
)
with engine.begin() as connection:
    connection.execute(
        text(
            "CREATE VIEW latest_event AS SELECT max(event.time) AS "
            "status_date, event.task_id AS task_id FROM event GROUP BY event.task_id;"
        )
    )
