# 10.py 
# 69. t-SNEによる可視化
# ベクトル空間上の国名に関する単語ベクトルをt-SNEで可視化せよ．
import logging
from pathlib import Path
import numpy as np
import seven_lib
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple

# Constants
OUTPUT_DIR = Path("data")
WORD_VECTOR_MODEL_PATH = OUTPUT_DIR / "GoogleNews-vectors-negative300.bin.gz"
OUTPUT_IMAGE = "graph69.png"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def perform_tsne(vectors: np.ndarray) -> np.ndarray:
    """Perform t-SNE on the given vectors."""
    scaler = StandardScaler()
    scaled_vectors = scaler.fit_transform(vectors)
    
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
    return tsne.fit_transform(scaled_vectors)

def visualize_tsne(tsne_results: np.ndarray, labels: List[str]):
    """Create and save a t-SNE visualization."""
    plt.figure(figsize=(16, 12))
    plt.scatter(tsne_results[:, 0], tsne_results[:, 1], alpha=0.7)
    
    for i, label in enumerate(labels):
        plt.annotate(label, (tsne_results[i, 0], tsne_results[i, 1]), fontsize=8, alpha=0.8)
    
    plt.title("t-SNE visualization of country word vectors")
    plt.xlabel("t-SNE feature 1")
    plt.ylabel("t-SNE feature 2")
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE, dpi=300, bbox_inches='tight')
    logger.info(f"t-SNE visualization saved as {OUTPUT_IMAGE}")

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

        tsne_results = perform_tsne(country_vectors)
        logger.info("t-SNE transformation completed.")

        visualize_tsne(tsne_results, valid_countries)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()