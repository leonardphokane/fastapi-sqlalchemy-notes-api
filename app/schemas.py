from typing import List

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


# =========================
# Note Schemas
# =========================

class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================
# User Schemas
# =========================

class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class User(UserBase):
    id: int

    notes: List[Note] = Field(
        default_factory=list
    )

    model_config = ConfigDict(
        from_attributes=True
    )