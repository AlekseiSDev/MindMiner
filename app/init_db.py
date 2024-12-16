from qdrant_client.models import (
    VectorParams,
    SparseVectorParams,
    SparseIndexParams,
    Distance,
    PointStruct,
)
from qdrant_client import QdrantClient
import pickle
import time

from core.settings import settings

data = pickle.load(open(r"../data/dump.pickle", "rb"))

time.sleep(15)

qc = QdrantClient(str(settings.qdrant_host))

if not qc.collection_exists(settings.collection_name):
    qc.create_collection(
        collection_name=settings.collection_name,
        vectors_config={
            "text-dense": VectorParams(size=1024, distance=Distance.COSINE)
        },
        sparse_vectors_config={
            "text-sparse": SparseVectorParams(index=SparseIndexParams(on_disk=False))
        },
    )

    points = [PointStruct(id=i.id, vector=i.vector, payload=i.payload) for i in data]

    qc.upload_points(settings.collection_name, points)

    points_count = qc.count(settings.collection_name)

    print(f"Loaded {points_count} points into {settings.collection_name}")

else:
    print("Collection already exists.")
