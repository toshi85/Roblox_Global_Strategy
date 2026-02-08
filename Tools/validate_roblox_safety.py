import sys
import re
import os

LOG_FILE = "roblox_safety_validation.log"

# === BANNED WORDS (English + Japanese) ===
BANNED_WORDS = {
    # Violence (English)
    r"\bkill\b": "NG: 'kill'. Use 'eliminate', 'defeat'.",
    r"\bmurder\b": "NG: 'murder'. Use 'eliminate'.",
    r"\bdie\b": "NG: 'die'. Use 'gone', 'eliminated'.",
    r"\bdeath\b": "NG: 'death'. Use 'end', 'defeat'.",
    r"\bblood\b": "NG: 'blood'. Avoid graphic violence.",
    r"\bgore\b": "NG: 'gore'. Avoid graphic violence.",

    # Sexual (English)
    r"\bsex\b": "NG: 'sex'. Topic prohibited.",
    r"\bnude\b": "NG: 'nude'. Topic prohibited.",
    r"\bnaked\b": "NG: 'naked'. Topic prohibited.",
    r"\bporn\b": "NG: 'porn'. Topic prohibited.",
    r"\bkiss(?:ing)?\b": "NG: 'kiss/kissing'. Avoid romantic content.",

    # Gambling (English)
    r"\bgambl(?:e|ing)\b": "NG: 'gamble/gambling'. Topic prohibited.",
    r"\bcasino\b": "NG: 'casino'. Topic prohibited.",
    r"\bslot\s*machine\b": "NG: 'slot machine'. Topic prohibited.",
    r"\bbet(?:ting)?\b": "NG: 'bet/betting'. Use 'challenge', 'contest'.",

    # Discrimination (English)
    r"\bhate\s*speech\b": "NG: 'hate speech'. Topic prohibited.",
    r"\bracis[tm]\b": "NG: Racial terms prohibited.",

    # Drugs (English)
    r"\bdrug(?:s)?\b": "NG: 'drugs'. Topic prohibited.",
    r"\bweed\b": "NG: 'weed'. Topic prohibited.",
    r"\bcocaine\b": "NG: 'cocaine'. Topic prohibited.",

    # Fraud/Exploit (English)
    r"\bscam\b": "NG: 'scam'. Avoid promoting deception.",
    r"\bhack(?:ing|ed)?\b": "NG: 'hack'. Avoid exploit promotion.",
    r"\bexploit\b": "NG: 'exploit'. Avoid exploit promotion.",

    # Self-harm (English)
    r"\bsuicid(?:e|al)\b": "NG: 'suicide/suicidal'. Topic prohibited.",
    r"\bself[- ]?harm\b": "NG: 'self-harm'. Topic prohibited.",

    # Violence (Japanese)
    r"殺す": "NG: '殺す'. Use '倒す', '排除する'.",
    r"死ぬ": "NG: '死ぬ'. Use 'やられる', '消える'.",
    r"殺害": "NG: '殺害'. Topic prohibited.",
    r"暴行": "NG: '暴行'. Topic prohibited.",

    # Bullying (Japanese)
    r"ハブる": "NG: 'ハブる'. Bullying promotion prohibited.",
    r"仲間外れ": "NG: '仲間外れ'. Use redemption narrative.",
    r"無視しろ": "NG: '無視しろ'. Bullying promotion prohibited.",

    # Discrimination (Japanese)
    r"障害者": "NG: '障害者' as insult. Discrimination prohibited.",
    r"ガイジ": "NG: 'ガイジ'. Slur prohibited.",
}

# === IP/TRADEMARK VIOLATIONS ===
TRADEMARK_PATTERNS = {
    r"[Oo]fficial\s*[Rr]oblox": "NG: 'Official Roblox' implies endorsement. Remove 'Official'.",
    r"Roblox\s*公式": "NG: 'Roblox公式' implies endorsement.",
    r"[Mm]inecraft": "WARNING: Minecraft brand reference. Ensure no IP infringement.",
    r"[Ff]ortnite": "WARNING: Fortnite brand reference. Ensure no IP infringement.",
    r"[Nn]intendo": "WARNING: Nintendo brand reference. High copyright risk.",
    r"[Dd]isney": "WARNING: Disney brand reference. High copyright risk.",
}

# === AGE-INAPPROPRIATE PATTERNS ===
AGE_RISK_PATTERNS = {
    r"[Ff]or\s*[Kk]ids": "WARNING: 'For Kids' label may trigger COPPA. This channel targets 13-24, NOT kids.",
    r"子供向け": "WARNING: '子供向け' label conflicts with 13-24 age target.",
    r"18\+|[Aa]dult[- ][Oo]nly|NSFW": "NG: Adult-only labels. Content must be suitable for 13+.",
}


def log_print(msg):
    print(msg)
    try:
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(msg + "\n")
    except Exception:
        pass


def validate_file(file_path):
    # Reset log
    try:
        with open(LOG_FILE, "w", encoding='utf-8') as f:
            f.write("")
    except Exception:
        pass

    log_print(f"\n--- [Roblox Safety Check]: {os.path.basename(file_path)} ---")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except FileNotFoundError:
        log_print("[ERROR]: File not found.")
        return False

    errors = []
    warnings = []

    for i, line in enumerate(lines):
        line_num = i + 1
        stripped = line.strip()
        if not stripped:
            continue

        # Skip comments and metadata
        if stripped.startswith('#') or stripped.startswith('<!--') or stripped.startswith('[BGM'):
            continue

        # 1. Banned Words Check
        for pattern, reason in BANNED_WORDS.items():
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                errors.append(f"Line {line_num}: {reason}\n   -> \"{stripped[:80]}\"")

        # 2. Trademark/IP Check
        for pattern, reason in TRADEMARK_PATTERNS.items():
            if re.search(pattern, line):
                if reason.startswith("WARNING"):
                    warnings.append(f"Line {line_num}: {reason}\n   -> \"{stripped[:80]}\"")
                else:
                    errors.append(f"Line {line_num}: {reason}\n   -> \"{stripped[:80]}\"")

        # 3. Age-Inappropriate Labels
        for pattern, reason in AGE_RISK_PATTERNS.items():
            if re.search(pattern, line):
                if reason.startswith("WARNING"):
                    warnings.append(f"Line {line_num}: {reason}\n   -> \"{stripped[:80]}\"")
                else:
                    errors.append(f"Line {line_num}: {reason}\n   -> \"{stripped[:80]}\"")

    # Output results
    if warnings:
        log_print(f"\n⚠️  Warnings ({len(warnings)}):")
        for w in warnings:
            log_print(f"  {w}")

    if errors:
        log_print(f"\n❌ Errors ({len(errors)}):")
        for e in errors:
            log_print(f"  {e}")
        log_print("\n[FAILED]: Fix errors before publishing.")
        return False

    log_print("\n✅ [SUCCESS]: No safety issues found.")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        log_print("Usage: python3 validate_roblox_safety.py <file_path>")
        sys.exit(1)

    success = validate_file(sys.argv[1])
    sys.exit(0 if success else 1)
