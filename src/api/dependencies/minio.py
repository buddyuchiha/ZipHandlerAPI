from services.minio_service import MinioService


minio = MinioService()

async def get_minio_service() -> MinioService:
    return minio 