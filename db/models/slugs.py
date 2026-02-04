from db.base import Base
from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class Slugs(Base):
    __tablename__ = 'slugs'

    id = mapped_column(Integer, primary_key=True)
    slugId = Mapped[str]
    createdAt = Mapped[datetime]
    slugString = Mapped[str]
    collectionId = Mapped[str]
    season = Mapped[str]
    member = Mapped[str]
    artist = Mapped[str]
    collectionNo = Mapped[str]
    className = Mapped[str]
    frontImage = Mapped[str]
    backImage = Mapped[str]
    backgroundColor = Mapped[str]
    textColor = Mapped[str]
    onOffline = Mapped[str]
    bandImageUrl = Mapped[str]
