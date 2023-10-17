from typing import Dict, Any


class PlisioError(Exception):

    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)
        self.code = code