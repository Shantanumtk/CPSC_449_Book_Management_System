from pydantic import BaseModel, Field
from typing import Optional
# Base schema for book
# Base schema defining common book attributes with example values
class BookBase(BaseModel):
    title: str 
    author: str = Field(..., example="Mr Novel")
    description: Optional[str]  = Field(None, example="A classic novel.")

# Schema for creating a book
#Schema for creating a new book (inherits from BookBase)
class BookCreate(BookBase):
    pass

# Schema for updating a book
# Schema for updating an existing book with optional fields
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str]  = None
    description: Optional[str]  = None

# Schema for response
# Schema for book response, adds an ID for database records
class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
