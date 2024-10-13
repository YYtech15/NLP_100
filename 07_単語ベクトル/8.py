# 8.py 
# 67. k-meansクラスタリング
# 国名に関する単語ベクトルを抽出し，
# k-meansクラスタリングをクラスタ数k=5として実行せよ
import logging
from pathlib import Path
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seven_lib
from typing import List, Tuple

# Constants
OUTPUT_DIR = Path("data")
WORD_VECTOR_MODEL_PATH = OUTPUT_DIR / "GoogleNews-vectors-negative300.bin.gz"
NUM_CLUSTERS = 5

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def perform_kmeans_clustering(vectors: np.ndarray, n_clusters: int) -> KMeans:
    """Perform k-means clustering on the given vectors."""
    scaler = StandardScaler()
    scaled_vectors = scaler.fit_transform(vectors)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(scaled_vectors)
    return kmeans

def display_clusters(countries: List[str], kmeans: KMeans):
    """Display the countries in each cluster."""
    for i in range(NUM_CLUSTERS):
        cluster_countries = [country for country, label in zip(countries, kmeans.labels_) if label == i]
        logger.info(f"Cluster {i + 1}: {', '.join(cluster_countries)}")

def process_country_vectors(wvm: seven_lib.WordVectorManager) -> Tuple[List[str], np.ndarray]:
    """Process country vectors."""
    countries = seven_lib.get_country_names()
    logger.info(f"Retrieved {len(countries)} country names.")

    valid_countries, country_vectors = seven_lib.extract_country_vectors(countries, wvm)
    logger.info(f"Extracted vectors for {len(valid_countries)} countries.")

    if len(valid_countries) < NUM_CLUSTERS:
        raise ValueError(f"Number of extracted countries ({len(valid_countries)}) is less than the number of clusters ({NUM_CLUSTERS}).")

    return valid_countries, country_vectors

def main():
    try:
        with seven_lib.WordVectorManager(WORD_VECTOR_MODEL_PATH, WORD_VECTOR_MODEL_PATH.with_suffix('')) as wvm:
            valid_countries, country_vectors = process_country_vectors(wvm)

        kmeans = perform_kmeans_clustering(country_vectors, NUM_CLUSTERS)
        logger.info("k-means clustering completed.")

        display_clusters(valid_countries, kmeans)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()