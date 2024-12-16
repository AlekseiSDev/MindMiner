from qdrant_client.models import (
    VectorParams,
    SparseVectorParams,
    SparseIndexParams,
    Distance,
    PointStruct,
)
from qdrant_client import QdrantClient
import pickle

from core.settings import settings

data = pickle.load(open(r"../data/dump.pickle", "rb"))

qc = QdrantClient(settings.qdrant_host)

qc.create_collection(
    collection_name=settings.collection_name,
    vectors_config={"text-dense": VectorParams(size=1024, distance=Distance.COSINE)},
    sparse_vectors_config={
        "text-sparse": SparseVectorParams(index=SparseIndexParams(on_disk=False))
    },
)

points = [PointStruct(id=i.id, vector=i.vector, payload=i.payload) for i in data]

qc.upload_points(settings.collection_name, points)

points_count = qc.count(settings.collection_name)

print(f"Loaded {points_count} points into {settings.collection_name}")
