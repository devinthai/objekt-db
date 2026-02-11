from db.base import Base
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column

class Slugs(Base):
    __tablename__ = 'slugs'

    id = mapped_column(Integer, primary_key=True)
    slugId = mapped_column(String, unique=True)
    createdAt = mapped_column(DateTime(timezone=True))
    slugString = mapped_column(String)
    collectionId = mapped_column(String)
    season = mapped_column(String)
    member = mapped_column(String)
    artist = mapped_column(String)
    collectionNo = mapped_column(String)
    className = mapped_column(String)
    frontImage = mapped_column(String)
    backImage = mapped_column(String)
    backgroundColor = mapped_column(String)
    textColor = mapped_column(String)
    onOffline = mapped_column(String)
    bandImageUrl = mapped_column(String)
    workBatch = mapped_column(Integer)
