from sqlalchemy import inspect

from app.core.database import Base, engine
from app.models import item  # noqa: F401


def test_items_table_exists():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    assert "items" in inspector.get_table_names()
