"""VELOCITY AFRIKAANS - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY AFRIKAANS"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "AFRIKAANS"
HANDLE = "@velocityafrikaans"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "af",
    "name": "Afrikaans",
    "native_name": "Afrikaans",
    "history_key": "afrikaans",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "af-ZA-WillemNeural",
    "native_fallback_voice": "af-ZA-AdriNeural",
    "native_engine": "edge",
    "native_lang_code": "af",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "AFRIKAANS",
    "translit_label": "SAY IT LIKE",
    "greeting": "Hallo!",
    "encouragement": "Wonderlik!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Groete", "hand", "#1CB0F6"),
    ("Basic Phrases", "Basiese Frases", "chat", "#58CC02"),
    ("Common Expressions", "Algemene Uitdrukkings", "chat", "#1CB0F6"),
    ("Travel", "Reis", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurant", "fork", "#FF7A00"),
    ("Shopping", "Inkopies", "bag", "#E056A0"),
    ("Emergency", "Noodgeval", "siren", "#FF4B4B"),
    ("Family Terms", "Familie Terme", "heart", "#E056A0"),
    ("Numbers", "Getalle", "hash", "#A560E8"),
    ("Time", "Tyd", "clock", "#00A889"),
    ("Motivation", "Motivering", "rocket", "#A560E8"),
    ("Love", "Liefde", "heart", "#FF4B4B"),
    ("Success", "Sukses", "trophy", "#F5A700"),
    ("Wisdom", "Wysheid", "book", "#A560E8"),
    ("Happiness", "Geluk", "smile", "#F5A700"),
    ("Self Improvement", "Selfverbetering", "leaf", "#58CC02"),
    ("Gratitude", "Dankbaarheid", "heart", "#FF7A00"),
    ("Friendship", "Vriendskap", "users", "#00A889"),
    ("Hope", "Hoop", "sun", "#FF7A00"),
    ("Creativity", "Kreatiwiteit", "palette", "#E056A0"),
    ("Inner Peace", "Innerlike Vrede", "lotus", "#00A889"),
    ("Confidence", "Selfvertroue", "shield", "#1CB0F6"),
    ("Perseverance", "Volharding", "mountain", "#FF7A00"),
    ("Inspiration", "Inspirasie", "sparkles", "#A560E8"),
    ("Positive Life", "Positiewe Lewe", "sun", "#58CC02"),
    ("Courage", "Moed", "shield", "#FF4B4B"),
    ("Kindness", "Vriendelikheid", "heart", "#E056A0"),
    ("Patience", "Geduld", "hourglass", "#00A889"),
    ("Forgiveness", "Vergifnis", "hands", "#FF7A00"),
    ("Strength", "Krag", "dumbbell", "#FF4B4B"),
    ("Joy", "Vreugde", "smile", "#F5A700"),
    ("Balance", "Balans", "scale", "#00A889"),
    ("Growth", "Groei", "sprout", "#58CC02"),
    ("Purpose", "Doel", "target", "#A560E8"),
    ("Mindfulness", "Bewustheid", "lotus", "#00A889"),
    ("Daily Routine", "Daaglikse Roetine", "calendar", "#1CB0F6"),
    ("Weather", "Weer", "cloud", "#1CB0F6"),
    ("Feelings", "Gevoelens", "smile", "#E056A0"),
    ("Food", "Kos", "fork", "#FF7A00"),
    ("Health", "Gesondheid", "heart", "#58CC02"),
    ("Work", "Werk", "briefcase", "#1CB0F6"),
    ("Technology", "Tegnologie", "chip", "#A560E8"),
    ("Nature", "Natuur", "leaf", "#58CC02"),
    ("Animals", "Diere", "paw", "#FF7A00"),
    ("Colors", "Kleure", "palette", "#E056A0"),
    ("Directions", "Aanwysings", "compass", "#1CB0F6"),
    ("Body Parts", "Liggaamsdele", "hand", "#00A889"),
    ("Clothes", "Klere", "shirt", "#E056A0"),
    ("Music", "Musiek", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Vakansiedae", "gift", "#FF4B4B"),
    ("Education", "Onderwys", "book", "#1CB0F6"),
    ("Culture", "Kultuur", "globe", "#00A889"),
    ("Finance", "Finansies", "coin", "#58CC02"),
    ("Relationships", "Verhoudings", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnafrikaans",
    "#afrikaanslessons",
    "#afrikaansforbeginners",
    "#languagelearning",
    "#afrikaansvocabulary",
    "#velocityafrikaans",
    "#dailyafrikaans",
    "#afrikaans",
    "#learnlanguages",
    "#speakafrikaans",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
