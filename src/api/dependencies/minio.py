from services.minio_service import MinioService


minio = MinioService()

async def get_minio_service() -> MinioService:
    """Returns connect to Minio"""   
    return minio 