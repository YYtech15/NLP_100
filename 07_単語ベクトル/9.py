# 9.py 
# 68. Ward法によるクラスタリング
# 国名に関する単語ベクトルに対し，Ward法による階層型クラスタリングを実行せよ．
# さらに，クラスタリング結果をデンドログラムとして可視化せよ．
import logging
from pathlib import Path
import numpy as np
import seven_lib
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple

# Constants
OUTPUT_DIR = Path("data")
WORD_VECTOR_MODEL_PATH = OUTPUT_DIR / "GoogleNews-vectors-negative300.bin.gz"
OUTPUT_IMAGE = "graph68.png"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def perform_ward_clustering(vectors: np.ndarray) -> np.ndarray:
    """Perform Ward hierarchical clustering on the given vectors."""
    scaler = StandardScaler()
    scaled_vectors = scaler.fit_transform(vectors)
    
    return linkage(scaled_vectors, method='ward')

def create_dendrogram(linkage_matrix: np.ndarray, labels: List[str]):
    """Create and save a dendrogram of the clustering results."""
    plt.figure(figsize=(20, 10))
    dendrogram(linkage_matrix, labels=labels, leaf_rotation=90, leaf_font_size=6)
    plt.title("Hierarchical Clustering Dendrogram (Ward)")
    plt.xlabel("Country")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE)
    logger.info(f"Dendrogram saved as {OUTPUT_IMAGE}")

def process_country_vectors(wvm: seven_lib.WordVectorManager) -> Tuple[List[str], np.ndarray]:
    """Process country vectors."""
    countries = seven_lib.get_country_names()
    logger.info(f"Retrieved {len(countries)} country names.")

    valid_countries, country_vectors = seven_lib.extract_country_vectors(countries, wvm)
    logger.info(f"Extracted vectors for {len(valid_countries)} countries.")

    return valid_countries, country_vectors

def main():
    try:
        with seven_lib.WordVectorManager(WORD_VECTOR_MODEL_PATH, WORD_VECTOR_MODEL_PATH.with_suffix('')) as wvm:
            valid_countries, country_vectors = process_country_vectors(wvm)

        linkage_matrix = perform_ward_clustering(country_vectors)
        logger.info("Ward hierarchical clustering completed.")

        create_dendrogram(linkage_matrix, valid_countries)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()