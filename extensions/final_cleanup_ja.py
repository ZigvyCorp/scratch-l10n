#!/usr/bin/env python3
"""
Final cleanup - translate all remaining simple English terms.
"""

import json
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

# Dictionary for exact matches (case-insensitive)
EXACT_TRANSLATIONS = {
    # Keep technical acronyms as-is
    "3D AR/VR": "3D AR/VR",
    "API": "API",
    "URL": "URL",
    "JSON": "JSON",
    "XML": "XML",
    "HTML": "HTML",
    "CSS": "CSS",
    "ID": "ID",
    "XYZ": "XYZ",

    # Simple menu items
    "Up-Down Flipped": "上下反転",
    "Left-Right Flipped": "左右反転",
    "mute": "ミュート",
    "unmute": "ミュート解除",
    "yes": "はい",
    "no": "いいえ",
    "vertical": "縦",
    "horizontal": "横",
    "Male": "男性",
    "Female": "女性",
    "Male2": "男性2",
    "Female2": "女性2",
    "Male3": "男性3",
    "Female3": "女性3",
    "Boy": "男の子",
    "Girl": "女の子",
    "Highest": "最高",
    "Lowest": "最低",
    "Both": "両方",
    "Plane": "平面",
    "None": "なし",
    "Auto": "自動",
    "Manual": "手動",
    "Random": "ランダム",
    "Loop": "ループ",
    "Once": "1回",
    "Repeat": "繰り返し",
    "Forever": "ずっと",
    "True": "真",
    "False": "偽",
    "On": "オン",
    "Off": "オフ",
    "Up": "上",
    "Down": "下",
    "Left": "左",
    "Right": "右",
    "Front": "前",
    "Back": "後ろ",
    "Top": "上",
    "Bottom": "下",
    "Center": "中央",
    "Middle": "中央",
    "Begin": "開始",
    "End": "終了",
    "Start": "開始",
    "Stop": "停止",
    "Pause": "一時停止",
    "Resume": "再開",
    "Play": "再生",
    "Record": "録音",
    "Reset": "リセット",
    "Clear": "クリア",
    "Delete": "削除",
    "Remove": "削除",
    "Add": "追加",
    "Insert": "挿入",
    "Update": "更新",
    "Save": "保存",
    "Load": "読み込み",
    "Open": "開く",
    "Close": "閉じる",
    "Connect": "接続",
    "Disconnect": "切断",
    "Online": "オンライン",
    "Offline": "オフライン",
    "Available": "利用可能",
    "Unavailable": "利用不可",
    "Enabled": "有効",
    "Disabled": "無効",
    "Active": "アクティブ",
    "Inactive": "非アクティブ",
    "Visible": "表示",
    "Hidden": "非表示",
    "Show": "表示",
    "Hide": "非表示",
    "Normal": "通常",
    "Bold": "太字",
    "Italic": "斜体",
    "Underline": "下線",
    "Single": "単一",
    "Multiple": "複数",
    "All": "すべて",
    "Any": "任意",
    "Some": "いくつか",
    "Other": "その他",
    "Default": "デフォルト",
    "Custom": "カスタム",
    "New": "新規",
    "Old": "古い",
    "First": "最初",
    "Last": "最後",
    "Next": "次",
    "Previous": "前",
    "Success": "成功",
    "Error": "エラー",
    "Warning": "警告",
    "Info": "情報",
    "Debug": "デバッグ",
    "Full": "フル",
    "Empty": "空",
    "Filled": "塗りつぶし",
    "Outline": "輪郭",
    "Solid": "ソリッド",
    "Dashed": "破線",
    "Dotted": "点線",
    "Thick": "太い",
    "Thin": "細い",
    "Large": "大",
    "Medium": "中",
    "Small": "小",
    "Wide": "広い",
    "Narrow": "狭い",
    "Fast": "速い",
    "Slow": "遅い",
    "High": "高",
    "Low": "低",
    "Maximum": "最大",
    "Minimum": "最小",
    "Positive": "正",
    "Negative": "負",
    "Zero": "ゼロ",
    "Infinity": "無限",
    "Circle": "円",
    "Rectangle": "四角形",
    "Square": "正方形",
    "Triangle": "三角形",
    "Polygon": "多角形",
    "Line": "線",
    "Point": "点",
    "Sphere": "球",
    "Cube": "立方体",
    "Cylinder": "円柱",
    "Cone": "円錐",
    "Static": "静的",
    "Dynamic": "動的",
    "Fixed": "固定",
    "Movable": "移動可能",
    "Solid": "ソリッド",
    "Liquid": "液体",
    "Gas": "気体",
    "Red": "赤",
    "Green": "緑",
    "Blue": "青",
    "Yellow": "黄",
    "Orange": "橙",
    "Purple": "紫",
    "Pink": "ピンク",
    "Brown": "茶",
    "Black": "黒",
    "White": "白",
    "Gray": "灰色",
    "Grey": "灰色",
    "Transparent": "透明",
    "Opaque": "不透明",
}

# Additional word-level translations
WORD_TRANSLATIONS = {
    "flip": "反転",
    "flipped": "反転",
    "flip": "反転",
    "rotate": "回転",
    "rotated": "回転",
    "rotation": "回転",
    "scale": "拡大縮小",
    "scaled": "拡大縮小",
    "scaling": "拡大縮小",
    "move": "移動",
    "moved": "移動",
    "moving": "移動",
    "transform": "変換",
    "transformed": "変換",
    "transformation": "変換",
    "translate": "移動",
    "translated": "移動",
    "translation": "移動",
    "xyz": "XYZ",
    "rgb": "RGB",
    "hsv": "HSV",
    "hex": "HEX",
}

def clean_translate(text):
    """Clean translation for simple terms."""
    if not text:
        return text

    # Check if it's an exact match
    text_stripped = text.strip()
    if text_stripped in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text_stripped]

    # Check case-insensitive
    for exact, translation in EXACT_TRANSLATIONS.items():
        if text_stripped.lower() == exact.lower():
            return translation

    # Apply word-level translations
    result = text
    for word, translation in WORD_TRANSLATIONS.items():
        # Word boundary replacement
        result = re.sub(r'\b' + re.escape(word) + r'\b', translation, result, flags=re.IGNORECASE)

    return result

def main():
    ja_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja.json'

    print("Loading Japanese extensions file...")
    ja_data = load_json(ja_file)

    print(f"Total entries: {len(ja_data)}")
    print("\nApplying final cleanup...")

    fixes_applied = 0

    for key, value in list(ja_data.items()):
        fixed = clean_translate(value)
        if fixed != value:
            ja_data[key] = fixed
            fixes_applied += 1

    print(f"\nFixes applied: {fixes_applied}")

    # Final analysis
    print("\nFinal analysis...")
    problematic_40 = 0
    problematic_50 = 0
    problematic_70 = 0

    for key, value in ja_data.items():
        clean = re.sub(r'\[[^\]]+\]', '', value)
        clean = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean)
        if clean:
            eng = len(re.findall(r'[a-zA-Z]', clean))
            jap = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean))
            total = eng + jap
            if total > 0:
                pct = eng / total
                if pct > 0.4:
                    problematic_40 += 1
                if pct > 0.5:
                    problematic_50 += 1
                if pct > 0.7:
                    problematic_70 += 1

    print(f"Entries with >40% English: {problematic_40}")
    print(f"Entries with >50% English: {problematic_50}")
    print(f"Entries with >70% English: {problematic_70}")

    # Save
    print(f"\nSaving fixed file: {ja_file}")
    save_json(ja_file, ja_data)

    print("\nDone!")

if __name__ == '__main__':
    main()
