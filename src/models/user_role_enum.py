from enum import Enum

class UserRole(str, Enum):
    DM = 'DM'
    PLAYER = 'PLAYER'