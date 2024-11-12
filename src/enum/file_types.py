from enum import Enum


class FileType(Enum):
    PDF = "pdf"
    WORD = "docx"
    EXCEL = "xlsx"
    POWERPOINT = "pptx"

    @classmethod
    def from_extension(cls, ext):
        ext = ext.lower()
        if ext == ".pdf":
            return cls.PDF
        elif ext in [".docx", ".doc"]:
            return cls.WORD
        elif ext in [".xlsx", ".xls"]:
            return cls.EXCEL
        elif ext in [".pptx", ".ppt"]:
            return cls.POWERPOINT
        else:
            raise ValueError(f"Unsupported file type: {ext}")
