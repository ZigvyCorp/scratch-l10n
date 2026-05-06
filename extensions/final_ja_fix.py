#!/usr/bin/env python3
"""
Final comprehensive fix for Japanese extensions translation.
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

# Massive comprehensive translation dictionary
COMPLETE_FIXES = {
    # Keep technical acronyms
    "d3arvr.categoryName": "3D AR/VR",

    # Multiplayer extension
    "mp.stopType.rebound": "跳ね返る",
    "mp.stopType.reboundAndDelete": "跳ね返って破壊",
    "mp.stopType.selfDestructAndCollect": "自己破壊して収集",
    "mp.broadcastTouchMessage": "[SPRITE] に触れたとき クローンID接頭辞 [CLONEID] 自分は [STOPTYPE] して [BROADCASTMESSAGE] を送る パラメータ [PARAM]",
    "mp.isConnectedToGame": "ゲームに接続している",
    "mp.whenAddedToGame": "ゲームに追加されたとき",
    "mp.leaveMultiplayerGame": "マルチプレイヤーゲームワールド [WORLDNAME] から退出",
    "mp.setSyncCostume": "同期的にコスチュームを [COSTUME] にする",

    # Entity types
    "playerentity": "プレイヤー",
    "obstacleentity": "障害物",
    "collectableentity": "収集可能物",
    "circleshape": "円",
    "rectangleshape": "四角形",
    "capsuleshape": "カプセル",
    "convexpolygonshape": "凸包",
    "fixedbody": "固定",
    "kinematicbody": "移動可能",
    "objecttype": "オブジェクト",
    "sensortype": "センサー",
    "Edge": "エッジ",

    # Physics extension
    "physics.enablePhysics": "2D物理ワールドを初期化 重力 x [X] y [Y]",
    "physics.applyForceImpulse": "力の衝撃を適用 x [XFORCE] y [YFORCE]",
    "physics.applyTorqueImpulse": "トルク衝撃を適用 [TORQUE]",
    "physics.turnoncollisiondetection": "地面検出をオンにする 距離 [DISTANCE] デバッグ [DEBUG]",
    "physics_getMass": "質量",
    "physics.getGroundSlope": "地面の傾き",
    "physics.disablePhysics": "物理演算を無効にする",
    "physics.setGravity": "重力を設定 x [X] y [Y]",
    "physics.applyForce": "力を適用 x [XFORCE] y [YFORCE]",
    "physics.applyTorque": "トルクを適用 [TORQUE]",
    "physics.setMass": "質量を [MASS] にする",
    "physics.setDensity": "密度を [DENSITY] にする",
    "physics.setFriction": "摩擦を [FRICTION] にする",
    "physics.setRestitution": "反発を [RESTITUTION] にする",
    "physics.setLinearDamping": "線形減衰を [DAMPING] にする",
    "physics.setAngularDamping": "角減衰を [DAMPING] にする",
    "physics.enableRotation": "回転を有効にする",
    "physics.disableRotation": "回転を無効にする",
    "physics.whenCollision": "[SPRITE] と衝突したとき",
    "physics.isTouchingGround": "地面に触れている",
    "physics.getVelocityX": "x速度",
    "physics.getVelocityY": "y速度",

    # P2P / Cloud extension
    "p2p.categoryName": "クラウド",
    "p2p.sendPhoneSMSWarning": "電話番号は数字のみ含めることができます",
    "p2p.formatContent.normal": "通常",
    "p2p.formatContent.bold": "太字",
    "p2p.formatContent.italic": "斜体",
    "p2p.formatContent.boldItalic": "太字斜体",
    "p2p.sendMessage": "[RECEIVER] にメッセージ [MESSAGE] を送る",
    "p2p.receiveMessage": "メッセージを受信したとき",
    "p2p.getLastMessage": "最後のメッセージ",
    "p2p.getSender": "送信者",
    "p2p.setUsername": "ユーザー名を [USERNAME] にする",
    "p2p.getUsername": "ユーザー名",
    "p2p.connect": "接続する",
    "p2p.disconnect": "切断する",
    "p2p.isConnected": "接続している",

    # Widget extension
    "widget.actionVideo": "[名前] のビデオを [ACTION]",
    "widget.currentVideoTime": "[名前] の現在のビデオ時間",
    "widget.menuItem.single": "単一",
    "widget.menuItem.multiple": "複数",
    "widget.menuItem.scroll": "スクロール",
    "widget.menuItem.noScroll": "スクロールなし",
    "widget.menuItem.input": "入力",
    "widget.menuItem.readOnly": "読み取り専用",
    "widget.menuItem.textArea": "テキストエリア",
    "widget.menuItem.checkBox": "チェックボックス",
    "widget.menuItem.radioButton": "ラジオボタン",
    "widget.menuItem.dropDown": "ドロップダウン",
    "widget.menuItem.button": "ボタン",
    "widget.menuItem.slider": "スライダー",
    "widget.menuItem.image": "画像",
    "widget.menuItem.video": "ビデオ",
    "widget.menuItem.canvas": "キャンバス",
    "widget.menuItem.label": "ラベル",
    "widget.menuItem.container": "コンテナ",

    # More common patterns
    "Connected": "接続済み",
    "Disconnected": "切断済み",
    "Online": "オンライン",
    "Offline": "オフライン",
    "Available": "利用可能",
    "Unavailable": "利用不可",
    "Enabled": "有効",
    "Disabled": "無効",
    "Active": "アクティブ",
    "Inactive": "非アクティブ",
    "Success": "成功",
    "Failed": "失敗",
    "Error": "エラー",
    "Warning": "警告",
    "Info": "情報",
    "Debug": "デバッグ",
}

def comprehensive_translate(text):
    """Comprehensive translation function."""
    if not text:
        return text

    # Comprehensive word replacements (order matters!)
    replacements = [
        # Prepositions and conjunctions (specific phrases first)
        (r'\bwhen\s+', 'とき'),
        (r'\bwhen added to\b', '追加されたとき'),
        (r'\bwhen touching\b', '触れたとき'),
        (r'\bwhen connected\b', '接続されたとき'),
        (r'\bwhen disconnected\b', '切断されたとき'),
        (r'\bwhen receiving\b', '受信したとき'),
        (r'\badded to\b', '追加された'),
        (r'\bconnected to\b', '接続している'),
        (r'\btouching\b', '触れた'),

        # Actions and verbs
        (r'\binitialize\b', '初期化する'),
        (r'\bapply\b', '適用する'),
        (r'\bturn on\b', 'オンにする'),
        (r'\bturn off\b', 'オフにする'),
        (r'\benable\b', '有効にする'),
        (r'\bdisable\b', '無効にする'),
        (r'\bcreate\b', '作成する'),
        (r'\bdelete\b', '削除する'),
        (r'\bremove\b', '削除する'),
        (r'\badd\b', '追加する'),
        (r'\bupdate\b', '更新する'),
        (r'\bset\b', '設定する'),
        (r'\bget\b', '取得する'),
        (r'\bshow\b', '表示する'),
        (r'\bhide\b', '非表示にする'),
        (r'\bclear\b', 'クリアする'),
        (r'\blist\b', '一覧'),
        (r'\bjoin\b', '参加する'),
        (r'\bleave\b', '退出する'),
        (r'\breset\b', 'リセットする'),
        (r'\bbroadcast\b', '送る'),
        (r'\breceive\b', '受信する'),
        (r'\bsend\b', '送る'),
        (r'\bplay\b', '再生する'),
        (r'\bstop\b', '停止する'),
        (r'\bpause\b', '一時停止する'),
        (r'\bresume\b', '再開する'),
        (r'\bstart\b', '開始する'),
        (r'\bend\b', '終了する'),
        (r'\bsave\b', '保存する'),
        (r'\bload\b', '読み込む'),
        (r'\bopen\b', '開く'),
        (r'\bclose\b', '閉じる'),
        (r'\bconnect\b', '接続する'),
        (r'\bdisconnect\b', '切断する'),
        (r'\bsynchronously\b', '同期的に'),

        # Technical terms
        (r'\bmultiplayer\b', 'マルチプレイヤー'),
        (r'\bphysics\b', '物理'),
        (r'\bdatabase\b', 'データベース'),
        (r'\bcloud\b', 'クラウド'),
        (r'\bwidget\b', 'ウィジェット'),
        (r'\bchart\b', 'グラフ'),
        (r'\bgame\b', 'ゲーム'),
        (r'\bplayer\b', 'プレイヤー'),
        (r'\bsprite\b', 'スプライト'),
        (r'\bworld\b', 'ワールド'),
        (r'\bserver\b', 'サーバー'),
        (r'\bhost\b', 'ホスト'),
        (r'\bpassword\b', 'パスワード'),
        (r'\bmy name\b', '自分の名前'),
        (r'\bnamed\b', '名前',),
        (r'\bname\b', '名前'),
        (r'\btable\b', 'テーブル'),
        (r'\bobstacle\b', '障害物'),
        (r'\bcollectable\b', '収集可能物'),
        (r'\bobject\b', 'オブジェクト'),
        (r'\bsensor\b', 'センサー'),
        (r'\bedge\b', 'エッジ'),

        # Properties and attributes
        (r'\bposition\b', '位置'),
        (r'\bdirection\b', '向き'),
        (r'\bspeed\b', '速度'),
        (r'\bvelocity\b', '速度'),
        (r'\bwidth\b', '幅'),
        (r'\bheight\b', '高さ'),
        (r'\bsize\b', '大きさ'),
        (r'\bcostume\b', 'コスチューム'),
        (r'\bghost\b', '透明度'),
        (r'\brotation\b', '回転'),
        (r'\bstyle\b', '方法'),
        (r'\bmessage\b', 'メッセージ'),
        (r'\bparameter\b', 'パラメータ'),
        (r'\bmode\b', 'モード'),
        (r'\brole\b', '役割'),
        (r'\bcapacity\b', '定員'),
        (r'\bregion\b', '地域'),
        (r'\bgravity\b', '重力'),
        (r'\bforce\b', '力'),
        (r'\btorque\b', 'トルク'),
        (r'\bimpulse\b', '衝撃'),
        (r'\bmass\b', '質量'),
        (r'\bdensity\b', '密度'),
        (r'\bfriction\b', '摩擦'),
        (r'\brestitution\b', '反発'),
        (r'\bdamping\b', '減衰'),
        (r'\blinear\b', '線形'),
        (r'\bangular\b', '角'),
        (r'\bcollision\b', '衝突'),
        (r'\bground\b', '地面'),
        (r'\bslope\b', '傾き'),
        (r'\bdetection\b', '検出'),
        (r'\bdebug\b', 'デバッグ'),
        (r'\bdistance\b', '距離'),
        (r'\bwithin\b', '以内'),
        (r'\bprefix\b', '接頭辞'),
        (r'\bclone\b', 'クローン'),
        (r'\bcurrent\b', '現在の'),
        (r'\btime\b', '時間'),
        (r'\bvideo\b', 'ビデオ'),
        (r'\bimage\b', '画像'),
        (r'\bcanvas\b', 'キャンバス'),
        (r'\blabel\b', 'ラベル'),
        (r'\bcontainer\b', 'コンテナ'),
        (r'\bbutton\b', 'ボタン'),
        (r'\bslider\b', 'スライダー',),
        (r'\binput\b', '入力'),
        (r'\bread only\b', '読み取り専用'),
        (r'\btext area\b', 'テキストエリア'),
        (r'\bcheck box\b', 'チェックボックス'),
        (r'\bradio button\b', 'ラジオボタン'),
        (r'\bdrop down\b', 'ドロップダウン'),
        (r'\bscroll\b', 'スクロール'),
        (r'\bno scroll\b', 'スクロールなし'),
        (r'\bsingle\b', '単一'),
        (r'\bmultiple\b', '複数'),
        (r'\bnormal\b', '通常'),
        (r'\bbold\b', '太字'),
        (r'\bitalic\b', '斜体'),
        (r'\bbold-italic\b', '太字斜体'),

        # Shapes
        (r'\bcircle\b', '円'),
        (r'\brectangle\b', '四角形'),
        (r'\bbox\b', '四角形'),
        (r'\bpolygon\b', '多角形'),
        (r'\bcapsule\b', 'カプセル'),
        (r'\bconvex hull\b', '凸包'),

        # Types and states
        (r'\bstatic\b', '静的'),
        (r'\bdynamic\b', '動的'),
        (r'\bkinematic\b', '運動学的'),
        (r'\bfixed\b', '固定'),
        (r'\bmovable\b', '移動可能'),
        (r'\bhosted\b', 'ホスト'),
        (r'\breceived\b', '受信した'),
        (r'\bopened\b', '開始された'),
        (r'\bclosed\b', '閉じた'),
        (r'\bjoined\b', '参加した'),
        (r'\bleft\b', '退出した'),
        (r'\bcreated\b', '作成された'),
        (r'\bremoved\b', '削除された'),

        # Prepositions and particles
        (r'\bfrom\b', 'から'),
        (r'\bto\b', 'へ'),
        (r'\bin\b', 'の'),
        (r'\bby\b', 'による'),
        (r'\bwith\b', 'で'),
        (r'\bas\b', 'として'),
        (r'\bfor\b', '用'),
        (r'\bat\b', 'で'),
        (r'\bof\b', 'の'),
        (r'\band\b', 'と'),
        (r'\bor\b', 'または'),

        # Common words
        (r'\bthis\b', 'この'),
        (r'\bthat\b', 'その'),
        (r'\bmy\b', '自分の'),
        (r'\ball\b', 'すべて'),
        (r'\bany\b', '任意'),
        (r'\bnone\b', 'なし'),
        (r'\bother\b', 'その他'),
        (r'\boriginal\b', 'オリジナル'),
        (r'\bdefault\b', 'デフォルト'),
        (r'\bcollect\b', '収集'),
        (r'\bdestroy\b', '破壊'),
        (r'\brebound\b', '跳ね返る'),
        (r'\bself-destruct\b', '自己破壊'),
        (r'\bcontinue\b', '続行'),
        (r'\bstop\b', '停止'),
        (r'\bcan only include\b', 'のみ含めることができます'),
        (r'\bdigits\b', '数字'),
        (r'\bphone number\b', '電話番号'),
        (r'\buser\s*name\b', 'ユーザー名'),
        (r'\bsender\b', '送信者'),
        (r'\breceiver\b', '受信者'),
        (r'\blast\b', '最後の'),
        (r'\bconnected\b', '接続している'),
        (r'\bis\b', 'は'),
        (r'\bare\b', 'は'),
        (r'\bI will\b', '自分は'),
        (r'\bwill\b', 'する'),
    ]

    result = text
    for pattern, replacement in replacements:
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

    # Apply complete fixes first
    for key, fixed_value in COMPLETE_FIXES.items():
        if key in ja_data:
            original = ja_data[key]
            if original != fixed_value:
                ja_data[key] = fixed_value
                fixes_applied += 1
                issues_found.append({
                    'key': key,
                    'original': original,
                    'fixed': fixed_value,
                    'type': 'complete_fix'
                })

    # Apply comprehensive translation to remaining entries
    for key, value in list(ja_data.items()):
        if key in COMPLETE_FIXES:
            continue

        # Check if needs translation
        clean_text = re.sub(r'\[[^\]]+\]', '', value)
        clean_text = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_text)

        if not clean_text:
            continue

        english_chars = len(re.findall(r'[a-zA-Z]', clean_text))
        japanese_chars = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_text))
        total = english_chars + japanese_chars

        # Translate if more than 20% English
        if total > 0 and english_chars / total > 0.2:
            fixed = comprehensive_translate(value)
            if fixed != value:
                ja_data[key] = fixed
                fixes_applied += 1
                issues_found.append({
                    'key': key,
                    'original': value,
                    'fixed': fixed,
                    'type': 'auto_translate'
                })

    print(f"\nTotal fixes applied: {fixes_applied}")
    print(f"  - Complete manual fixes: {sum(1 for i in issues_found if i['type'] == 'complete_fix')}")
    print(f"  - Automatic translations: {sum(1 for i in issues_found if i['type'] == 'auto_translate')}")

    # Show examples
    complete_fixes = [i for i in issues_found if i['type'] == 'complete_fix'][:5]
    auto_fixes = [i for i in issues_found if i['type'] == 'auto_translate'][:5]

    if complete_fixes:
        print(f"\nComplete fix examples:")
        for issue in complete_fixes:
            print(f"  {issue['key']}:")
            print(f"    Before: {issue['original']}")
            print(f"    After:  {issue['fixed']}")

    if auto_fixes:
        print(f"\nAutomatic translation examples:")
        for issue in auto_fixes:
            print(f"  {issue['key']}:")
            print(f"    Before: {issue['original']}")
            print(f"    After:  {issue['fixed']}")

    # Save
    print(f"\nSaving fixed file: {ja_file}")
    save_json(ja_file, ja_data)

    # Save report
    report_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja_final_fix_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(issues_found, f, ensure_ascii=False, indent=2)

    print(f"Detailed report saved: {report_file}")

    # Final analysis
    print("\nFinal analysis...")
    still_english = 0
    for key, value in ja_data.items():
        clean = re.sub(r'\[[^\]]+\]', '', value)
        clean = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean)
        if clean:
            eng = len(re.findall(r'[a-zA-Z]', clean))
            jap = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean))
            total = eng + jap
            if total > 0 and eng / total > 0.4:
                still_english += 1

    print(f"Entries still with >40% English: {still_english}")
    print("\nDone!")

if __name__ == '__main__':
    main()
