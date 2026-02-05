from db.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime

class MetadataSnapshot(Base):
    __tablename__ = "metadata_snapshots"

    id = mapped_column(Integer, primary_key=True)
    slug = mapped_column(String)
    total = mapped_column(String)
    spin = mapped_column(String)
    transferable = mapped_column(String)
    snapshotTimestamp = mapped_column(DateTime(timezone = True))

