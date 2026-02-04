from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer 
from datetime import datetime

class MetadataSnapshot(Base):
    __tablename__ = "metadata_snapshots"

    id = mapped_column(Integer, primary_key=True)
    slug = Mapped[str]
    total = Mapped[int]
    spin = Mapped[int]
    transferable = Mapped[int]
    snapshotTimestamp = Mapped[datetime]

