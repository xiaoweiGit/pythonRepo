from enum import Enum, unique


@unique
class APIErrorCode(Enum):
    Success = 1
    Unknown_Error = -1
    AlreadyExist = -2


@unique
class APIErrorCodeDescription(Enum):
    Success = "Success"
    Unknown_Error = "Unknown Error"
    AlreadyExist = "Specified object already exists"
