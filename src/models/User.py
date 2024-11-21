from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import registry, Mapped, mapped_column

user_registry = registry()

@user_registry.mapped_as_dataclass
class Users:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_onupdate=func.now()
    )
