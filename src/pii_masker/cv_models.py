from pydantic import BaseModel, EmailStr, Field

# --- Sub-models -----------------------------------------------------------

class Contact(BaseModel):
    """Structured contact information."""
    location: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    linkedin: str | None = None


class Language(BaseModel):
    """A spoken language with an optional proficiency level."""
    name: str
    level: str | None = None  # e.g. "native", "fluent", "professional", "B2"


class Experience(BaseModel):
    """A single work experience entry."""
    role: str
    company: str
    location: str | None = None
    start: str  # e.g. "2023" or "2023-01"
    end: str = "present"  # e.g. "present", "2024", or "2024-06"
    bullets: list[str] = []


class Education(BaseModel):
    """A single education entry."""
    degree: str
    school: str
    year: str  # e.g. "2020" or "2018–2020"


class CustomSection(BaseModel):
    """A free-form extra section (e.g. open source, talks, awards)."""
    title: str
    items: list[str] = []


# --- Root model ------------------------------------------------------------

class Cv(BaseModel):
    """Root CV schema. All sections are optional except name and title."""
    name: str
    title: str
    contact: Contact = Field(default_factory=Contact)
    languages: list[Language] = []
    profile: str | None = None
    experience: list[Experience] = []
    education: list[Education] = []
    skills: dict[str, str] = Field(
        default_factory=dict,
        description="Category -> comma-separated skill list, e.g. {'Backend': 'Python, FastAPI'}",
    )
    sections: list[CustomSection] = []