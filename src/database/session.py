from database.base import session 


async def get_db():
    """Dependency for database session"""
    
    db = session()
    try:
        yield db 
    finally:
        db.close()