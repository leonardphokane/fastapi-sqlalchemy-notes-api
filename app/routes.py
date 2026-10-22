from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from . import (
    crud,
    schemas,
    database
)

router = APIRouter(
    tags=["Notes API"]
)


# =========================
# Users
# =========================

@router.post(
    "/users/",
    response_model=schemas.UserResponse
)
async def create_user(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(
        database.get_db
    )
):
    return await crud.create_user(
        db,
        user
    )


@router.get(
    "/users/",
    response_model=List[schemas.UserResponse]
)
async def read_users(
    db: AsyncSession = Depends(
        database.get_db
    )
):
    return await crud.get_users(db)


# =========================
# Notes
# =========================

@router.post(
    "/users/{user_id}/notes/",
    response_model=schemas.Note
)
async def create_note_for_user(
    user_id: int,
    note: schemas.NoteCreate,
    db: AsyncSession = Depends(
        database.get_db
    )
):
    return await crud.create_note(
        db,
        note,
        user_id
    )


@router.get(
    "/notes/",
    response_model=List[schemas.Note]
)
async def read_notes(
    db: AsyncSession = Depends(
        database.get_db
    )
):
    return await crud.get_notes(db)


@router.get(
    "/notes/{note_id}",
    response_model=schemas.Note
)
async def read_note(
    note_id: int,
    db: AsyncSession = Depends(
        database.get_db
    )
):
    note = await crud.get_note(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


@router.delete(
    "/notes/{note_id}"
)
async def delete_note(
    note_id: int,
    db: AsyncSession = Depends(
        database.get_db
    )
):
    note = await crud.delete_note(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return {
        "message": "Note deleted successfully"
    }