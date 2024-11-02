from enum import Enum


class FileType(Enum):
    PDF = "pdf"
    WORD = "docx"
    EXCEL = "xlsx"

    @classmethod
    def from_extension(cls, ext):
        ext = ext.lower()
        if ext == ".pdf":
            return cls.PDF
        elif ext in [".docx", ".doc"]:
            return cls.WORD
        elif ext in [".xlsx", ".xls"]:
            return cls.EXCEL
        else:
            raise ValueError(f"Unsupported file type: {ext}")
