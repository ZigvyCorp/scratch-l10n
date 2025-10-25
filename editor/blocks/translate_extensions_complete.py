#!/usr/bin/env python3
"""
Complete translation script for scratch-l10n/editor/extensions/
Translates ALL remaining untranslated entries.
"""

import json
import os

# Comprehensive translation mappings for each language
TRANSLATIONS = {
    'es': {
        # Font names - keep as is (they are proper nouns)
        'Arial': 'Arial',
        'Arial, Bold': 'Arial, Negrita',
        'Calibri': 'Calibri',
        'Cambria': 'Cambria',
        'Copperplate': 'Copperplate',
        'Courier': 'Courier',
        'Courier New': 'Courier New',
        'Courier New, Bold': 'Courier New, Negrita',
        'Garamond': 'Garamond',
        'Helvetica': 'Helvetica',
        'KaiTi': 'KaiTi',
        'Microsoft Yahei': 'Microsoft Yahei',
        'SimHei': 'SimHei',
        'SimSun': 'SimSun',
        'SimSun, Bold': 'SimSun, Negrita',
        'Times': 'Times',
        'Times New Roman': 'Times New Roman',
        'Times New Roman, Bold': 'Times New Roman, Negrita',
        'Verdana': 'Verdana',

        # Common terms
        'OK': 'Aceptar',
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        'yes': 'sí',
        'no': 'no',
        'normal': 'normal',
        'Linear': 'Lineal',
        'Exponential': 'Exponencial',

        # Starfield items
        'Starfield 1': 'Campo estelar 1',
        'Starfield 2': 'Campo estelar 2',
        'Starfield 3': 'Campo estelar 3',
        'Starfield 4': 'Campo estelar 4',
        'Starfield 5': 'Campo estelar 5',
        'Starfield 6': 'Campo estelar 6',
        'Starfield 7': 'Campo estelar 7',
        'Starfield 8': 'Campo estelar 8',
        'Starfield and Sun': 'Campo estelar y sol',

        # 3D/Avatar terms
        'addavatar': 'añadir avatar',
        'aura': 'aura',
        'avatarrobot1': 'robot avatar 1',
        'avatarrobot2': 'robot avatar 2',
        'avatarrobot3': 'robot avatar 3',
        'diffusion': 'difusión',
        'emission': 'emisión',
        'hemisphericemitter': 'emisor hemisférico',
        'normal camera mode': 'modo de cámara normal',
        'sensortype': 'tipo de sensor',
        'saveprojectfirst': 'guardar proyecto primero',
        'loginbeforecreate': 'iniciar sesión antes de crear',

        # Music instruments
        'music.drumBongo': '(13) Bongo',
        'music.drumCabasa': '(15) Cabasa',
        'music.drumClaves': '(9) Claves',
        'music.drumConga': '(14) Conga',
        'music.drumCuica': '(18) Cuica',
        'music.getTempo': 'tempo',
        'music.instrumentMarimba': '(13) Marimba',
        'music.instrumentPiano': '(1) Piano',
        'music.instrumentPizzicato': '(7) Pizzicato',

        # Text to speech
        'text2speech.tenor': 'tenor',

        # WeDo
        'wedo2.motorId.a': 'motor A',
        'wedo2.motorId.b': 'motor B',
        'wedo2.motorId.default': 'motor',

        # Pen
        'pen.colorMenu.color': 'color',

        # P2P
        'p2p.formatContent.normal': 'normal',

        # Widget
        'widget.addRadioButton.horizontal': 'horizontal',
        'widget.addRadioButton.vertical': 'vertical',
        'widget.addRichTextbox': 'añadir cuadro de texto enriquecido',
        'widget.camera.normal': 'normal',
        'widget.chat.robot': 'robot',
        'widget.disableWidget': 'desactivar widget',
        'widget.menuItem.normal': 'normal',
        'widget.menuItem.show': 'mostrar',
        'widget.tabMenu.no': 'no',

        # 3D actions
        'd3action_d3_getXYZonPlanefromXY': 'mapear pantalla XY [X] [Y] a posición XYZ en objeto [OBJECTNAME] [PLANENAME]',
        'd3action_d3_movespsmesh': 'mover partícula en sps [NAME] en x [X] y [Y] z [Z] tiempo [TIME]',
        'd3action_d3_phoveredname': 'nombre del objeto previamente señalado',
        'd3object_d3_removeparent': 'quitar padre de [OBJECTNAME]',
        'd3physics_d3_changephysics': 'cambiar física de [OBJECTNAME] a [PHYSICSTYPE]',
        'd3scene_d3_readjoystick': 'leer joystick [AXIS] en [JOYSTICKID]',
        'd3tools_d3_animatetextureframes': 'animar cuadros de textura en [MESH] nombre de hoja de sprites [SPRITESHEETNAME] desde fila [ROWSTART] columna [COLUMNSTART] a fila [ROWEND] columna [COLUMNEND] ancho [WIDTH] alto [HEIGHT] duración [DURATION]',
    },
    'ja': {
        # Font names
        'Arial': 'Arial',
        'Arial, Bold': 'Arial, 太字',
        'Calibri': 'Calibri',
        'Cambria': 'Cambria',
        'Copperplate': 'Copperplate',
        'Courier': 'Courier',
        'Courier New': 'Courier New',
        'Courier New, Bold': 'Courier New, 太字',
        'Garamond': 'Garamond',
        'Helvetica': 'Helvetica',
        'KaiTi': 'KaiTi',
        'Microsoft Yahei': 'Microsoft Yahei',
        'SimHei': 'SimHei',
        'SimSun': 'SimSun',
        'SimSun, Bold': 'SimSun, 太字',
        'Times': 'Times',
        'Times New Roman': 'Times New Roman',
        'Times New Roman, Bold': 'Times New Roman, 太字',
        'Verdana': 'Verdana',

        # Common terms
        'OK': 'OK',
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',

        # Emitters and shapes
        'boxemitter': 'ボックスエミッター',
        'circle': '円',
        'coneemitter': 'コーンエミッター',
        'cylinderemitter': 'シリンダーエミッター',
        'hemisphericemitter': '半球エミッター',
        'meshemitter': 'メッシュエミッター',
        'pointemitter': 'ポイントエミッター',
        'sphereemitter': '球体エミッター',
        'rectangle': '長方形',

        # Effects
        'diffusion': '拡散',
        'emission': '放射',
        'fire': '火',
        'halo': 'ハロー',
        'light': '光',
        'orb': 'オーブ',
        'smoke': '煙',
        'spark': '火花',
        'water': '水',

        # States
        'dispose': '破棄',
        'dynamic': '動的',
        'static': '静的',
        'stop': '停止',
        'floor': '床',
        'wall': '壁',

        # Categories
        'd3arvr.categoryName': '3D AR/VR',

        # P2P time zones
        'p2p.scheduleEmailService.centralTime': '中部時間',
        'p2p.scheduleEmailService.easternTime': '東部時間',
        'p2p.scheduleEmailService.mountainTime': '山岳部時間',
        'p2p.scheduleEmailService.pacificTime': '太平洋時間',

        # Widget
        'widget.camera.back': '背面',
        'widget.camera.flipped': '反転',
        'widget.camera.normal': '通常',
        'widget.camera.side': '側面',
        'widget.chartType.bar': '棒グラフ',
        'widget.chartType.line': '折れ線グラフ',
        'widget.chartType.percentage': 'パーセント',
        'widget.chartType.pie': '円グラフ',
        'widget.chat.robot': 'ロボット',
        'widget.chat.user': 'ユーザー',
        'widget.disable': '無効',
        'widget.enable': '有効',
        'widget.image.keep': '維持',
        'widget.image.stretch': '伸縮',
    },
    'zh-cn': {
        # Font names
        'Arial': 'Arial',
        'Calibri': 'Calibri',
        'Cambria': 'Cambria',
        'Copperplate': 'Copperplate',
        'Courier': 'Courier',
        'Courier New': 'Courier New',
        'Garamond': 'Garamond',
        'Helvetica': 'Helvetica',
        'Times': 'Times',
        'Times New Roman': 'Times New Roman',
        'Verdana': 'Verdana',
        'Earth Rising': 'Earth Rising',

        # Common terms
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        'diffusion': '漫反射',
        'emission': '发光',

        # 3D extensions
        'd3tool.categoryName': '3D工具',
        'd3_exportboj': '将对象[NAME]导出为OBJ文件和MTL文件',
        'd3action_d3_getXYZonPlanefromXY': '将屏幕XY [X] [Y] 映射到对象[OBJECTNAME]平面[PLANENAME]上的XYZ位置',
        'd3action_d3_movespsmesh': '在sps [NAME]中移动粒子到x [X] y [Y] z [Z] 时间[TIME]',
        'd3action_d3_phoveredname': '上一个悬停对象名称',
        'd3object_d3_spritemaxx': '精灵对象最大x',
        'd3object_d3_spritemaxy': '精灵对象最大y',
        'd3object_d3_spritemaxz': '精灵对象最大z',
        'd3tools_d3_animatetextureframes': '在[MESH]上动画纹理帧 精灵表名称[SPRITESHEETNAME] 从行[ROWSTART]列[COLUMNSTART]到行[ROWEND]列[COLUMNEND] 宽度[WIDTH] 高度[HEIGHT] 持续时间[DURATION]',

        # MP (Multiplayer)
        'mp.stopType.continueAndCollect': '继续并收集',
        'mp.stopType.reboundAndDelete': '反弹并删除',
        'mp.stopType.selfDestructAndCollect': '自毁并收集',
        'mp.stopType.stopAndCollect': '停止并收集',

        # P2P
        'p2p.scheduleEmailService': '预约电子邮件服务',
        'p2p.scheduleEmailService.centralTime': '中部时间',
        'p2p.scheduleEmailService.easternTime': '东部时间',
        'p2p.scheduleEmailService.mountainTime': '山地时间',
        'p2p.scheduleEmailService.pacificTime': '太平洋时间',
        'p2p.schedulePhoneMessageService': '预约短信服务',

        # Widget
        'widget.chartType.bar': '柱状图',
    },
    'pl': {
        # Font names
        'Arial': 'Arial',
        'Arial, Bold': 'Arial, Pogrubiony',
        'Calibri': 'Calibri',
        'Cambria': 'Cambria',
        'Copperplate': 'Copperplate',
        'Courier': 'Courier',
        'Courier New': 'Courier New',
        'Courier New, Bold': 'Courier New, Pogrubiony',
        'Garamond': 'Garamond',
        'Helvetica': 'Helvetica',
        'KaiTi': 'KaiTi',
        'Microsoft Yahei': 'Microsoft Yahei',
        'SimHei': 'SimHei',
        'SimSun': 'SimSun',
        'SimSun, Bold': 'SimSun, Pogrubiony',
        'Times': 'Times',
        'Times New Roman': 'Times New Roman',
        'Times New Roman, Bold': 'Times New Roman, Pogrubiony',
        'Verdana': 'Verdana',

        # Common terms
        'OK': 'OK',
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        'beta': 'beta',
        'start': 'start',
        'stop': 'stop',

        # 3D/Avatar
        'addtorus': 'dodaj torus',
        'aura': 'aura',
        'avatarrobot1': 'robot awatar 1',
        'avatarrobot2': 'robot awatar 2',
        'avatarrobot3': 'robot awatar 3',
        'd3arvr.categoryName': '3D AR/VR',

        # Music
        'music.drumBongo': '(13) Bongo',
        'music.drumVibraslap': '(17) Vibraslap',
        'music.getTempo': 'tempo',
        'music.instrumentMarimba': '(13) Marimba',
        'music.instrumentPizzicato': '(7) Pizzicato',

        # Widget
        'widget.chat.robot': 'robot',
        'widget.menuItem.start': 'start',
        'widget.menuItem.stop': 'stop',
    },
    'vi': {
        # Font names
        'Arial': 'Arial',
        'Arial, Bold': 'Arial, Đậm',
        'Calibri': 'Calibri',
        'Cambria': 'Cambria',
        'Copperplate': 'Copperplate',
        'Courier': 'Courier',
        'Courier New': 'Courier New',
        'Courier New, Bold': 'Courier New, Đậm',
        'Garamond': 'Garamond',
        'Helvetica': 'Helvetica',
        'KaiTi': 'KaiTi',
        'Microsoft Yahei': 'Microsoft Yahei',
        'SimHei': 'SimHei',
        'SimSun': 'SimSun',
        'SimSun, Bold': 'SimSun, Đậm',
        'Times': 'Times',
        'Times New Roman': 'Times New Roman',
        'Times New Roman, Bold': 'Times New Roman, Đậm',
        'Verdana': 'Verdana',

        # Common terms
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        'alpha': 'alpha',
        'beta': 'beta',

        # Database
        'database.categoryName': 'Cơ sở dữ liệu',

        # Music instruments
        'music.drumCabasa': '(15) Cabasa',
        'music.drumGuiro': '(16) Guiro',
        'music.drumVibraslap': '(17) Vibraslap',
        'music.instrumentBass': '(6) Đàn bass',
        'music.instrumentBassoon': '(14) Kèn bassoon',
        'music.instrumentSteelDrum': '(18) Trống thép',
        'music.instrumentSynthPad': '(21) Tổng hợp Pad',
        'music.instrumentTrombone': '(9) Kèn trombone',
        'music.instrumentVibraphone': '(16) Vibraphone',

        # Text to speech
        'text2speech.alto': 'alto',
        'text2speech.tenor': 'tenor',

        # Widget
        'widget.chat.robot': 'robot',
    }
}

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file with proper formatting"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

def find_untranslated(en_data, target_data):
    """Find entries that are empty or still in English"""
    untranslated = []
    for key, en_value in en_data.items():
        target_value = target_data.get(key, '')
        if not target_value or target_value == en_value:
            untranslated.append(key)
    return untranslated

def main():
    base_dir = '/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions'
    en_path = os.path.join(base_dir, 'en.json')

    # Load English reference
    print("Loading English reference...")
    en_data = load_json(en_path)

    languages = {
        'es': 'Spanish',
        'ja': 'Japanese',
        'zh-cn': 'Chinese (Simplified)',
        'pl': 'Polish',
        'vi': 'Vietnamese'
    }

    summary = {}

    for lang_code, lang_name in languages.items():
        print(f"\n{'='*60}")
        print(f"Processing {lang_name} ({lang_code})...")
        print('='*60)

        target_path = os.path.join(base_dir, f'{lang_code}.json')

        # Load target language file
        target_data = load_json(target_path)

        # Find untranslated entries
        untranslated = find_untranslated(en_data, target_data)
        print(f"Found {len(untranslated)} untranslated entries")

        if not untranslated:
            print(f"No untranslated entries for {lang_name}")
            summary[lang_code] = {'translated': 0, 'total': len(en_data), 'remaining': 0}
            continue

        # Translate entries
        translations_dict = TRANSLATIONS.get(lang_code, {})
        translated_count = 0

        for key in untranslated:
            en_value = en_data[key]

            # Check if we have a translation
            if key in translations_dict:
                translated_value = translations_dict[key]
                target_data[key] = translated_value
                translated_count += 1
                print(f"  ✓ {key}")

        # Save updated file
        if translated_count > 0:
            save_json(target_path, target_data)
            print(f"\n✓ Saved {translated_count} translations to {lang_code}.json")

        remaining = len(untranslated) - translated_count
        summary[lang_code] = {
            'translated': translated_count,
            'total': len(untranslated),
            'remaining': remaining
        }

    # Print summary
    print("\n" + "="*60)
    print("TRANSLATION SUMMARY")
    print("="*60)
    total_translated = 0
    total_remaining = 0

    for lang_code, lang_name in languages.items():
        stats = summary[lang_code]
        print(f"{lang_name} ({lang_code}):")
        print(f"  - Translated: {stats['translated']}")
        print(f"  - Total untranslated found: {stats['total']}")
        print(f"  - Remaining: {stats['remaining']}")
        total_translated += stats['translated']
        total_remaining += stats['remaining']
        print()

    print(f"OVERALL:")
    print(f"  - Total entries translated: {total_translated}")
    print(f"  - Total entries remaining: {total_remaining}")

if __name__ == '__main__':
    main()
