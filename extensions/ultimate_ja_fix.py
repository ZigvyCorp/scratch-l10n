#!/usr/bin/env python3
"""
Ultimate comprehensive fix for Japanese extensions translation.
Includes ALL common English words found in the file.
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

def ultimate_translate(text):
    """
    Ultimate translation with comprehensive word list.
    Order matters - more specific phrases first, then individual words.
    """
    if not text:
        return text

    # Store variables temporarily
    variables = []
    temp_text = text
    for match in re.finditer(r'\[([^\]]+)\]', text):
        var_name = match.group(1)
        placeholder = f'__VAR{len(variables)}__'
        variables.append((placeholder, f'[{var_name}]'))
        temp_text = temp_text.replace(f'[{var_name}]', placeholder, 1)

    result = temp_text

    # Comprehensive translation dictionary (order matters - specific to general)
    translations = [
        # Multi-word phrases first
        (r'\bmy name\b', '自分の名前'),
        (r'\buser\s*name\b', 'ユーザー名'),
        (r'\bphone number\b', '電話番号'),
        (r'\bcan only include\b', 'のみ含めることができます'),
        (r'\bread only\b', '読み取り専用'),
        (r'\btext area\b', 'テキストエリア'),
        (r'\bcheck box\b', 'チェックボックス'),
        (r'\bradio button\b', 'ラジオボタン'),
        (r'\bdrop down\b', 'ドロップダウン'),
        (r'\bno scroll\b', 'スクロールなし'),
        (r'\bbold italic\b', '太字斜体'),
        (r'\bgoogle sheets\b', 'Googleスプレッドシート'),
        (r'\bfull screen\b', 'フルスクリーン'),
        (r'\bfull-screen\b', 'フルスクリーン'),
        (r'\bfullscreen\b', 'フルスクリーン'),
        (r'\bself-destruct\b', '自己破壊'),
        (r'\bself destruct\b', '自己破壊'),
        (r'\bground detection\b', '地面検出'),
        (r'\bcollision detection\b', '衝突検出'),
        (r'\bconvex hull\b', '凸包'),
        (r'\bvideo motion\b', 'ビデオの動き'),
        (r'\bpoint towards\b', '向ける'),
        (r'\bpoint to\b', '指す'),
        (r'\bgo to\b', '移動する'),
        (r'\bturn on\b', 'オンにする'),
        (r'\bturn off\b', 'オフにする'),
        (r'\bset to\b', 'を～にする'),
        (r'\bchange by\b', 'を～ずつ変える'),
        (r'\blook at\b', '見る'),
        (r'\bwithin distance\b', '距離以内'),
        (r'\bclone id\b', 'クローンID'),
        (r'\bcompound shape\b', '複合形状'),
        (r'\bcurve tolerance\b', '曲線許容誤差'),
        (r'\bpoint distance\b', '点間距離'),
        (r'\bbehave as\b', 'として振る舞う'),
        (r'\bcompare to\b', 'と比較する'),

        # Action verbs and verb phrases
        (r'\binitialize\b', '初期化する'),
        (r'\bconfigure\b', '構成する'),
        (r'\bapply\b', '適用する'),
        (r'\benable\b', '有効にする'),
        (r'\bdisable\b', '無効にする'),
        (r'\bactivate\b', '有効化する'),
        (r'\bdeactivate\b', '無効化する'),
        (r'\bcreate\b', '作成する'),
        (r'\bgenerate\b', '生成する'),
        (r'\bdelete\b', '削除する'),
        (r'\bremove\b', '削除する'),
        (r'\bdestroy\b', '破壊する'),
        (r'\badd\b', '追加する'),
        (r'\binsert\b', '挿入する'),
        (r'\bappend\b', '追加する'),
        (r'\bupdate\b', '更新する'),
        (r'\bmodify\b', '変更する'),
        (r'\bchange\b', '変更する'),
        (r'\bset\b', '設定する'),
        (r'\bget\b', '取得する'),
        (r'\bfetch\b', '取得する'),
        (r'\bretrieve\b', '取得する'),
        (r'\bshow\b', '表示する'),
        (r'\bdisplay\b', '表示する'),
        (r'\bhide\b', '非表示にする'),
        (r'\bclear\b', 'クリアする'),
        (r'\breset\b', 'リセットする'),
        (r'\blist\b', '一覧'),
        (r'\bjoin\b', '参加する'),
        (r'\bleave\b', '退出する'),
        (r'\bexit\b', '終了する'),
        (r'\bquit\b', '終了する'),
        (r'\bbroadcast\b', '送る'),
        (r'\bemit\b', '放出する'),
        (r'\breceive\b', '受信する'),
        (r'\bsend\b', '送る'),
        (r'\btransmit\b', '送信する'),
        (r'\bplay\b', '再生する'),
        (r'\bstop\b', '停止する'),
        (r'\bpause\b', '一時停止する'),
        (r'\bresume\b', '再開する'),
        (r'\bstart\b', '開始する'),
        (r'\bbegin\b', '開始する'),
        (r'\bend\b', '終了する'),
        (r'\bfinish\b', '完了する'),
        (r'\bcomplete\b', '完了する'),
        (r'\bsave\b', '保存する'),
        (r'\bload\b', '読み込む'),
        (r'\bopen\b', '開く'),
        (r'\bclose\b', '閉じる'),
        (r'\bconnect\b', '接続する'),
        (r'\bdisconnect\b', '切断する'),
        (r'\bmove\b', '動かす'),
        (r'\brotate\b', '回転する'),
        (r'\bscale\b', '拡大縮小する'),
        (r'\bresize\b', 'サイズ変更する'),
        (r'\btransform\b', '変換する'),
        (r'\btranslate\b', '移動する'),
        (r'\bshift\b', 'シフトする'),
        (r'\bglide\b', '滑らかに動く'),
        (r'\bteleport\b', 'テレポートする'),
        (r'\brebound\b', '跳ね返る'),
        (r'\bcollect\b', '収集する'),
        (r'\bgather\b', '集める'),
        (r'\bcount\b', '数える'),
        (r'\bmeasure\b', '測定する'),
        (r'\bcalculate\b', '計算する'),
        (r'\bcompute\b', '計算する'),
        (r'\bcheck\b', 'チェックする'),
        (r'\bverify\b', '確認する'),
        (r'\bvalidate\b', '検証する'),
        (r'\btest\b', 'テストする'),
        (r'\bcompare\b', '比較する'),
        (r'\bselect\b', '選択する'),
        (r'\bchoose\b', '選択する'),
        (r'\bpick\b', '選ぶ'),
        (r'\bfilter\b', 'フィルタする'),
        (r'\bsort\b', 'ソートする'),
        (r'\bsearch\b', '検索する'),
        (r'\bfind\b', '見つける'),
        (r'\bdetect\b', '検出する'),
        (r'\bsense\b', '感知する'),
        (r'\btouch\b', '触れる'),
        (r'\bhover\b', 'ホバーする'),
        (r'\bclick\b', 'クリックする'),
        (r'\bpress\b', '押す'),
        (r'\brelease\b', '離す'),
        (r'\bdrag\b', 'ドラッグする'),
        (r'\bdrop\b', 'ドロップする'),
        (r'\bscroll\b', 'スクロールする'),
        (r'\bzoom\b', 'ズームする'),
        (r'\bpan\b', 'パンする'),
        (r'\borbit\b', '周回する'),
        (r'\brender\b', 'レンダリングする'),
        (r'\bdraw\b', '描画する'),
        (r'\bpaint\b', '描く'),
        (r'\bsketch\b', 'スケッチする'),
        (r'\bfill\b', '塗りつぶす'),
        (r'\bstroke\b', 'ストロークする'),
        (r'\bclip\b', 'クリップする'),
        (r'\bmask\b', 'マスクする'),
        (r'\bblend\b', 'ブレンドする'),
        (r'\bmix\b', 'ミックスする'),
        (r'\bfade\b', 'フェードする'),
        (r'\btween\b', 'トゥイーンする'),
        (r'\banimate\b', 'アニメーションする'),
        (r'\bsimulate\b', 'シミュレートする'),
        (r'\bemulate\b', 'エミュレートする'),
        (r'\bimport\b', 'インポートする'),
        (r'\bexport\b', 'エクスポートする'),
        (r'\bupload\b', 'アップロードする'),
        (r'\bdownload\b', 'ダウンロードする'),
        (r'\bsynchronously\b', '同期的に'),
        (r'\basynchronously\b', '非同期的に'),

        # Technical terms and nouns
        (r'\bmultiplayer\b', 'マルチプレイヤー'),
        (r'\bphysics\b', '物理'),
        (r'\bdatabase\b', 'データベース'),
        (r'\bcloud\b', 'クラウド'),
        (r'\bwidget\b', 'ウィジェット'),
        (r'\bchart\b', 'グラフ'),
        (r'\bgraph\b', 'グラフ'),
        (r'\bgame\b', 'ゲーム'),
        (r'\bplayers\b', 'プレイヤー'),
        (r'\bplayer\b', 'プレイヤー'),
        (r'\bsprites\b', 'スプライト'),
        (r'\bsprite\b', 'スプライト'),
        (r'\bworlds\b', 'ワールド'),
        (r'\bworld\b', 'ワールド'),
        (r'\bservers\b', 'サーバー'),
        (r'\bserver\b', 'サーバー'),
        (r'\bhosts\b', 'ホスト'),
        (r'\bhost\b', 'ホスト'),
        (r'\bpasswords\b', 'パスワード'),
        (r'\bpassword\b', 'パスワード'),
        (r'\btables\b', 'テーブル'),
        (r'\btable\b', 'テーブル'),
        (r'\bsheet\b', 'シート'),
        (r'\bsheets\b', 'シート'),
        (r'\bobstacles\b', '障害物'),
        (r'\bobstacle\b', '障害物'),
        (r'\bcollectables\b', '収集可能物'),
        (r'\bcollectable\b', '収集可能物'),
        (r'\bobjects\b', 'オブジェクト'),
        (r'\bobject\b', 'オブジェクト'),
        (r'\bentities\b', 'エンティティ'),
        (r'\bentity\b', 'エンティティ'),
        (r'\bsensors\b', 'センサー'),
        (r'\bsensor\b', 'センサー'),
        (r'\bemitters\b', 'エミッター'),
        (r'\bemitter\b', 'エミッター'),
        (r'\bparticles\b', 'パーティクル'),
        (r'\bparticle\b', 'パーティクル'),
        (r'\bedges\b', 'エッジ'),
        (r'\bedge\b', 'エッジ'),
        (r'\bcorners\b', '角'),
        (r'\bcorner\b', '角'),
        (r'\bborders\b', '境界'),
        (r'\bborder\b', '境界'),

        # Properties and attributes
        (r'\bpositions\b', '位置'),
        (r'\bposition\b', '位置'),
        (r'\bdirections\b', '向き'),
        (r'\bdirection\b', '向き'),
        (r'\bspeeds\b', '速度'),
        (r'\bspeed\b', '速度'),
        (r'\bvelocities\b', '速度'),
        (r'\bvelocity\b', '速度'),
        (r'\bwidths\b', '幅'),
        (r'\bwidth\b', '幅'),
        (r'\bheights\b', '高さ'),
        (r'\bheight\b', '高さ'),
        (r'\bsizes\b', '大きさ'),
        (r'\bsize\b', '大きさ'),
        (r'\bscales\b', '拡大率'),
        (r'\bscale\b', '拡大率'),
        (r'\bcostumes\b', 'コスチューム'),
        (r'\bcostume\b', 'コスチューム'),
        (r'\bghost\b', '透明度'),
        (r'\brotations\b', '回転'),
        (r'\brotation\b', '回転'),
        (r'\bstyles\b', '方法'),
        (r'\bstyle\b', '方法'),
        (r'\bmessages\b', 'メッセージ'),
        (r'\bmessage\b', 'メッセージ'),
        (r'\bparameters\b', 'パラメータ'),
        (r'\bparameter\b', 'パラメータ'),
        (r'\bmodes\b', 'モード'),
        (r'\bmode\b', 'モード'),
        (r'\broles\b', '役割'),
        (r'\brole\b', '役割'),
        (r'\bcapacities\b', '定員'),
        (r'\bcapacity\b', '定員'),
        (r'\bregions\b', '地域'),
        (r'\bregion\b', '地域'),
        (r'\bgravity\b', '重力'),
        (r'\bforces\b', '力'),
        (r'\bforce\b', '力'),
        (r'\btorques\b', 'トルク'),
        (r'\btorque\b', 'トルク'),
        (r'\bimpulses\b', '衝撃'),
        (r'\bimpulse\b', '衝撃'),
        (r'\bmasses\b', '質量'),
        (r'\bmass\b', '質量'),
        (r'\bdensities\b', '密度'),
        (r'\bdensity\b', '密度'),
        (r'\bfrictions\b', '摩擦'),
        (r'\bfriction\b', '摩擦'),
        (r'\brestitutions\b', '反発'),
        (r'\brestitution\b', '反発'),
        (r'\bdampings\b', '減衰'),
        (r'\bdamping\b', '減衰'),
        (r'\blinear\b', '線形'),
        (r'\bangular\b', '角'),
        (r'\bcollisions\b', '衝突'),
        (r'\bcollision\b', '衝突'),
        (r'\bgrounds\b', '地面'),
        (r'\bground\b', '地面'),
        (r'\bslopes\b', '傾き'),
        (r'\bslope\b', '傾き'),
        (r'\bdetection\b', '検出'),
        (r'\bdebugs\b', 'デバッグ'),
        (r'\bdebug\b', 'デバッグ'),
        (r'\bdistances\b', '距離'),
        (r'\bdistance\b', '距離'),
        (r'\bprefixes\b', '接頭辞'),
        (r'\bprefix\b', '接頭辞'),
        (r'\bsuffixes\b', '接尾辞'),
        (r'\bsuffix\b', '接尾辞'),
        (r'\bclones\b', 'クローン'),
        (r'\bclone\b', 'クローン'),
        (r'\bcurrents\b', '現在の'),
        (r'\bcurrent\b', '現在の'),
        (r'\btimes\b', '時間'),
        (r'\btime\b', '時間'),
        (r'\bdurations\b', '期間'),
        (r'\bduration\b', '期間'),
        (r'\bperiods\b', '期間'),
        (r'\bperiod\b', '期間'),
        (r'\bdelays\b', '遅延'),
        (r'\bdelay\b', '遅延'),
        (r'\bintervals\b', '間隔'),
        (r'\binterval\b', '間隔'),
        (r'\bseconds\b', '秒'),
        (r'\bsecond\b', '秒'),
        (r'\bvideos\b', 'ビデオ'),
        (r'\bvideo\b', 'ビデオ'),
        (r'\bimages\b', '画像'),
        (r'\bimage\b', '画像'),
        (r'\bphotos\b', '写真'),
        (r'\bphoto\b', '写真'),
        (r'\bpictures\b', '画像'),
        (r'\bpicture\b', '画像'),
        (r'\btextures\b', 'テクスチャ'),
        (r'\btexture\b', 'テクスチャ'),
        (r'\bmaterials\b', 'マテリアル'),
        (r'\bmaterial\b', 'マテリアル'),
        (r'\bcolors\b', '色'),
        (r'\bcolor\b', '色'),
        (r'\bcolours\b', '色'),
        (r'\bcolour\b', '色'),
        (r'\bcanvases\b', 'キャンバス'),
        (r'\bcanvas\b', 'キャンバス'),
        (r'\blabels\b', 'ラベル'),
        (r'\blabel\b', 'ラベル'),
        (r'\bcontainers\b', 'コンテナ'),
        (r'\bcontainer\b', 'コンテナ'),
        (r'\bbuttons\b', 'ボタン'),
        (r'\bbutton\b', 'ボタン'),
        (r'\bsliders\b', 'スライダー'),
        (r'\bslider\b', 'スライダー'),
        (r'\binputs\b', '入力'),
        (r'\binput\b', '入力'),
        (r'\boutputs\b', '出力'),
        (r'\boutput\b', '出力'),
        (r'\bfields\b', 'フィールド'),
        (r'\bfield\b', 'フィールド'),
        (r'\bvalues\b', '値'),
        (r'\bvalue\b', '値'),
        (r'\bdata\b', 'データ'),
        (r'\bkeys\b', 'キー'),
        (r'\bkey\b', 'キー'),
        (r'\bids\b', 'ID'),
        (r'\bid\b', 'ID'),
        (r'\bnames\b', '名前'),
        (r'\bnamed\b', '名前'),
        (r'\bname\b', '名前'),
        (r'\btitles\b', 'タイトル'),
        (r'\btitle\b', 'タイトル'),
        (r'\btext\b', 'テキスト'),
        (r'\bstring\b', '文字列'),
        (r'\bnumber\b', '数'),
        (r'\binteger\b', '整数'),
        (r'\bfloat\b', '浮動小数点'),
        (r'\bboolean\b', '真偽値'),
        (r'\barray\b', '配列'),
        (r'\blists\b', 'リスト'),
        (r'\blist\b', 'リスト'),
        (r'\btags\b', 'タグ'),
        (r'\btag\b', 'タグ'),
        (r'\bflags\b', 'フラグ'),
        (r'\bflag\b', 'フラグ'),
        (r'\bstates\b', '状態'),
        (r'\bstate\b', '状態'),
        (r'\bstatus\b', 'ステータス'),
        (r'\blevels\b', 'レベル'),
        (r'\blevel\b', 'レベル'),
        (r'\blayers\b', 'レイヤー'),
        (r'\blayer\b', 'レイヤー'),
        (r'\bgroups\b', 'グループ'),
        (r'\bgroup\b', 'グループ'),
        (r'\bcategories\b', 'カテゴリー'),
        (r'\bcategory\b', 'カテゴリー'),
        (r'\btypes\b', 'タイプ'),
        (r'\btype\b', 'タイプ'),
        (r'\bkinds\b', '種類'),
        (r'\bkind\b', '種類'),
        (r'\bclasses\b', 'クラス'),
        (r'\bclass\b', 'クラス'),

        # Shapes
        (r'\bcircles\b', '円'),
        (r'\bcircle\b', '円'),
        (r'\brectangles\b', '四角形'),
        (r'\brectangle\b', '四角形'),
        (r'\bboxes\b', '四角形'),
        (r'\bbox\b', '四角形'),
        (r'\bsquares\b', '正方形'),
        (r'\bsquare\b', '正方形'),
        (r'\bpolygons\b', '多角形'),
        (r'\bpolygon\b', '多角形'),
        (r'\btriangles\b', '三角形'),
        (r'\btriangle\b', '三角形'),
        (r'\bcapsules\b', 'カプセル'),
        (r'\bcapsule\b', 'カプセル'),
        (r'\bspheres\b', '球'),
        (r'\bsphere\b', '球'),
        (r'\bcubes\b', '立方体'),
        (r'\bcube\b', '立方体'),
        (r'\bcylinders\b', '円柱'),
        (r'\bcylinder\b', '円柱'),
        (r'\bcones\b', '円錐'),
        (r'\bcone\b', '円錐'),
        (r'\bshapes\b', '形状'),
        (r'\bshape\b', '形状'),
        (r'\blines\b', '線'),
        (r'\bline\b', '線'),
        (r'\bpoints\b', '点'),
        (r'\bpoint\b', '点'),
        (r'\bvertices\b', '頂点'),
        (r'\bvertex\b', '頂点'),

        # Dimensions and measurements
        (r'\baxes\b', '軸'),
        (r'\baxis\b', '軸'),
        (r'\bangles\b', '角度'),
        (r'\bangle\b', '角度'),
        (r'\bradii\b', '半径'),
        (r'\bradius\b', '半径'),
        (r'\bdiameters\b', '直径'),
        (r'\bdiameter\b', '直径'),
        (r'\bthickness\b', '太さ'),
        (r'\bthick\b', '太い'),
        (r'\bthin\b', '細い'),
        (r'\boffsets\b', 'オフセット'),
        (r'\boffset\b', 'オフセット'),
        (r'\bmargins\b', '余白'),
        (r'\bmargin\b', '余白'),
        (r'\bpaddings\b', 'パディング'),
        (r'\bpadding\b', 'パディング'),
        (r'\bspacing\b', '間隔'),
        (r'\bspace\b', '空間'),
        (r'\bgaps\b', '隙間'),
        (r'\bgap\b', '隙間'),
        (r'\bdepths\b', '深さ'),
        (r'\bdepth\b', '深さ'),

        # Directions and positions
        (r'\bpositions\b', '位置'),
        (r'\bfronts\b', '前'),
        (r'\bfront\b', '前'),
        (r'\bbacks\b', '後ろ'),
        (r'\bback\b', '後ろ'),
        (r'\blefts\b', '左'),
        (r'\bleft\b', '左'),
        (r'\brights\b', '右'),
        (r'\bright\b', '右'),
        (r'\btops\b', '上'),
        (r'\btop\b', '上'),
        (r'\bbottoms\b', '下'),
        (r'\bbottom\b', '下'),
        (r'\bcenters\b', '中央'),
        (r'\bcenter\b', '中央'),
        (r'\bcentres\b', '中央'),
        (r'\bcentre\b', '中央'),
        (r'\bmiddles\b', '中央'),
        (r'\bmiddle\b', '中央'),
        (r'\bsides\b', '辺'),
        (r'\bside\b', '辺'),
        (r'\bforwards\b', '前方'),
        (r'\bforward\b', '前方'),
        (r'\bbackwards\b', '後方'),
        (r'\bbackward\b', '後方'),
        (r'\bupwards\b', '上方'),
        (r'\bupward\b', '上方'),
        (r'\bdownwards\b', '下方'),
        (r'\bdownward\b', '下方'),

        # States and conditions
        (r'\bstatic\b', '静的'),
        (r'\bdynamic\b', '動的'),
        (r'\bkinematic\b', '運動学的'),
        (r'\bfixed\b', '固定'),
        (r'\bmovable\b', '移動可能'),
        (r'\bhosted\b', 'ホスト'),
        (r'\breceived\b', '受信した'),
        (r'\bopened\b', '開いた'),
        (r'\bclosed\b', '閉じた'),
        (r'\bjoined\b', '参加した'),
        (r'\bleft\b', '退出した'),
        (r'\bcreated\b', '作成された'),
        (r'\bremoved\b', '削除された'),
        (r'\bhovered\b', 'ホバーされた'),
        (r'\bpressed\b', '押された'),
        (r'\bclicked\b', 'クリックされた'),
        (r'\btouching\b', '触れている'),
        (r'\btouched\b', '触れた'),
        (r'\bblocked\b', 'ブロックされた'),
        (r'\bblocking\b', 'ブロック中'),
        (r'\benabled\b', '有効'),
        (r'\bdisabled\b', '無効'),
        (r'\bactive\b', 'アクティブ'),
        (r'\binactive\b', '非アクティブ'),
        (r'\bvisible\b', '表示'),
        (r'\binvisible\b', '非表示'),
        (r'\bhidden\b', '非表示'),

        # Comparisons and ranges
        (r'\bminimum\b', '最小'),
        (r'\bmin\b', '最小'),
        (r'\bmaximum\b', '最大'),
        (r'\bmax\b', '最大'),
        (r'\bminimums\b', '最小値'),
        (r'\bmins\b', '最小値'),
        (r'\bmaximums\b', '最大値'),
        (r'\bmaxs\b', '最大値'),
        (r'\branges\b', '範囲'),
        (r'\brange\b', '範囲'),
        (r'\blimits\b', '限界'),
        (r'\blimit\b', '限界'),
        (r'\bthresholds\b', 'しきい値'),
        (r'\bthreshold\b', 'しきい値'),
        (r'\bcounts\b', '数'),
        (r'\bcount\b', '数'),
        (r'\btotals\b', '合計'),
        (r'\btotal\b', '合計'),
        (r'\bsums\b', '合計'),
        (r'\bsum\b', '合計'),
        (r'\baverages\b', '平均'),
        (r'\baverage\b', '平均'),
        (r'\bratios\b', '比率'),
        (r'\bratio\b', '比率'),
        (r'\bpercentages\b', 'パーセント'),
        (r'\bpercentage\b', 'パーセント'),

        # 3D and camera
        (r'\bcameras\b', 'カメラ'),
        (r'\bcamera\b', 'カメラ'),
        (r'\btargets\b', 'ターゲット'),
        (r'\btarget\b', 'ターゲット'),
        (r'\bviews\b', '視点'),
        (r'\bview\b', '視点'),
        (r'\bperspectives\b', '視点'),
        (r'\bperspective\b', '視点'),
        (r'\borthographic\b', '正投影'),
        (r'\bprojections\b', '投影'),
        (r'\bprojection\b', '投影'),
        (r'\bfov\b', '視野角'),

        # Lighting and effects
        (r'\blights\b', 'ライト'),
        (r'\blight\b', 'ライト'),
        (r'\bshadows\b', '影'),
        (r'\bshadow\b', '影'),
        (r'\bbrightness\b', '明るさ'),
        (r'\bintensities\b', '強度'),
        (r'\bintensity\b', '強度'),
        (r'\bopacity\b', '不透明度'),
        (r'\btransparency\b', '透明度'),
        (r'\balpha\b', 'アルファ'),
        (r'\beffects\b', '効果'),
        (r'\beffect\b', '効果'),
        (r'\bfilters\b', 'フィルタ'),
        (r'\bfilter\b', 'フィルタ'),

        # Data and formats
        (r'\burls\b', 'URL'),
        (r'\burl\b', 'URL'),
        (r'\blinks\b', 'リンク'),
        (r'\blink\b', 'リンク'),
        (r'\bpaths\b', 'パス'),
        (r'\bpath\b', 'パス'),
        (r'\bfiles\b', 'ファイル'),
        (r'\bfile\b', 'ファイル'),
        (r'\bformats\b', '形式'),
        (r'\bformat\b', '形式'),
        (r'\bjson\b', 'JSON'),
        (r'\bxml\b', 'XML'),
        (r'\bhtml\b', 'HTML'),
        (r'\bcss\b', 'CSS'),
        (r'\bapi\b', 'API'),

        # Miscellaneous
        (r'\brows\b', '行'),
        (r'\brow\b', '行'),
        (r'\bcolumns\b', '列'),
        (r'\bcolumn\b', '列'),
        (r'\bcells\b', 'セル'),
        (r'\bcell\b', 'セル'),
        (r'\btokens\b', 'トークン'),
        (r'\btoken\b', 'トークン'),
        (r'\bsessions\b', 'セッション'),
        (r'\bsession\b', 'セッション'),
        (r'\bbackgrounds\b', '背景'),
        (r'\bbackground\b', '背景'),
        (r'\bforegrounds\b', '前景'),
        (r'\bforeground\b', '前景'),
        (r'\bbodies\b', 'ボディ'),
        (r'\bbody\b', 'ボディ'),
        (r'\bcompound\b', '複合'),
        (r'\btolerance\b', '許容誤差'),
        (r'\bbehave\b', '振る舞う'),
        (r'\bgoogle\b', 'Google'),

        # Context and logic
        (r'\bwithin\b', '以内'),
        (r'\bbetween\b', '間'),
        (r'\bamong\b', '中'),
        (r'\baround\b', '周り'),
        (r'\bnear\b', '近く'),
        (r'\bfar\b', '遠く'),
        (r'\bduring\b', '間'),
        (r'\bafter\b', '後'),
        (r'\bbefore\b', '前'),
        (r'\buntil\b', 'まで'),
        (r'\bwhile\b', '間'),
        (r'\bwhen\b', 'とき'),
        (r'\bif\b', 'もし'),
        (r'\bthen\b', 'ならば'),
        (r'\belse\b', 'それ以外'),
        (r'\botherwise\b', 'それ以外'),

        # Prepositions and articles
        (r'\bfrom\b', 'から'),
        (r'\bto\b', 'へ'),
        (r'\bin\b', 'の'),
        (r'\bat\b', 'で'),
        (r'\bby\b', 'による'),
        (r'\bwith\b', 'で'),
        (r'\bwithout\b', 'なしで'),
        (r'\bfor\b', '用'),
        (r'\bof\b', 'の'),
        (r'\band\b', 'と'),
        (r'\bor\b', 'または'),
        (r'\bbut\b', 'しかし'),
        (r'\bas\b', 'として'),
        (r'\bvia\b', '経由で'),
        (r'\binto\b', 'へ'),
        (r'\bonto\b', '上へ'),
        (r'\bover\b', '上'),
        (r'\bunder\b', '下'),
        (r'\babove\b', '上'),
        (r'\bbelow\b', '下'),
        (r'\bthrough\b', '通して'),
        (r'\bacross\b', '横切って'),
        (r'\balong\b', '沿って'),
        (r'\btowards\b', '向かって'),
        (r'\btoward\b', '向かって'),
        (r'\bagainst\b', '対して'),
        (r'\bthe\b', ''),  # Articles removed in Japanese
        (r'\ba\b', ''),
        (r'\ban\b', ''),

        # Common words
        (r'\bthis\b', 'この'),
        (r'\bthat\b', 'その'),
        (r'\bthese\b', 'これらの'),
        (r'\bthose\b', 'それらの'),
        (r'\bmy\b', '自分の'),
        (r'\byour\b', 'あなたの'),
        (r'\bhis\b', '彼の'),
        (r'\bher\b', '彼女の'),
        (r'\bits\b', 'その'),
        (r'\bour\b', '私たちの'),
        (r'\btheir\b', '彼らの'),
        (r'\ball\b', 'すべて'),
        (r'\bany\b', '任意'),
        (r'\bsome\b', 'いくつか'),
        (r'\bmany\b', '多くの'),
        (r'\bmuch\b', '多くの'),
        (r'\bfew\b', '少ない'),
        (r'\blittle\b', '少し'),
        (r'\bnone\b', 'なし'),
        (r'\bother\b', 'その他'),
        (r'\banother\b', '別の'),
        (r'\beach\b', '各'),
        (r'\bevery\b', '各'),
        (r'\boriginal\b', 'オリジナル'),
        (r'\bdefault\b', 'デフォルト'),
        (r'\bcustom\b', 'カスタム'),
        (r'\bnew\b', '新しい'),
        (r'\bold\b', '古い'),
        (r'\bfirst\b', '最初'),
        (r'\blast\b', '最後'),
        (r'\bnext\b', '次'),
        (r'\bprevious\b', '前'),
        (r'\bnormal\b', '通常'),
        (r'\bbold\b', '太字'),
        (r'\bitalic\b', '斜体'),
        (r'\bsingle\b', '単一'),
        (r'\bmultiple\b', '複数'),
        (r'\bdouble\b', '2倍'),
        (r'\bhalf\b', '半分'),
        (r'\bdigits\b', '数字'),
        (r'\bdigit\b', '数字'),
        (r'\bonly\b', 'のみ'),
        (r'\binclude\b', '含む'),
        (r'\bcan\b', 'できる'),
        (r'\bwill\b', 'する'),
        (r'\bshould\b', 'すべき'),
        (r'\bmust\b', 'しなければならない'),
        (r'\bmay\b', 'かもしれない'),
        (r'\bhas\b', '持つ'),
        (r'\bhave\b', '持つ'),
        (r'\bis\b', 'は'),
        (r'\bare\b', 'は'),
        (r'\bwas\b', 'だった'),
        (r'\bwere\b', 'だった'),
        (r'\bbeen\b', 'された'),
        (r'\bbeing\b', 'されている'),
    ]

    # Apply translations
    for pattern, replacement in translations:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    # Restore variables
    for placeholder, variable in variables:
        result = result.replace(placeholder, variable)

    # Clean up multiple spaces
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result

def main():
    ja_file = '/home/binyu/dev/scratch-workspace/scratch-l10n/extensions/ja.json'

    print("Loading Japanese extensions file...")
    ja_data = load_json(ja_file)

    print(f"Total entries: {len(ja_data)}")
    print("\nApplying ultimate comprehensive translation...")

    fixes_applied = 0
    before_counts = []
    after_counts = []

    for key, value in list(ja_data.items()):
        # Count English before
        clean_before = re.sub(r'\[[^\]]+\]', '', value)
        clean_before = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_before)
        eng_before = len(re.findall(r'[a-zA-Z]', clean_before))
        jap_before = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_before))
        total_before = eng_before + jap_before

        # Apply translation
        fixed = ultimate_translate(value)

        if fixed != value:
            ja_data[key] = fixed
            fixes_applied += 1

            # Count English after
            clean_after = re.sub(r'\[[^\]]+\]', '', fixed)
            clean_after = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean_after)
            eng_after = len(re.findall(r'[a-zA-Z]', clean_after))
            jap_after = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean_after))
            total_after = eng_after + jap_after

            if total_before > 0:
                before_counts.append(eng_before / total_before)
            if total_after > 0:
                after_counts.append(eng_after / total_after)

    print(f"\nFixes applied: {fixes_applied}")
    if before_counts and after_counts:
        avg_before = sum(before_counts) / len(before_counts) * 100
        avg_after = sum(after_counts) / len(after_counts) * 100
        print(f"Average English % before: {avg_before:.1f}%")
        print(f"Average English % after: {avg_after:.1f}%")
        print(f"Improvement: {avg_before - avg_after:.1f}%")

    # Final analysis
    print("\nFinal analysis...")
    still_problematic = 0
    for key, value in ja_data.items():
        clean = re.sub(r'\[[^\]]+\]', '', value)
        clean = re.sub(r'[0-9()\s\-\.,!?:;%]+', '', clean)
        if clean:
            eng = len(re.findall(r'[a-zA-Z]', clean))
            jap = len(re.findall(r'[ぁ-んァ-ヴー一-龯]', clean))
            total = eng + jap
            if total > 0 and eng / total > 0.4:
                still_problematic += 1

    print(f"Entries still with >40% English: {still_problematic}")
    print(f"Improvement: {777 - still_problematic} entries fixed")

    # Save
    backup_file = ja_file + '.backup2'
    print(f"\nCreating backup: {backup_file}")
    save_json(backup_file, load_json(ja_file))

    print(f"Saving fixed file: {ja_file}")
    save_json(ja_file, ja_data)

    print("\nDone!")

if __name__ == '__main__':
    main()
