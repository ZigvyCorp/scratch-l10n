#!/usr/bin/env python3
"""
Comprehensive fix for Japanese extensions translation file.
Provides complete manual translations for all problematic entries.
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

# Comprehensive manual translations for problematic entries
MANUAL_FIXES = {
    # Multiplayer extension
    "mp.createMultiplayerGame": "ゲームを作成 名前 [GAMENAME] パスワード [PASSWORD] 自分の名前 [DISPLAYNAME] 役割 [ROLE] サーバー [REGION] 定員 [PLAYERCOUNT] ワールド 幅 [WIDTH] 高さ [HEIGHT]",
    "mp.listMultiplayerGameUsers": "ゲーム [GAMENAME] のプレイヤー一覧 ホスト [HOSTUSERNAME] サーバー [REGION] テーブル [TABLE]",
    "mp.resetMultiplayerGame": "ゲームワールドをリセット",
    "mp.listMultiplayerGames": "マルチプレイヤーゲーム一覧 サーバー [REGION] テーブル [TABLE]",
    "mp.joinMultiplayerGame": "マルチプレイヤーゲームに参加 名前 [GAMENAME] ホスト [HOSTUSERNAME] サーバー [REGION] パスワード [PASSWORD] 自分の名前 [DISPLAYNAME] 役割 [ROLE]",
    "mp.addSpriteToGame": "このスプライトをゲームに追加 [MOTIONTYPE] [SHAPETYPE] 幅 [WIDTH] 高さ [HEIGHT]",
    "mp.removeSpriteFromGame": "このスプライトをゲームから削除",
    "mp.setSyncMovement": "同期的に速度を設定 x [XSPEED] y [YSPEED]",
    "mp_setSyncMovement2": "同期的に速度を設定 [SPEED] 向き [DIR]",
    "mp_setSyncDir": "同期的に向きを設定 [DIRECTION]",
    "mp_setSyncPosition": "同期的に位置を設定 x [XPOS] y [YPOS]",
    "mp.broadcastMessageToAll": "[BROADCASTMESSAGE] を送る パラメータ [PARAM] モード [TARGETTYPE]",
    "mp.spriteScope.allSprites": "すべてのスプライト",
    "mp.spriteScope.originalSprites": "オリジナルスプライト",
    "mp.stopType.stop": "停止",
    "mp.stopType.stopAndCollect": "停止して収集",
    "mp.stopType.continue": "続行",
    "mp.stopType.continueAndCollect": "続行して収集",
    "mp.stopType.selfDestruct": "自己破壊",
    "mp.motionType.static": "静的",
    "mp.motionType.dynamic": "動的",
    "mp.motionType.kinematic": "運動学的",
    "mp.shapeType.box": "四角形",
    "mp.shapeType.circle": "円",
    "mp.shapeType.polygon": "多角形",
    "mp.removeSprite": "スプライト [TARGETSPRITE] を削除",
    "mp.setPosition": "スプライト [TARGETSPRITE] の位置を x [XPOS] y [YPOS] にする",
    "mp.setXPosition": "スプライト [TARGETSPRITE] のx座標を [XPOS] にする",
    "mp.setYPosition": "スプライト [TARGETSPRITE] のy座標を [YPOS] にする",
    "mp.setDirection": "スプライト [TARGETSPRITE] の向きを [DIRECTION] にする",
    "mp.getX": "スプライト [TARGETSPRITE] のx座標",
    "mp.getY": "スプライト [TARGETSPRITE] のy座標",
    "mp.getDirection": "スプライト [TARGETSPRITE] の向き",
    "mp.getVelX": "スプライト [TARGETSPRITE] のx速度",
    "mp.getVelY": "スプライト [TARGETSPRITE] のy速度",
    "mp.getAngularVelocity": "スプライト [TARGETSPRITE] の角速度",
    "mp.setXVelocity": "スプライト [TARGETSPRITE] のx速度を [XVEL] にする",
    "mp.setYVelocity": "スプライト [TARGETSPRITE] のy速度を [YVEL] にする",
    "mp.setAngularVelocity": "スプライト [TARGETSPRITE] の角速度を [ANGULARVEL] にする",
    "mp.changeCostume": "スプライト [TARGETSPRITE] のコスチュームを [COSTUME] にする",
    "mp.setGhost": "スプライト [TARGETSPRITE] の透明度を [GHOST] にする",
    "mp.setRotationStyle": "スプライト [TARGETSPRITE] の回転方法を [ROTATESTYLE] にする",
    "mp.setSize": "スプライト [TARGETSPRITE] の大きさを [SIZE] にする",
    "mp.touchingObject": "スプライト [TARGETSPRITE] が [TOUCHINGOBJECTMENU] に触れた",
    "mp.getBroadcastedMessage": "受信したメッセージ",
    "mp.getBroadcastedParameter": "受信したパラメータ",
    "mp.myId": "自分のID",
    "mp.hostId": "ホストのID",
    "mp.getPlayerRole": "プレイヤー [PLAYER] の役割",
    "mp.getPlayerName": "プレイヤー [PLAYER] の名前",
    "mp.host": "ホスト",
    "mp.receivedMessage": "メッセージを受信したとき",
    "mp.myConnectionOpened": "接続が開始されたとき",
    "mp.myConnectionClosed": "接続が閉じたとき",
    "mp.playerJoined": "プレイヤーが参加したとき",
    "mp.playerLeft": "プレイヤーが退出したとき",
    "mp.spriteCreated": "スプライト [SPRITE] が作成されたとき",
    "mp.spriteRemoved": "スプライト [SPRITE] が削除されたとき",

    # 3D AR/VR - keep as technical term
    "d3arvr.categoryName": "3D AR/VR",

    # Database extension
    "db.createDatabase": "データベース [DATABASE] を作成",
    "db.dropDatabase": "データベース [DATABASE] を削除",
    "db.createTable": "テーブル [TABLE] を作成 データベース [DATABASE] カラム [COLUMNS]",
    "db.dropTable": "テーブル [TABLE] を削除 データベース [DATABASE]",
    "db.insert": "挿入 データベース [DATABASE] テーブル [TABLE] 値 [VALUES]",
    "db.select": "選択 データベース [DATABASE] テーブル [TABLE] 条件 [WHERE] 順序 [ORDERBY]",
    "db.update": "更新 データベース [DATABASE] テーブル [TABLE] 設定 [SET] 条件 [WHERE]",
    "db.delete": "削除 データベース [DATABASE] テーブル [TABLE] 条件 [WHERE]",
    "db.execute": "実行 SQL [SQL] データベース [DATABASE]",
    "db.getResult": "結果を取得",
    "db.getRowCount": "行数を取得",

    # Chart extension
    "chart.createChart": "グラフを作成 タイプ [TYPE] データ [DATA] ラベル [LABELS]",
    "chart.updateChart": "グラフを更新 データ [DATA]",
    "chart.showChart": "グラフを表示",
    "chart.hideChart": "グラフを非表示",
    "chart.clearChart": "グラフをクリア",
    "chart.setChartTitle": "グラフのタイトルを [TITLE] にする",
    "chart.setAxisLabel": "軸 [AXIS] のラベルを [LABEL] にする",
    "chart.chartType.line": "折れ線",
    "chart.chartType.bar": "棒",
    "chart.chartType.pie": "円",
    "chart.chartType.scatter": "散布図",

    # Widget extension
    "widget.createWidget": "ウィジェット [WIDGET] を作成",
    "widget.deleteWidget": "ウィジェット [WIDGET] を削除",
    "widget.showWidget": "ウィジェット [WIDGET] を表示",
    "widget.hideWidget": "ウィジェット [WIDGET] を非表示",
    "widget.setWidgetProperty": "ウィジェット [WIDGET] のプロパティ [PROPERTY] を [VALUE] にする",
    "widget.getWidgetProperty": "ウィジェット [WIDGET] のプロパティ [PROPERTY]",
    "widget.widgetClicked": "ウィジェット [WIDGET] がクリックされたとき",

    # Common English terms that appear throughout
    "Continue": "続行",
    "Original": "オリジナル",
    "All": "すべて",
    "Self-Destruct": "自己破壊",
    "Stop": "停止",
    "Collect": "収集",
    "game": "ゲーム",
    "player": "プレイヤー",
    "players": "プレイヤー",
    "sprite": "スプライト",
    "sprites": "スプライト",
    "world": "ワールド",
    "server": "サーバー",
    "host": "ホスト",
    "password": "パスワード",
    "named": "名前",
    "name": "名前",
    "table": "テーブル",
    "multiplayer": "マルチプレイヤー",
    "database": "データベース",
    "chart": "グラフ",
    "widget": "ウィジェット",
}

def fix_mixed_text(text):
    """Fix mixed English/Japanese text by translating common English terms."""
    if not text:
        return text

    # Skip if already all Japanese (with variables/numbers/punctuation)
    clean_text = re.sub(r'\[[^\]]+\]', '', text)  # Remove variables
    clean_text = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_text)  # Remove numbers/punctuation

    if not clean_text:
        return text

    # Count English vs Japanese
    english_chars = len(re.findall(r'[a-zA-Z]', clean_text))
    japanese_chars = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_text))

    # If less than 30% English, probably OK
    total = english_chars + japanese_chars
    if total > 0 and english_chars / total < 0.3:
        return text

    # Apply translations for common terms
    translations = {
        # Technical terms
        r'\bgame\b': 'ゲーム',
        r'\bplayers?\b': 'プレイヤー',
        r'\bsprites?\b': 'スプライト',
        r'\bworld\b': 'ワールド',
        r'\bserver\b': 'サーバー',
        r'\bhost\b': 'ホスト',
        r'\bpassword\b': 'パスワード',
        r'\bnamed\b': '名前',
        r'\bmy name\b': '自分の名前',
        r'\bname\b': '名前',
        r'\btable\b': 'テーブル',
        r'\bmultiplayer\b': 'マルチプレイヤー',
        r'\bdatabase\b': 'データベース',
        r'\bchart\b': 'グラフ',
        r'\bwidget\b': 'ウィジェット',
        r'\bcreate\b': '作成',
        r'\bdelete\b': '削除',
        r'\bremove\b': '削除',
        r'\badd\b': '追加',
        r'\bupdate\b': '更新',
        r'\bset\b': '設定',
        r'\bget\b': '取得',
        r'\bshow\b': '表示',
        r'\bhide\b': '非表示',
        r'\bclear\b': 'クリア',
        r'\blist\b': '一覧',
        r'\bjoin\b': '参加',
        r'\breset\b': 'リセット',
        r'\bbroadcast\b': '送る',
        r'\bfrom\b': 'から',
        r'\bto\b': 'へ',
        r'\bin\b': 'の',
        r'\bby\b': 'による',
        r'\bwith\b': 'で',
        r'\bas\b': 'として',
        r'\bthis\b': 'この',
        r'\band\b': 'と',
        r'\bor\b': 'または',
        r'\bAll\b': 'すべて',
        r'\bOriginal\b': 'オリジナル',
        r'\bStop\b': '停止',
        r'\bContinue\b': '続行',
        r'\bCollect\b': '収集',
        r'\bSelf-Destruct\b': '自己破壊',
        r'\bstatic\b': '静的',
        r'\bdynamic\b': '動的',
        r'\bkinematic\b': '運動学的',
        r'\bbox\b': '四角形',
        r'\bcircle\b': '円',
        r'\bpolygon\b': '多角形',
        r'\bposition\b': '位置',
        r'\bdirection\b': '向き',
        r'\bspeed\b': '速度',
        r'\bvelocity\b': '速度',
        r'\bwidth\b': '幅',
        r'\bheight\b': '高さ',
        r'\bsize\b': '大きさ',
        r'\bcostume\b': 'コスチューム',
        r'\bghost\b': '透明度',
        r'\brotation\b': '回転',
        r'\bstyle\b': '方法',
        r'\btouching\b': '触れた',
        r'\bmessage\b': 'メッセージ',
        r'\bparameter\b': 'パラメータ',
        r'\bmode\b': 'モード',
        r'\brole\b': '役割',
        r'\bcapacity\b': '定員',
        r'\bregion\b': '地域',
        r'\bhosted\b': 'ホスト',
        r'\bsynchronously\b': '同期的に',
        r'\breceived\b': '受信した',
        r'\bopened\b': '開始された',
        r'\bclosed\b': '閉じた',
        r'\bjoined\b': '参加した',
        r'\bleft\b': '退出した',
        r'\bcreated\b': '作成された',
        r'\bremoved\b': '削除された',
        r'\bwhen\b': 'とき',
        r'\bof\b': 'の',
    }

    result = text
    for pattern, replacement in translations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    return result

def main():
    ja_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja.json'
    en_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/en.json'

    print("Loading files...")
    ja_data = load_json(ja_file)
    en_data = load_json(en_file)

    print(f"Total entries: {len(ja_data)}")

    fixes_applied = 0
    issues_found = []

    # First apply manual fixes
    for key, fixed_value in MANUAL_FIXES.items():
        if key in ja_data:
            original = ja_data[key]
            if original != fixed_value:
                ja_data[key] = fixed_value
                fixes_applied += 1
                issues_found.append({
                    'key': key,
                    'original': original,
                    'fixed': fixed_value,
                    'type': 'manual_fix'
                })

    # Then apply automatic fixes for remaining entries
    for key, value in list(ja_data.items()):
        if key in MANUAL_FIXES:
            continue  # Already fixed

        # Check if needs fixing
        clean_text = re.sub(r'\[[^\]]+\]', '', value)
        clean_text = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_text)

        if not clean_text:
            continue

        english_chars = len(re.findall(r'[a-zA-Z]', clean_text))
        japanese_chars = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_text))
        total = english_chars + japanese_chars

        if total > 0 and english_chars / total > 0.3:
            fixed = fix_mixed_text(value)
            if fixed != value:
                ja_data[key] = fixed
                fixes_applied += 1
                issues_found.append({
                    'key': key,
                    'original': value,
                    'fixed': fixed,
                    'type': 'auto_fix'
                })

    print(f"\nFixes applied: {fixes_applied}")
    print(f"  - Manual fixes: {sum(1 for i in issues_found if i['type'] == 'manual_fix')}")
    print(f"  - Automatic fixes: {sum(1 for i in issues_found if i['type'] == 'auto_fix')}")

    # Show some examples
    manual_fixes = [i for i in issues_found if i['type'] == 'manual_fix']
    auto_fixes = [i for i in issues_found if i['type'] == 'auto_fix']

    if manual_fixes:
        print(f"\nManual fix examples (first 10):")
        for issue in manual_fixes[:10]:
            print(f"  {issue['key']}:")
            print(f"    Original: {issue['original']}")
            print(f"    Fixed: {issue['fixed']}")

    if auto_fixes:
        print(f"\nAutomatic fix examples (first 10):")
        for issue in auto_fixes[:10]:
            print(f"  {issue['key']}:")
            print(f"    Original: {issue['original']}")
            print(f"    Fixed: {issue['fixed']}")

    # Save the fixed file
    backup_file = ja_file + '.backup'
    print(f"\nCreating backup: {backup_file}")
    save_json(backup_file, load_json(ja_file))

    print(f"Saving fixed file: {ja_file}")
    save_json(ja_file, ja_data)

    # Save detailed report
    report_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja_comprehensive_fix_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(issues_found, f, ensure_ascii=False, indent=2)

    print(f"Detailed report saved: {report_file}")
    print("\nDone!")

if __name__ == '__main__':
    main()
