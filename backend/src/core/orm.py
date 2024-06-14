import datetime
from sqlalchemy import ForeignKey, String, Date, Time, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_utils.types.password import PasswordType

from typing import Annotated

class Base(DeclarativeBase):
    pass

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.now
)]

str_60 = Annotated[str, mapped_column(String(60))]
str_60_unique = Annotated[str, mapped_column(String(60), unique=True)]


class UsersModel(Base):
    __tablename__ = "users"
    
    id: Mapped[intpk]
    username: Mapped[str_60_unique]
    email: Mapped[str] = mapped_column(String(60), nullable=True)
    password: Mapped[str] = mapped_column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))

class ReportsModel(Base):
    __tablename__ = "reports"

    id: Mapped[intpk]  
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    mood_rating: Mapped[int]
    comment: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class ReflectionsModel(Base):
    __tablename__ = "reflections"

    id: Mapped[intpk]
    report_id: Mapped[int] = mapped_column(ForeignKey("reports.id"))
    text: Mapped[str]

    updated_at: Mapped[updated_at]

class SessionsModel(Base):
    __tablename__ = "sessions"
    
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))