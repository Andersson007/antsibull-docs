import enum

from typing import List, Optional, Tuple, Union


class ReportLevel(enum.Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    SEVERE = 4
    NONE = 5


class RstcheckConfig:
    def __init__(
        self,
        report_level: Optional[ReportLevel] = ...,
        ignore_directives: Optional[List[str]] = ...,
        ignore_roles: Optional[List[str]] = ...,
        ignore_substitutions: Optional[List[str]] = ...,
        ignore_languages: Optional[List[str]] = ...,
    ): ...
