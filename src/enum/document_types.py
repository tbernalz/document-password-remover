from enum import Enum


class DocumentType(Enum):
    PDF = "pdf"

    @classmethod
    def from_extension(cls, ext):
        ext = ext.lower()
        if ext == ".pdf":
            return cls.PDF
        else:
            raise ValueError(f"Unsupported file type: {ext}")
