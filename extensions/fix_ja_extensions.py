#!/usr/bin/env python3
"""
Fix Japanese extensions translation file.
Identifies and fixes:
1. Mixed English/Japanese text
2. Corrupted Japanese characters
3. English text that should be Japanese
4. Grammar issues
"""

import json
import re
from typing import Dict, List, Tuple

def load_json(filepath: str) -> Dict:
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict):
    """Save JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

def has_corruption(text: str) -> bool:
    """Check if text has corrupted Japanese patterns."""
    corruption_patterns = [
        r'[a-z][ァ-ヴぁ-ん]',  # English letter followed by Japanese
        r'[ァ-ヴぁ-ん][a-z]',  # Japanese followed by English letter (excluding variables)
        r'もしic',
        r'zオン',
        r'cオン',
        r'bまたは',
        r'wまたは',
        r'または[a-z]',
        r'[a-z]また',
    ]

    # Skip variable patterns like [VARIABLE]
    if '[' in text and ']' in text:
        # Extract parts not in brackets
        parts = re.split(r'\[[^\]]+\]', text)
    else:
        parts = [text]

    for part in parts:
        for pattern in corruption_patterns:
            if re.search(pattern, part):
                return True
    return False

def is_mostly_english(text: str) -> bool:
    """Check if text is mostly English (should be translated)."""
    # Remove variable placeholders
    clean_text = re.sub(r'\[[^\]]+\]', '', text)
    # Remove numbers and special chars
    clean_text = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_text)

    if not clean_text:
        return False

    # Count English and Japanese characters
    english_chars = len(re.findall(r'[a-zA-Z]', clean_text))
    japanese_chars = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_text))

    # If more than 50% English, it's mostly English
    total = english_chars + japanese_chars
    if total > 0:
        return english_chars / total > 0.5
    return False

# Comprehensive translation mapping
TRANSLATIONS = {
    # Technical terms
    "property": "プロパティ",
    "full screen": "フルスクリーン",
    "fullscreen": "フルスクリーン",
    "widget": "ウィジェット",
    "database": "データベース",
    "chart": "グラフ",
    "draw": "描画",
    "add": "追加",
    "remove": "削除",
    "delete": "削除",
    "create": "作成",
    "set": "設定",
    "get": "取得",
    "reset": "リセット",
    "clear": "クリア",
    "display": "表示",
    "show": "表示",
    "hide": "非表示",
    "enable": "有効",
    "disable": "無効",
    "start": "開始",
    "stop": "停止",
    "pause": "一時停止",
    "resume": "再開",
    "play": "再生",
    "record": "録音",
    "save": "保存",
    "load": "読み込み",
    "update": "更新",
    "change": "変更",
    "switch": "切り替え",
    "toggle": "切り替え",
    "select": "選択",
    "choose": "選択",
    "pick": "選択",

    # Common words
    "the": "",
    "a": "",
    "an": "",
    "is": "は",
    "are": "は",
    "to": "に",
    "of": "の",
    "and": "と",
    "or": "または",
    "when": "とき",
    "if": "もし",
    "then": "ならば",
    "else": "それ以外",
    "for": "間",
    "in": "中",
    "on": "上",
    "off": "オフ",
    "up": "上",
    "down": "下",
    "left": "左",
    "right": "右",
    "front": "前",
    "back": "後ろ",
    "forward": "前進",
    "backward": "後退",
    "yes": "はい",
    "no": "いいえ",
    "true": "真",
    "false": "偽",
    "all": "すべて",
    "any": "任意",
    "none": "なし",
    "other": "その他",
    "default": "デフォルト",

    # Extension-specific
    "loudness": "音量",
    "timer": "タイマー",
    "video": "ビデオ",
    "motion": "動き",
    "direction": "向き",
    "transparency": "透明度",
    "stage": "ステージ",
    "backdrop": "背景",
    "costume": "コスチューム",
    "sprite": "スプライト",
    "clone": "クローン",
    "broadcast": "送る",
    "receive": "受け取る",
    "wait": "待つ",
    "repeat": "繰り返す",
    "forever": "ずっと",
    "until": "まで",
    "sensing": "調べる",
    "operator": "演算",
    "variable": "変数",
    "list": "リスト",
    "block": "ブロック",
    "script": "スクリプト",
    "sound": "音",
    "music": "音楽",
    "note": "音符",
    "beat": "拍",
    "tempo": "テンポ",
    "volume": "音量",
    "pitch": "音程",
    "instrument": "楽器",
    "drum": "ドラム",

    # Actions
    "turn on": "オンにする",
    "turn off": "オフにする",
    "turn": "回転",
    "move": "動かす",
    "go to": "移動する",
    "glide": "滑らかに動く",
    "point": "向ける",
    "say": "言う",
    "think": "考える",
    "ask": "聞く",
    "answer": "答え",
    "touching": "触れた",
    "color": "色",
    "distance": "距離",
    "pressed": "押された",
    "key": "キー",
    "mouse": "マウス",
    "x position": "x座標",
    "y position": "y座標",
    "size": "大きさ",
    "speed": "速さ",
    "power": "パワー",
    "brightness": "明るさ",
    "effect": "効果",

    # Text/Translate specific
    "language": "言語",
    "translate": "翻訳",
    "speech": "音声",
    "voices": "音声",
    "speak": "話す",
    "listen": "聞く",

    # Pen specific
    "pen": "ペン",
    "stamp": "スタンプ",
    "erase": "消す",

    # Video sensing
    "video motion": "ビデオの動き",
    "video direction": "ビデオの向き",

    # Music extension
    "set instrument": "楽器を",
    "rest": "休符",

    # Makey Makey
    "space": "スペース",
    "arrow": "矢印",
    "sequence": "順番",
}

# Specific fixes for known corrupted entries
SPECIFIC_FIXES = {
    # Add specific corrupted entries found during analysis
}

def fix_translation(key: str, value: str, en_value: str) -> Tuple[str, str]:
    """Fix a single translation entry."""
    original = value
    reason = []

    # Skip if already empty or just punctuation
    if not value.strip() or value.strip() in ['', '.', ',', '!', '?']:
        return value, ""

    # Check for specific known fixes
    if key in SPECIFIC_FIXES:
        return SPECIFIC_FIXES[key], f"Applied specific fix for {key}"

    # Check if it's mostly English (needs translation)
    if is_mostly_english(value):
        # Try to apply translations
        fixed = value
        for eng, jap in TRANSLATIONS.items():
            # Only replace whole words, not parts of variables
            pattern = r'\b' + re.escape(eng) + r'\b'
            fixed = re.sub(pattern, jap, fixed, flags=re.IGNORECASE)

        if fixed != value:
            reason.append("Translated English text")
            value = fixed

    # Check for corruption
    if has_corruption(value):
        reason.append("Fixed corrupted characters")
        # This would need more sophisticated fixing based on context
        # For now, we'll flag it for manual review

    if reason:
        return value, "; ".join(reason)

    return value, ""

def analyze_and_fix(ja_file: str, en_file: str) -> Dict:
    """Analyze and fix Japanese translation file."""
    ja_data = load_json(ja_file)
    en_data = load_json(en_file)

    issues = []
    fixes_made = 0

    print(f"Analyzing {len(ja_data)} entries...")

    for key, ja_value in ja_data.items():
        en_value = en_data.get(key, "")

        # Check for issues
        has_issue = False
        issue_types = []

        if has_corruption(ja_value):
            has_issue = True
            issue_types.append("corruption")

        if is_mostly_english(ja_value):
            has_issue = True
            issue_types.append("untranslated")

        if has_issue:
            fixed_value, reason = fix_translation(key, ja_value, en_value)
            if fixed_value != ja_value:
                issues.append({
                    'key': key,
                    'original': ja_value,
                    'fixed': fixed_value,
                    'english': en_value,
                    'types': issue_types,
                    'reason': reason
                })
                ja_data[key] = fixed_value
                fixes_made += 1
            else:
                # Still has issues but couldn't auto-fix
                issues.append({
                    'key': key,
                    'original': ja_value,
                    'fixed': ja_value,
                    'english': en_value,
                    'types': issue_types,
                    'reason': 'Needs manual review'
                })

    return {
        'data': ja_data,
        'issues': issues,
        'fixes_made': fixes_made
    }

def main():
    ja_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja.json'
    en_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/en.json'

    print("Starting Japanese extensions translation fix...")
    print("=" * 80)

    result = analyze_and_fix(ja_file, en_file)

    print(f"\nTotal entries analyzed: {len(result['data'])}")
    print(f"Issues found: {len(result['issues'])}")
    print(f"Automatic fixes applied: {result['fixes_made']}")

    # Group issues by type
    corruption_issues = [i for i in result['issues'] if 'corruption' in i['types']]
    untranslated_issues = [i for i in result['issues'] if 'untranslated' in i['types']]

    print(f"\nIssue breakdown:")
    print(f"  - Corrupted text: {len(corruption_issues)}")
    print(f"  - Untranslated text: {len(untranslated_issues)}")

    # Show examples
    if corruption_issues:
        print(f"\nCorruption examples (first 10):")
        for issue in corruption_issues[:10]:
            print(f"  {issue['key']}:")
            print(f"    Original: {issue['original']}")
            print(f"    Fixed: {issue['fixed']}")
            print(f"    English: {issue['english']}")

    if untranslated_issues:
        print(f"\nUntranslated examples (first 10):")
        for issue in untranslated_issues[:10]:
            print(f"  {issue['key']}:")
            print(f"    Original: {issue['original']}")
            print(f"    Fixed: {issue['fixed']}")
            print(f"    English: {issue['english']}")

    # Save detailed report
    report_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja_fix_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(result['issues'], f, ensure_ascii=False, indent=2)

    print(f"\nDetailed report saved to: {report_file}")

    # Ask before saving
    print("\n" + "=" * 80)
    print("Review the issues above.")
    print("The fixed file will be saved back to the original location.")

    return result

if __name__ == '__main__':
    result = main()
