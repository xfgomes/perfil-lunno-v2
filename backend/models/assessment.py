from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON, ForeignKey, Float
from .base import Base, PKMixin, TimestampMixin

class Assessment(Base, PKMixin, TimestampMixin):
    __tablename__ = "assessments"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    version: Mapped[str] = mapped_column(String(20), default="v1")
    bigfive: Mapped[dict] = mapped_column(JSON, default={})
    disc: Mapped[dict] = mapped_column(JSON, default={})
    archetype: Mapped[dict] = mapped_column(JSON, default={})
    softskills: Mapped[dict] = mapped_column(JSON, default={})
    sjt_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    narrative_report_individual: Mapped[str | None] = mapped_column(String(20000), nullable=True)
