from enum import Enum


class DocumentType(Enum):
    PDF = "pdf"
    WORD = "docx"

    @classmethod
    def from_extension(cls, ext):
        ext = ext.lower()
        if ext == ".pdf":
            return cls.PDF
        elif ext in [".docx", ".doc"]:
            return cls.WORD
        else:
            raise ValueError(f"Unsupported file type: {ext}")
