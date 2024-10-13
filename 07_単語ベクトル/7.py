# 7.py 
# 66. WordSimilarity-353での評価
# The WordSimilarity-353 Test Collectionの評価データをダウンロードし，
# 単語ベクトルにより計算される類似度のランキングと，
# 人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ
import zipfile
from pathlib import Path
import pandas as pd
import scipy.stats as stats
import logging
from typing import Tuple, Optional
import seven_lib

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
INPUT_DIR = Path("data")
OUTPUT_DIR = Path("data/wordsim353")
ZIP_FILE_PATH = INPUT_DIR / "wordsim353.zip"
WORD_VECTOR_MODEL_PATH = INPUT_DIR / "GoogleNews-vectors-negative300.bin.gz"
COMBINED_CSV_PATH = OUTPUT_DIR / "combined.csv"

def ensure_data_available(zip_path: Path, extract_to: Path) -> None:
    """Ensures that the required data is available, either by extracting the zip file or using existing files."""
    if COMBINED_CSV_PATH.is_file():
        logger.info(f"{COMBINED_CSV_PATH} が既に存在します。展開をスキップします。")
        return

    if zip_path.is_file():
        extract_zip(zip_path, extract_to)
    else:
        logger.warning(f"{zip_path} が見つかりません。既存のファイルを使用します。")

def extract_zip(zip_path: Path, extract_to: Path) -> None:
    """Extracts a zip file to the specified directory."""
    extract_to.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    logger.info(f"ファイルが {extract_to} に展開されました。")

def load_data(file_path: Path) -> pd.DataFrame:
    """Loads data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        df = df.rename(columns={"Word 1": "word1", "Word 2": "word2", "Human (mean)": "human_similarity"})
        return df
    except Exception as e:
        logger.error(f"データの読み込み中にエラーが発生しました: {e}")
        raise

def calculate_vector_similarity(row: pd.Series, wvm: seven_lib.WordVectorManager) -> Optional[float]:
    """Calculates vector similarity for a word pair."""
    try:
        return wvm.cos_similarity(row['word1'], row['word2'])
    except Exception as e:
        logger.warning(f"類似度の計算中にエラーが発生しました: {row['word1']}, {row['word2']}, エラー: {e}")
        return None

def process_similarity_data(df: pd.DataFrame, wvm: seven_lib.WordVectorManager) -> pd.DataFrame:
    """Processes the similarity data by calculating vector similarities and rankings."""
    logger.info("ベクトル類似度を計算しています...")
    
    df['vector_similarity'] = df.apply(lambda row: calculate_vector_similarity(row, wvm), axis=1)
    df = df.dropna()
    df['human_rank'] = df['human_similarity'].rank(ascending=False)
    df['vector_rank'] = df['vector_similarity'].rank(ascending=False)
    return df

def display_rankings(df: pd.DataFrame, top_n: int = 10) -> None:
    """Displays the top N word pairs ranked by human and vector similarities."""
    print("人間による類似度ランキング:")
    print(df.sort_values('human_similarity', ascending=False)[['word1', 'word2', 'human_similarity']].head(top_n))
    print("\nベクトルによる類似度ランキング:")
    print(df.sort_values('vector_similarity', ascending=False)[['word1', 'word2', 'vector_similarity']].head(top_n))

def calculate_correlation(df: pd.DataFrame) -> Tuple[float, float]:
    """Calculates the Spearman correlation coefficient between human and vector rankings."""
    return stats.spearmanr(df['human_rank'], df['vector_rank'])

def main() -> None:
    try:
        ensure_data_available(ZIP_FILE_PATH, OUTPUT_DIR)
        
        if not COMBINED_CSV_PATH.is_file():
            raise FileNotFoundError(f"{COMBINED_CSV_PATH} が見つかりません。データが正しく展開されているか確認してください。")
        
        df = load_data(COMBINED_CSV_PATH)
        
        with seven_lib.WordVectorManager(WORD_VECTOR_MODEL_PATH, WORD_VECTOR_MODEL_PATH.with_suffix('')) as wvm:
            processed_df = process_similarity_data(df, wvm)
        
        display_rankings(processed_df)
        
        correlation, p_value = calculate_correlation(processed_df)
        
        logger.info(f"スピアマン相関係数: {correlation}")
        logger.info(f"p値: {p_value}")
    
    except Exception as e:
        logger.error(f"予期しないエラーが発生しました: {e}", exc_info=True)

if __name__ == "__main__":
    main()