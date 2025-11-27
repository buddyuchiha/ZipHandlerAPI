import enum


class TaskStatus(enum.Enum):
    """Task status enumeration"""
    
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"