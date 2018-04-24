from enum import Enum, unique


@unique
class APIErrorCode(Enum):
    Success = 1
    Unknown_Error = -1
    AlreadyExist = -2
    InvalidUid=-3

    AuthParasError=-10000

    DBConfigError=-200001


@unique
class APIErrorCodeDescription(Enum):
    Success = "Success"
    Unknown_Error = "Unknown Error"
    AlreadyExist = "Specified object already exists"
    InvalidUid="Invalid user id"
    AuthParasError="Missing Parameters"

    DBConfigError="Database Config Error"


@unique
class AuthCode(Enum):
    NullOrEmpty = 0x01,
    Email = 0x10,
    Phone = 0x100
