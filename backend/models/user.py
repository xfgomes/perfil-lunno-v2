from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from .base import Base, PKMixin, TimestampMixin

class User(Base, PKMixin, TimestampMixin):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(32), default="user")
    organization_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"), nullable=True)

class Organization(Base, PKMixin, TimestampMixin):
    __tablename__ = "organizations"
    name: Mapped[str] = mapped_column(String(160), unique=True)
