from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


# =========================
# Users
# =========================

async def create_user(
    db: AsyncSession,
    user: schemas.UserCreate
):
    db_user = models.User(
        name=user.name
    )

    db.add(db_user)

    await db.commit()

    await db.refresh(db_user)

    return db_user


async def get_users(
    db: AsyncSession
):
    result = await db.execute(
        select(models.User)
    )

    return result.scalars().all()


# =========================
# Notes
# =========================

async def create_note(
    db: AsyncSession,
    note: schemas.NoteCreate,
    user_id: int
):
    db_note = models.Note(
        **note.model_dump(),
        owner_id=user_id
    )

    db.add(db_note)

    await db.commit()

    await db.refresh(db_note)

    return db_note


async def get_notes(
    db: AsyncSession
):
    result = await db.execute(
        select(models.Note)
    )

    return result.scalars().all()


async def get_note(
    db: AsyncSession,
    note_id: int
):
    result = await db.execute(
        select(models.Note)
        .where(models.Note.id == note_id)
    )

    return result.scalar_one_or_none()


async def delete_note(
    db: AsyncSession,
    note_id: int
):
    note = await get_note(
        db,
        note_id
    )

    if not note:
        return None

    await db.delete(note)

    await db.commit()

    return note