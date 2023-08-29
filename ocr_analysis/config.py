from pathlib import Path
from dynaconf import Dynaconf

BASE_DIR = Path(__file__).resolve().parent.parent

settings = Dynaconf (
    load_dotenv = True,
    envvar_prefix_for_dynaconf = False,
    dotenv_path = str(BASE_DIR.joinpath("envs",".env")),
)
DATA_PATTERN = {
    "PHONE_NUMBER": r'(?<!\d)(?:\+90|0)?[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}(?!\d)',
    "CREDIT_CARD_NUMBER": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    "URL":r'\bhttps?://[^\s/]+\b',
    "COMBOLIST":r'\b[A-Za-z0-9._%+-]+:[A-Za-z0-9._%+-]+\b',
    "EMAIL":r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',
    "DOMAIN": r'(?<!@)\b([a-zA-Z0-9-]+\.[a-zA-Z]{2,6})(?=\s|$|,)',
    "HASH": r'\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b',
    "DATES":r'\b\d{2}/\d{2}/\d{4}\b',
    "PLATE":r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b',
    "ID_NUMBER": r"\b[1-9]\d{10}\b"
}
