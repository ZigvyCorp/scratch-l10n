#!/usr/bin/env python3
"""
Translate all remaining untranslated entries in scratch-l10n/editor/extensions/
for Spanish (es), Japanese (ja), Chinese (zh-cn), Polish (pl), and Vietnamese (vi).
"""

import json
import os
from pathlib import Path

# Translation dictionaries for each language
TRANSLATIONS = {
    'es': {
        # Common UI elements
        'blocks': 'bloques',
        'block': 'bloque',
        'reporter': 'reportero',
        'Boolean': 'Booleano',
        'hat': 'sombrero',
        'command': 'comando',

        # Music extension
        'music.categoryName': 'Música',
        'music.drumBass': '(2) Bombo',
        'music.drumBongo': '(13) Bongo',
        'music.drumCabasa': '(15) Cabasa',
        'music.drumClaves': '(9) Claves',
        'music.drumClosedHiHat': '(6) Charles Cerrado',
        'music.drumConga': '(14) Conga',
        'music.drumCowbell': '(11) Cencerro',
        'music.drumCrashCymbal': '(4) Platillo',
        'music.drumCuica': '(18) Cuica',
        'music.drumGuiro': '(16) Güiro',
        'music.drumHandClap': '(8) Aplauso',
        'music.drumOpenHiHat': '(5) Charles Abierto',
        'music.drumSideStick': '(3) Baqueta Lateral',
        'music.drumSnare': '(1) Caja',
        'music.drumTambourine': '(7) Pandereta',
        'music.drumTriangle': '(12) Triángulo',
        'music.drumVibraslap': '(17) Vibráfono',
        'music.drumWoodBlock': '(10) Bloque de Madera',

        # Pen extension
        'pen.categoryName': 'Lápiz',
        'pen.changeColorParam': 'cambiar [COLOR_PARAM] del lápiz por [VALUE]',
        'pen.changeHue': 'cambiar color de lápiz por [HUE]',
        'pen.changeShade': 'cambiar intensidad de lápiz por [SHADE]',
        'pen.changeSize': 'cambiar tamaño de lápiz por [SIZE]',
        'pen.clear': 'borrar todo',
        'pen.colorMenu.brightness': 'brillo',
        'pen.colorMenu.color': 'color',
        'pen.colorMenu.saturation': 'saturación',
        'pen.colorMenu.transparency': 'transparencia',
        'pen.penDown': 'bajar lápiz',
        'pen.penUp': 'subir lápiz',
        'pen.setColor': 'fijar color de lápiz a [COLOR]',
        'pen.setColorParam': 'fijar [COLOR_PARAM] del lápiz a [VALUE]',
        'pen.setHue': 'fijar color de lápiz a [HUE]',
        'pen.setShade': 'fijar intensidad de lápiz a [SHADE]',
        'pen.setSize': 'fijar tamaño de lápiz a [SIZE]',
        'pen.stamp': 'sellar',

        # Video Sensing extension
        'videoSensing.categoryName': 'Sensor de Video',
        'videoSensing.direction': 'dirección',
        'videoSensing.motion': 'movimiento',
        'videoSensing.off': 'apagado',
        'videoSensing.on': 'encendido',
        'videoSensing.onFlipped': 'encendido volteado',
        'videoSensing.setVideoTransparency': 'fijar transparencia de video a [TRANSPARENCY]',
        'videoSensing.sprite': 'objeto',
        'videoSensing.stage': 'escenario',
        'videoSensing.videoOn': '[ATTRIBUTE] de video en [SUBJECT]',
        'videoSensing.videoToggle': '[VIDEO_STATE] video',
        'videoSensing.whenMotionGreaterThan': 'cuando el movimiento del video > [REFERENCE]',

        # Text to Speech extension
        'text2speech.categoryName': 'Texto a Voz',
        'text2speech.defaultTextToSpeak': 'hola',
        'text2speech.alto': 'alto',
        'text2speech.giant': 'gigante',
        'text2speech.kitten': 'gatito',
        'text2speech.setVoiceBlock': 'fijar voz a [VOICE]',
        'text2speech.speakAndWaitBlock': 'decir [WORDS]',
        'text2speech.squeak': 'chillido',
        'text2speech.tenor': 'tenor',

        # Translate extension
        'translate.categoryName': 'Traducir',
        'translate.defaultTextToTranslate': 'hola',
        'translate.translateBlock': 'traducir [WORDS] a [LANGUAGE]',
        'translate.viewerLanguage': 'idioma',

        # Makey Makey extension
        'makeymakey.categoryName': 'Makey Makey',
        'makeymakey.downArrow': 'flecha abajo',
        'makeymakey.downArrowMenu': 'abajo',
        'makeymakey.leftArrow': 'flecha izquierda',
        'makeymakey.leftArrowMenu': 'izquierda',
        'makeymakey.rightArrow': 'flecha derecha',
        'makeymakey.rightArrowMenu': 'derecha',
        'makeymakey.spaceKey': 'espacio',
        'makeymakey.upArrow': 'flecha arriba',
        'makeymakey.upArrowMenu': 'arriba',
        'makeymakey.whenKeyPressed': 'cuando se presione [KEY]',
        'makeymakey.whenKeysPressedInOrder': 'cuando se presionen [SEQUENCE] en orden',

        # Micro:bit extension
        'microbit.categoryName': 'micro:bit',
        'microbit.clearDisplay': 'borrar pantalla',
        'microbit.defaultTextToDisplay': 'Hola!',
        'microbit.displaySymbol': 'mostrar [MATRIX]',
        'microbit.displayText': 'mostrar texto [TEXT]',
        'microbit.gesturesMenu.jumped': 'saltado',
        'microbit.gesturesMenu.moved': 'movido',
        'microbit.gesturesMenu.shaken': 'agitado',
        'microbit.isButtonPressed': '¿botón [BTN] presionado?',
        'microbit.isTilted': '¿inclinado [DIRECTION]?',
        'microbit.pinStateMenu.off': 'apagado',
        'microbit.pinStateMenu.on': 'encendido',
        'microbit.tiltAngle': 'ángulo de inclinación [DIRECTION]',
        'microbit.tiltDirectionMenu.any': 'cualquiera',
        'microbit.tiltDirectionMenu.back': 'atrás',
        'microbit.tiltDirectionMenu.front': 'adelante',
        'microbit.tiltDirectionMenu.left': 'izquierda',
        'microbit.tiltDirectionMenu.right': 'derecha',
        'microbit.whenButtonPressed': 'cuando se presione botón [BTN]',
        'microbit.whenGesture': 'cuando [GESTURE]',
        'microbit.whenPinConnected': 'cuando el pin [PIN] esté conectado',
        'microbit.whenTilted': 'cuando se incline [DIRECTION]',

        # EV3 extension
        'ev3.categoryName': 'EV3',
        'ev3.beepNote': 'sonar nota [NOTE] durante [TIME] segundos',
        'ev3.buttonPressed': '¿botón [PORT] presionado?',
        'ev3.getBrightness': 'brillo',
        'ev3.getDistance': 'distancia',
        'ev3.getMotorPosition': 'posición del motor [PORT]',
        'ev3.motorSetPower': 'motor [PORT] fijar potencia a [POWER]%',
        'ev3.motorTurnClockwise': 'motor [PORT] girar en sentido horario durante [TIME] segundos',
        'ev3.motorTurnCounterClockwise': 'motor [PORT] girar en sentido antihorario durante [TIME] segundos',
        'ev3.whenBrightnessLessThan': 'cuando el brillo < [DISTANCE]',
        'ev3.whenButtonPressed': 'cuando se presione el botón [PORT]',
        'ev3.whenDistanceLessThan': 'cuando la distancia < [DISTANCE]',

        # BOOST extension
        'boost.categoryName': 'BOOST',
        'boost.getMotorPosition': 'posición del motor [MOTOR_REPORTER_ID]',
        'boost.getTiltAngle': 'ángulo de inclinación [TILT_DIRECTION]',
        'boost.motorDirection.backward': 'en sentido antihorario',
        'boost.motorDirection.forward': 'en sentido horario',
        'boost.motorDirection.reverse': 'inverso',
        'boost.motorOff': 'apagar motor [MOTOR_ID]',
        'boost.motorOn': 'encender motor [MOTOR_ID]',
        'boost.motorOnFor': 'encender motor [MOTOR_ID] durante [DURATION] segundos',
        'boost.motorOnForRotation': 'encender motor [MOTOR_ID] para [ROTATION] rotaciones',
        'boost.seeingColor': '¿viendo el ladrillo [COLOR]?',
        'boost.setLightHue': 'fijar color de luz a [HUE]',
        'boost.setMotorDirection': 'fijar dirección del motor [MOTOR_ID] [MOTOR_DIRECTION]',
        'boost.setMotorPower': 'fijar potencia del motor [MOTOR_ID] a [POWER]%',
        'boost.whenColor': 'cuando el ladrillo es [COLOR]',
        'boost.whenTilted': 'cuando se incline [TILT_DIRECTION_ANY]',

        # WeDo 2.0 extension
        'wedo2.categoryName': 'WeDo 2.0',
        'wedo2.getDistance': 'distancia',
        'wedo2.getTiltAngle': 'ángulo de inclinación [TILT_DIRECTION]',
        'wedo2.isTilted': '¿inclinado [TILT_DIRECTION_ANY]?',
        'wedo2.motorDirection.backward': 'en sentido antihorario',
        'wedo2.motorDirection.forward': 'en sentido horario',
        'wedo2.motorDirection.reverse': 'inverso',
        'wedo2.motorId.a': 'motor A',
        'wedo2.motorId.all': 'todos los motores',
        'wedo2.motorId.b': 'motor B',
        'wedo2.motorId.default': 'motor',
        'wedo2.motorOff': 'apagar [MOTOR_ID]',
        'wedo2.motorOn': 'encender [MOTOR_ID]',
        'wedo2.motorOnFor': 'encender [MOTOR_ID] durante [DURATION] segundos',
        'wedo2.playNoteFor': 'tocar nota [NOTE] durante [DURATION] segundos',
        'wedo2.setLightHue': 'fijar color de luz a [HUE]',
        'wedo2.setMotorDirection': 'fijar dirección de [MOTOR_ID] [MOTOR_DIRECTION]',
        'wedo2.startMotorPower': 'fijar potencia de [MOTOR_ID] a [POWER]',
        'wedo2.whenDistance': 'cuando distancia [OP] [REFERENCE]',
        'wedo2.whenTilted': 'cuando se incline [TILT_DIRECTION_ANY]',
    },
    'ja': {
        # Common UI elements
        'blocks': 'ブロック',
        'block': 'ブロック',
        'reporter': 'レポーター',
        'Boolean': '真偽',
        'hat': 'ハット',
        'command': 'コマンド',

        # Music extension
        'music.categoryName': '音楽',
        'music.drumBass': '(2) バスドラム',
        'music.drumBongo': '(13) ボンゴ',
        'music.drumCabasa': '(15) カバサ',
        'music.drumClaves': '(9) クラベス',
        'music.drumClosedHiHat': '(6) クローズドハイハット',
        'music.drumConga': '(14) コンガ',
        'music.drumCowbell': '(11) カウベル',
        'music.drumCrashCymbal': '(4) クラッシュシンバル',
        'music.drumCuica': '(18) クイーカ',
        'music.drumGuiro': '(16) ギロ',
        'music.drumHandClap': '(8) ハンドクラップ',
        'music.drumOpenHiHat': '(5) オープンハイハット',
        'music.drumSideStick': '(3) サイドスティック',
        'music.drumSnare': '(1) スネアドラム',
        'music.drumTambourine': '(7) タンバリン',
        'music.drumTriangle': '(12) トライアングル',
        'music.drumVibraslap': '(17) ビブラスラップ',
        'music.drumWoodBlock': '(10) ウッドブロック',

        # Pen extension
        'pen.categoryName': 'ペン',
        'pen.changeColorParam': 'ペンの[COLOR_PARAM]を[VALUE]ずつ変える',
        'pen.changeHue': 'ペンの色を[HUE]ずつ変える',
        'pen.changeShade': 'ペンの濃さを[SHADE]ずつ変える',
        'pen.changeSize': 'ペンの太さを[SIZE]ずつ変える',
        'pen.clear': 'すべて消す',
        'pen.colorMenu.brightness': '明るさ',
        'pen.colorMenu.color': '色',
        'pen.colorMenu.saturation': '彩度',
        'pen.colorMenu.transparency': '透明度',
        'pen.penDown': 'ペンを下ろす',
        'pen.penUp': 'ペンを上げる',
        'pen.setColor': 'ペンの色を[COLOR]にする',
        'pen.setColorParam': 'ペンの[COLOR_PARAM]を[VALUE]にする',
        'pen.setHue': 'ペンの色を[HUE]にする',
        'pen.setShade': 'ペンの濃さを[SHADE]にする',
        'pen.setSize': 'ペンの太さを[SIZE]にする',
        'pen.stamp': 'スタンプ',

        # Video Sensing extension
        'videoSensing.categoryName': 'ビデオモーションセンサー',
        'videoSensing.direction': '向き',
        'videoSensing.motion': '動き',
        'videoSensing.off': 'オフ',
        'videoSensing.on': 'オン',
        'videoSensing.onFlipped': 'オン(反転)',
        'videoSensing.setVideoTransparency': 'ビデオの透明度を[TRANSPARENCY]にする',
        'videoSensing.sprite': 'スプライト',
        'videoSensing.stage': 'ステージ',
        'videoSensing.videoOn': '[SUBJECT]のビデオ[ATTRIBUTE]',
        'videoSensing.videoToggle': 'ビデオを[VIDEO_STATE]にする',
        'videoSensing.whenMotionGreaterThan': 'ビデオモーションが[REFERENCE]より大きいとき',

        # Text to Speech extension
        'text2speech.categoryName': '音声合成',
        'text2speech.defaultTextToSpeak': 'こんにちは',
        'text2speech.alto': 'アルト',
        'text2speech.giant': 'ジャイアント',
        'text2speech.kitten': '子猫',
        'text2speech.setVoiceBlock': '音声を[VOICE]にする',
        'text2speech.speakAndWaitBlock': '[WORDS]と話す',
        'text2speech.squeak': 'きしむ音',
        'text2speech.tenor': 'テノール',

        # Translate extension
        'translate.categoryName': '翻訳',
        'translate.defaultTextToTranslate': 'こんにちは',
        'translate.translateBlock': '[WORDS]を[LANGUAGE]に翻訳',
        'translate.viewerLanguage': '言語',

        # Makey Makey extension
        'makeymakey.categoryName': 'Makey Makey',
        'makeymakey.downArrow': '下矢印',
        'makeymakey.downArrowMenu': '下',
        'makeymakey.leftArrow': '左矢印',
        'makeymakey.leftArrowMenu': '左',
        'makeymakey.rightArrow': '右矢印',
        'makeymakey.rightArrowMenu': '右',
        'makeymakey.spaceKey': 'スペース',
        'makeymakey.upArrow': '上矢印',
        'makeymakey.upArrowMenu': '上',
        'makeymakey.whenKeyPressed': '[KEY]キーが押されたとき',
        'makeymakey.whenKeysPressedInOrder': '[SEQUENCE]が順番に押されたとき',

        # Micro:bit extension
        'microbit.categoryName': 'micro:bit',
        'microbit.clearDisplay': '画面を消す',
        'microbit.defaultTextToDisplay': 'こんにちは!',
        'microbit.displaySymbol': '[MATRIX]を表示する',
        'microbit.displayText': 'テキスト[TEXT]を表示する',
        'microbit.gesturesMenu.jumped': '跳ねた',
        'microbit.gesturesMenu.moved': '動いた',
        'microbit.gesturesMenu.shaken': '振られた',
        'microbit.isButtonPressed': 'ボタン[BTN]が押されている',
        'microbit.isTilted': '[DIRECTION]に傾いている',
        'microbit.pinStateMenu.off': 'オフ',
        'microbit.pinStateMenu.on': 'オン',
        'microbit.tiltAngle': '[DIRECTION]の傾き角度',
        'microbit.tiltDirectionMenu.any': 'どれか',
        'microbit.tiltDirectionMenu.back': '後ろ',
        'microbit.tiltDirectionMenu.front': '前',
        'microbit.tiltDirectionMenu.left': '左',
        'microbit.tiltDirectionMenu.right': '右',
        'microbit.whenButtonPressed': 'ボタン[BTN]が押されたとき',
        'microbit.whenGesture': '[GESTURE]とき',
        'microbit.whenPinConnected': 'ピン[PIN]が接続されたとき',
        'microbit.whenTilted': '[DIRECTION]に傾いたとき',

        # EV3 extension
        'ev3.categoryName': 'EV3',
        'ev3.beepNote': '[NOTE]の音を[TIME]秒鳴らす',
        'ev3.buttonPressed': 'ボタン[PORT]が押されている',
        'ev3.getBrightness': '明るさ',
        'ev3.getDistance': '距離',
        'ev3.getMotorPosition': 'モーター[PORT]の位置',
        'ev3.motorSetPower': 'モーター[PORT]のパワーを[POWER]%にする',
        'ev3.motorTurnClockwise': 'モーター[PORT]を時計回りに[TIME]秒回す',
        'ev3.motorTurnCounterClockwise': 'モーター[PORT]を反時計回りに[TIME]秒回す',
        'ev3.whenBrightnessLessThan': '明るさが[DISTANCE]より小さいとき',
        'ev3.whenButtonPressed': 'ボタン[PORT]が押されたとき',
        'ev3.whenDistanceLessThan': '距離が[DISTANCE]より小さいとき',

        # BOOST extension
        'boost.categoryName': 'BOOST',
        'boost.getMotorPosition': 'モーター[MOTOR_REPORTER_ID]の位置',
        'boost.getTiltAngle': '[TILT_DIRECTION]の傾き角度',
        'boost.motorDirection.backward': '反時計回り',
        'boost.motorDirection.forward': '時計回り',
        'boost.motorDirection.reverse': '逆',
        'boost.motorOff': 'モーター[MOTOR_ID]をオフにする',
        'boost.motorOn': 'モーター[MOTOR_ID]をオンにする',
        'boost.motorOnFor': 'モーター[MOTOR_ID]を[DURATION]秒オンにする',
        'boost.motorOnForRotation': 'モーター[MOTOR_ID]を[ROTATION]回転させる',
        'boost.seeingColor': 'ブロック[COLOR]を見ている',
        'boost.setLightHue': 'ライトの色を[HUE]にする',
        'boost.setMotorDirection': 'モーター[MOTOR_ID]の方向を[MOTOR_DIRECTION]にする',
        'boost.setMotorPower': 'モーター[MOTOR_ID]のパワーを[POWER]%にする',
        'boost.whenColor': 'ブロックが[COLOR]のとき',
        'boost.whenTilted': '[TILT_DIRECTION_ANY]に傾いたとき',

        # WeDo 2.0 extension
        'wedo2.categoryName': 'WeDo 2.0',
        'wedo2.getDistance': '距離',
        'wedo2.getTiltAngle': '[TILT_DIRECTION]の傾き角度',
        'wedo2.isTilted': '[TILT_DIRECTION_ANY]に傾いている',
        'wedo2.motorDirection.backward': '反時計回り',
        'wedo2.motorDirection.forward': '時計回り',
        'wedo2.motorDirection.reverse': '逆',
        'wedo2.motorId.a': 'モーターA',
        'wedo2.motorId.all': 'すべてのモーター',
        'wedo2.motorId.b': 'モーターB',
        'wedo2.motorId.default': 'モーター',
        'wedo2.motorOff': '[MOTOR_ID]をオフにする',
        'wedo2.motorOn': '[MOTOR_ID]をオンにする',
        'wedo2.motorOnFor': '[MOTOR_ID]を[DURATION]秒オンにする',
        'wedo2.playNoteFor': '[NOTE]の音を[DURATION]秒演奏する',
        'wedo2.setLightHue': 'ライトの色を[HUE]にする',
        'wedo2.setMotorDirection': '[MOTOR_ID]の方向を[MOTOR_DIRECTION]にする',
        'wedo2.startMotorPower': '[MOTOR_ID]のパワーを[POWER]にする',
        'wedo2.whenDistance': '距離が[REFERENCE][OP]のとき',
        'wedo2.whenTilted': '[TILT_DIRECTION_ANY]に傾いたとき',
    },
    'zh-cn': {
        # Common UI elements
        'blocks': '积木',
        'block': '积木',
        'reporter': '报告',
        'Boolean': '布尔',
        'hat': '帽子',
        'command': '命令',

        # Music extension
        'music.categoryName': '音乐',
        'music.drumBass': '(2) 低音鼓',
        'music.drumBongo': '(13) 邦戈鼓',
        'music.drumCabasa': '(15) 卡巴萨',
        'music.drumClaves': '(9) 音棒',
        'music.drumClosedHiHat': '(6) 闭镲',
        'music.drumConga': '(14) 康加鼓',
        'music.drumCowbell': '(11) 牛铃',
        'music.drumCrashCymbal': '(4) 碎音钹',
        'music.drumCuica': '(18) 锯加鼓',
        'music.drumGuiro': '(16) 刮葫',
        'music.drumHandClap': '(8) 拍手',
        'music.drumOpenHiHat': '(5) 开镲',
        'music.drumSideStick': '(3) 敲鼓边',
        'music.drumSnare': '(1) 小鼓',
        'music.drumTambourine': '(7) 铃鼓',
        'music.drumTriangle': '(12) 三角铁',
        'music.drumVibraslap': '(17) 颤音器',
        'music.drumWoodBlock': '(10) 木鱼',

        # Pen extension
        'pen.categoryName': '画笔',
        'pen.changeColorParam': '将画笔的[COLOR_PARAM]增加[VALUE]',
        'pen.changeHue': '将画笔颜色增加[HUE]',
        'pen.changeShade': '将画笔亮度增加[SHADE]',
        'pen.changeSize': '将画笔粗细增加[SIZE]',
        'pen.clear': '全部擦除',
        'pen.colorMenu.brightness': '亮度',
        'pen.colorMenu.color': '颜色',
        'pen.colorMenu.saturation': '饱和度',
        'pen.colorMenu.transparency': '透明度',
        'pen.penDown': '落笔',
        'pen.penUp': '抬笔',
        'pen.setColor': '将画笔颜色设为[COLOR]',
        'pen.setColorParam': '将画笔的[COLOR_PARAM]设为[VALUE]',
        'pen.setHue': '将画笔颜色设为[HUE]',
        'pen.setShade': '将画笔亮度设为[SHADE]',
        'pen.setSize': '将画笔粗细设为[SIZE]',
        'pen.stamp': '图章',

        # Video Sensing extension
        'videoSensing.categoryName': '视频侦测',
        'videoSensing.direction': '方向',
        'videoSensing.motion': '运动',
        'videoSensing.off': '关闭',
        'videoSensing.on': '开启',
        'videoSensing.onFlipped': '开启并左右翻转',
        'videoSensing.setVideoTransparency': '将视频透明度设为[TRANSPARENCY]',
        'videoSensing.sprite': '角色',
        'videoSensing.stage': '舞台',
        'videoSensing.videoOn': '视频在[SUBJECT]上的[ATTRIBUTE]',
        'videoSensing.videoToggle': '[VIDEO_STATE]摄像头',
        'videoSensing.whenMotionGreaterThan': '当视频运动 > [REFERENCE]',

        # Text to Speech extension
        'text2speech.categoryName': '文字朗读',
        'text2speech.defaultTextToSpeak': '你好',
        'text2speech.alto': '中音',
        'text2speech.giant': '巨人',
        'text2speech.kitten': '小猫',
        'text2speech.setVoiceBlock': '将语音设为[VOICE]',
        'text2speech.speakAndWaitBlock': '朗读[WORDS]',
        'text2speech.squeak': '尖叫',
        'text2speech.tenor': '男高音',

        # Translate extension
        'translate.categoryName': '翻译',
        'translate.defaultTextToTranslate': '你好',
        'translate.translateBlock': '将[WORDS]翻译成[LANGUAGE]',
        'translate.viewerLanguage': '语言',

        # Makey Makey extension
        'makeymakey.categoryName': 'Makey Makey',
        'makeymakey.downArrow': '下箭头',
        'makeymakey.downArrowMenu': '下',
        'makeymakey.leftArrow': '左箭头',
        'makeymakey.leftArrowMenu': '左',
        'makeymakey.rightArrow': '右箭头',
        'makeymakey.rightArrowMenu': '右',
        'makeymakey.spaceKey': '空格',
        'makeymakey.upArrow': '上箭头',
        'makeymakey.upArrowMenu': '上',
        'makeymakey.whenKeyPressed': '当按下[KEY]键',
        'makeymakey.whenKeysPressedInOrder': '当按下[SEQUENCE]的顺序',

        # Micro:bit extension
        'microbit.categoryName': 'micro:bit',
        'microbit.clearDisplay': '清空显示',
        'microbit.defaultTextToDisplay': '你好!',
        'microbit.displaySymbol': '显示[MATRIX]',
        'microbit.displayText': '显示文字[TEXT]',
        'microbit.gesturesMenu.jumped': '跳',
        'microbit.gesturesMenu.moved': '移动',
        'microbit.gesturesMenu.shaken': '摇晃',
        'microbit.isButtonPressed': '按钮[BTN]被按下?',
        'microbit.isTilted': '向[DIRECTION]倾斜?',
        'microbit.pinStateMenu.off': '关闭',
        'microbit.pinStateMenu.on': '开启',
        'microbit.tiltAngle': '[DIRECTION]倾斜角度',
        'microbit.tiltDirectionMenu.any': '任意',
        'microbit.tiltDirectionMenu.back': '后',
        'microbit.tiltDirectionMenu.front': '前',
        'microbit.tiltDirectionMenu.left': '左',
        'microbit.tiltDirectionMenu.right': '右',
        'microbit.whenButtonPressed': '当按钮[BTN]被按下',
        'microbit.whenGesture': '当[GESTURE]',
        'microbit.whenPinConnected': '当引脚[PIN]连接',
        'microbit.whenTilted': '当向[DIRECTION]倾斜',

        # EV3 extension
        'ev3.categoryName': 'EV3',
        'ev3.beepNote': '播放音符[NOTE] [TIME]秒',
        'ev3.buttonPressed': '按钮[PORT]被按下?',
        'ev3.getBrightness': '亮度',
        'ev3.getDistance': '距离',
        'ev3.getMotorPosition': '马达[PORT]位置',
        'ev3.motorSetPower': '将马达[PORT]功率设为[POWER]%',
        'ev3.motorTurnClockwise': '马达[PORT]顺时针转[TIME]秒',
        'ev3.motorTurnCounterClockwise': '马达[PORT]逆时针转[TIME]秒',
        'ev3.whenBrightnessLessThan': '当亮度 < [DISTANCE]',
        'ev3.whenButtonPressed': '当按钮[PORT]被按下',
        'ev3.whenDistanceLessThan': '当距离 < [DISTANCE]',

        # BOOST extension
        'boost.categoryName': 'BOOST',
        'boost.getMotorPosition': '马达[MOTOR_REPORTER_ID]位置',
        'boost.getTiltAngle': '[TILT_DIRECTION]倾斜角度',
        'boost.motorDirection.backward': '逆时针',
        'boost.motorDirection.forward': '顺时针',
        'boost.motorDirection.reverse': '反向',
        'boost.motorOff': '关闭马达[MOTOR_ID]',
        'boost.motorOn': '开启马达[MOTOR_ID]',
        'boost.motorOnFor': '开启马达[MOTOR_ID] [DURATION]秒',
        'boost.motorOnForRotation': '马达[MOTOR_ID]转[ROTATION]圈',
        'boost.seeingColor': '看到积木[COLOR]?',
        'boost.setLightHue': '将灯光颜色设为[HUE]',
        'boost.setMotorDirection': '将马达[MOTOR_ID]方向设为[MOTOR_DIRECTION]',
        'boost.setMotorPower': '将马达[MOTOR_ID]功率设为[POWER]%',
        'boost.whenColor': '当积木是[COLOR]',
        'boost.whenTilted': '当向[TILT_DIRECTION_ANY]倾斜',

        # WeDo 2.0 extension
        'wedo2.categoryName': 'WeDo 2.0',
        'wedo2.getDistance': '距离',
        'wedo2.getTiltAngle': '[TILT_DIRECTION]倾斜角度',
        'wedo2.isTilted': '向[TILT_DIRECTION_ANY]倾斜?',
        'wedo2.motorDirection.backward': '逆时针',
        'wedo2.motorDirection.forward': '顺时针',
        'wedo2.motorDirection.reverse': '反向',
        'wedo2.motorId.a': '马达 A',
        'wedo2.motorId.all': '所有马达',
        'wedo2.motorId.b': '马达 B',
        'wedo2.motorId.default': '马达',
        'wedo2.motorOff': '关闭[MOTOR_ID]',
        'wedo2.motorOn': '开启[MOTOR_ID]',
        'wedo2.motorOnFor': '开启[MOTOR_ID] [DURATION]秒',
        'wedo2.playNoteFor': '演奏音符[NOTE] [DURATION]秒',
        'wedo2.setLightHue': '将灯光颜色设为[HUE]',
        'wedo2.setMotorDirection': '将[MOTOR_ID]方向设为[MOTOR_DIRECTION]',
        'wedo2.startMotorPower': '将[MOTOR_ID]功率设为[POWER]',
        'wedo2.whenDistance': '当距离[OP] [REFERENCE]',
        'wedo2.whenTilted': '当向[TILT_DIRECTION_ANY]倾斜',
    },
    'pl': {
        # Common UI elements
        'blocks': 'bloki',
        'block': 'blok',
        'reporter': 'reporter',
        'Boolean': 'wartość logiczna',
        'hat': 'kapelusz',
        'command': 'polecenie',

        # Music extension
        'music.categoryName': 'Muzyka',
        'music.drumBass': '(2) Bęben basowy',
        'music.drumBongo': '(13) Bongo',
        'music.drumCabasa': '(15) Kabasa',
        'music.drumClaves': '(9) Klawy',
        'music.drumClosedHiHat': '(6) Zamknięty hi-hat',
        'music.drumConga': '(14) Konga',
        'music.drumCowbell': '(11) Dzwonek krowi',
        'music.drumCrashCymbal': '(4) Talerz crash',
        'music.drumCuica': '(18) Kuika',
        'music.drumGuiro': '(16) Guiro',
        'music.drumHandClap': '(8) Klasnięcie',
        'music.drumOpenHiHat': '(5) Otwarty hi-hat',
        'music.drumSideStick': '(3) Pałka boczna',
        'music.drumSnare': '(1) Werbel',
        'music.drumTambourine': '(7) Tamburyn',
        'music.drumTriangle': '(12) Trójkąt',
        'music.drumVibraslap': '(17) Vibraslap',
        'music.drumWoodBlock': '(10) Blok drewniany',

        # Pen extension
        'pen.categoryName': 'Pisak',
        'pen.changeColorParam': 'zmień [COLOR_PARAM] pisaka o [VALUE]',
        'pen.changeHue': 'zmień kolor pisaka o [HUE]',
        'pen.changeShade': 'zmień ciemność pisaka o [SHADE]',
        'pen.changeSize': 'zmień rozmiar pisaka o [SIZE]',
        'pen.clear': 'wyczyść wszystko',
        'pen.colorMenu.brightness': 'jasność',
        'pen.colorMenu.color': 'kolor',
        'pen.colorMenu.saturation': 'nasycenie',
        'pen.colorMenu.transparency': 'przezroczystość',
        'pen.penDown': 'przyłóż pisak',
        'pen.penUp': 'podnieś pisak',
        'pen.setColor': 'ustaw kolor pisaka na [COLOR]',
        'pen.setColorParam': 'ustaw [COLOR_PARAM] pisaka na [VALUE]',
        'pen.setHue': 'ustaw kolor pisaka na [HUE]',
        'pen.setShade': 'ustaw ciemność pisaka na [SHADE]',
        'pen.setSize': 'ustaw rozmiar pisaka na [SIZE]',
        'pen.stamp': 'stempluj',

        # Video Sensing extension
        'videoSensing.categoryName': 'Czujnik wideo',
        'videoSensing.direction': 'kierunek',
        'videoSensing.motion': 'ruch',
        'videoSensing.off': 'wyłącz',
        'videoSensing.on': 'włącz',
        'videoSensing.onFlipped': 'włącz odwrócone',
        'videoSensing.setVideoTransparency': 'ustaw przezroczystość wideo na [TRANSPARENCY]',
        'videoSensing.sprite': 'duszek',
        'videoSensing.stage': 'scena',
        'videoSensing.videoOn': '[ATTRIBUTE] wideo na [SUBJECT]',
        'videoSensing.videoToggle': '[VIDEO_STATE] wideo',
        'videoSensing.whenMotionGreaterThan': 'kiedy ruch wideo > [REFERENCE]',

        # Text to Speech extension
        'text2speech.categoryName': 'Zamiana tekstu na mowę',
        'text2speech.defaultTextToSpeak': 'cześć',
        'text2speech.alto': 'alt',
        'text2speech.giant': 'gigant',
        'text2speech.kitten': 'kociak',
        'text2speech.setVoiceBlock': 'ustaw głos na [VOICE]',
        'text2speech.speakAndWaitBlock': 'powiedz [WORDS]',
        'text2speech.squeak': 'pisk',
        'text2speech.tenor': 'tenor',

        # Translate extension
        'translate.categoryName': 'Tłumacz',
        'translate.defaultTextToTranslate': 'cześć',
        'translate.translateBlock': 'przetłumacz [WORDS] na [LANGUAGE]',
        'translate.viewerLanguage': 'język',

        # Makey Makey extension
        'makeymakey.categoryName': 'Makey Makey',
        'makeymakey.downArrow': 'strzałka w dół',
        'makeymakey.downArrowMenu': 'dół',
        'makeymakey.leftArrow': 'strzałka w lewo',
        'makeymakey.leftArrowMenu': 'lewo',
        'makeymakey.rightArrow': 'strzałka w prawo',
        'makeymakey.rightArrowMenu': 'prawo',
        'makeymakey.spaceKey': 'spacja',
        'makeymakey.upArrow': 'strzałka w górę',
        'makeymakey.upArrowMenu': 'góra',
        'makeymakey.whenKeyPressed': 'kiedy klawisz [KEY] naciśnięty',
        'makeymakey.whenKeysPressedInOrder': 'kiedy klawisze [SEQUENCE] naciśnięte po kolei',

        # Micro:bit extension
        'microbit.categoryName': 'micro:bit',
        'microbit.clearDisplay': 'wyczyść wyświetlacz',
        'microbit.defaultTextToDisplay': 'Cześć!',
        'microbit.displaySymbol': 'wyświetl [MATRIX]',
        'microbit.displayText': 'wyświetl tekst [TEXT]',
        'microbit.gesturesMenu.jumped': 'skok',
        'microbit.gesturesMenu.moved': 'ruch',
        'microbit.gesturesMenu.shaken': 'potrząśnięcie',
        'microbit.isButtonPressed': 'przycisk [BTN] naciśnięty?',
        'microbit.isTilted': 'przechylony [DIRECTION]?',
        'microbit.pinStateMenu.off': 'wyłączony',
        'microbit.pinStateMenu.on': 'włączony',
        'microbit.tiltAngle': 'kąt przechylenia [DIRECTION]',
        'microbit.tiltDirectionMenu.any': 'dowolny',
        'microbit.tiltDirectionMenu.back': 'tył',
        'microbit.tiltDirectionMenu.front': 'przód',
        'microbit.tiltDirectionMenu.left': 'lewo',
        'microbit.tiltDirectionMenu.right': 'prawo',
        'microbit.whenButtonPressed': 'kiedy przycisk [BTN] naciśnięty',
        'microbit.whenGesture': 'kiedy [GESTURE]',
        'microbit.whenPinConnected': 'kiedy pin [PIN] podłączony',
        'microbit.whenTilted': 'kiedy przechylony [DIRECTION]',

        # EV3 extension
        'ev3.categoryName': 'EV3',
        'ev3.beepNote': 'zagraj nutę [NOTE] przez [TIME] sekund',
        'ev3.buttonPressed': 'przycisk [PORT] naciśnięty?',
        'ev3.getBrightness': 'jasność',
        'ev3.getDistance': 'odległość',
        'ev3.getMotorPosition': 'pozycja silnika [PORT]',
        'ev3.motorSetPower': 'ustaw moc silnika [PORT] na [POWER]%',
        'ev3.motorTurnClockwise': 'obróć silnik [PORT] zgodnie z ruchem wskazówek zegara przez [TIME] sekund',
        'ev3.motorTurnCounterClockwise': 'obróć silnik [PORT] przeciwnie do ruchu wskazówek zegara przez [TIME] sekund',
        'ev3.whenBrightnessLessThan': 'kiedy jasność < [DISTANCE]',
        'ev3.whenButtonPressed': 'kiedy przycisk [PORT] naciśnięty',
        'ev3.whenDistanceLessThan': 'kiedy odległość < [DISTANCE]',

        # BOOST extension
        'boost.categoryName': 'BOOST',
        'boost.getMotorPosition': 'pozycja silnika [MOTOR_REPORTER_ID]',
        'boost.getTiltAngle': 'kąt przechylenia [TILT_DIRECTION]',
        'boost.motorDirection.backward': 'przeciwnie do ruchu wskazówek zegara',
        'boost.motorDirection.forward': 'zgodnie z ruchem wskazówek zegara',
        'boost.motorDirection.reverse': 'odwrotnie',
        'boost.motorOff': 'wyłącz silnik [MOTOR_ID]',
        'boost.motorOn': 'włącz silnik [MOTOR_ID]',
        'boost.motorOnFor': 'włącz silnik [MOTOR_ID] na [DURATION] sekund',
        'boost.motorOnForRotation': 'włącz silnik [MOTOR_ID] na [ROTATION] obrotów',
        'boost.seeingColor': 'widzisz klocek [COLOR]?',
        'boost.setLightHue': 'ustaw kolor światła na [HUE]',
        'boost.setMotorDirection': 'ustaw kierunek silnika [MOTOR_ID] [MOTOR_DIRECTION]',
        'boost.setMotorPower': 'ustaw moc silnika [MOTOR_ID] na [POWER]%',
        'boost.whenColor': 'kiedy klocek jest [COLOR]',
        'boost.whenTilted': 'kiedy przechylony [TILT_DIRECTION_ANY]',

        # WeDo 2.0 extension
        'wedo2.categoryName': 'WeDo 2.0',
        'wedo2.getDistance': 'odległość',
        'wedo2.getTiltAngle': 'kąt przechylenia [TILT_DIRECTION]',
        'wedo2.isTilted': 'przechylony [TILT_DIRECTION_ANY]?',
        'wedo2.motorDirection.backward': 'przeciwnie do ruchu wskazówek zegara',
        'wedo2.motorDirection.forward': 'zgodnie z ruchem wskazówek zegara',
        'wedo2.motorDirection.reverse': 'odwrotnie',
        'wedo2.motorId.a': 'silnik A',
        'wedo2.motorId.all': 'wszystkie silniki',
        'wedo2.motorId.b': 'silnik B',
        'wedo2.motorId.default': 'silnik',
        'wedo2.motorOff': 'wyłącz [MOTOR_ID]',
        'wedo2.motorOn': 'włącz [MOTOR_ID]',
        'wedo2.motorOnFor': 'włącz [MOTOR_ID] na [DURATION] sekund',
        'wedo2.playNoteFor': 'zagraj nutę [NOTE] przez [DURATION] sekund',
        'wedo2.setLightHue': 'ustaw kolor światła na [HUE]',
        'wedo2.setMotorDirection': 'ustaw kierunek [MOTOR_ID] [MOTOR_DIRECTION]',
        'wedo2.startMotorPower': 'ustaw moc [MOTOR_ID] na [POWER]',
        'wedo2.whenDistance': 'kiedy odległość [OP] [REFERENCE]',
        'wedo2.whenTilted': 'kiedy przechylony [TILT_DIRECTION_ANY]',
    },
    'vi': {
        # Common UI elements
        'blocks': 'khối lệnh',
        'block': 'khối',
        'reporter': 'báo cáo',
        'Boolean': 'luận lý',
        'hat': 'mũ',
        'command': 'lệnh',

        # Music extension
        'music.categoryName': 'Âm nhạc',
        'music.drumBass': '(2) Trống bass',
        'music.drumBongo': '(13) Trống bongo',
        'music.drumCabasa': '(15) Cabasa',
        'music.drumClaves': '(9) Claves',
        'music.drumClosedHiHat': '(6) Hi-hat đóng',
        'music.drumConga': '(14) Trống conga',
        'music.drumCowbell': '(11) Chuông bò',
        'music.drumCrashCymbal': '(4) Chũm chọe crash',
        'music.drumCuica': '(18) Cuica',
        'music.drumGuiro': '(16) Guiro',
        'music.drumHandClap': '(8) Vỗ tay',
        'music.drumOpenHiHat': '(5) Hi-hat mở',
        'music.drumSideStick': '(3) Gõ mép trống',
        'music.drumSnare': '(1) Trống snare',
        'music.drumTambourine': '(7) Trống lắc',
        'music.drumTriangle': '(12) Tam giác',
        'music.drumVibraslap': '(17) Vibraslap',
        'music.drumWoodBlock': '(10) Mõ',

        # Pen extension
        'pen.categoryName': 'Bút',
        'pen.changeColorParam': 'thay đổi [COLOR_PARAM] bút thêm [VALUE]',
        'pen.changeHue': 'thay đổi màu bút thêm [HUE]',
        'pen.changeShade': 'thay đổi độ sáng bút thêm [SHADE]',
        'pen.changeSize': 'thay đổi kích thước bút thêm [SIZE]',
        'pen.clear': 'xóa tất cả',
        'pen.colorMenu.brightness': 'độ sáng',
        'pen.colorMenu.color': 'màu',
        'pen.colorMenu.saturation': 'độ bão hòa',
        'pen.colorMenu.transparency': 'độ trong suốt',
        'pen.penDown': 'hạ bút',
        'pen.penUp': 'nhấc bút',
        'pen.setColor': 'đặt màu bút thành [COLOR]',
        'pen.setColorParam': 'đặt [COLOR_PARAM] bút thành [VALUE]',
        'pen.setHue': 'đặt màu bút thành [HUE]',
        'pen.setShade': 'đặt độ sáng bút thành [SHADE]',
        'pen.setSize': 'đặt kích thước bút thành [SIZE]',
        'pen.stamp': 'đóng dấu',

        # Video Sensing extension
        'videoSensing.categoryName': 'Cảm biến Video',
        'videoSensing.direction': 'hướng',
        'videoSensing.motion': 'chuyển động',
        'videoSensing.off': 'tắt',
        'videoSensing.on': 'bật',
        'videoSensing.onFlipped': 'bật lật ngược',
        'videoSensing.setVideoTransparency': 'đặt độ trong suốt video thành [TRANSPARENCY]',
        'videoSensing.sprite': 'nhân vật',
        'videoSensing.stage': 'sân khấu',
        'videoSensing.videoOn': '[ATTRIBUTE] video trên [SUBJECT]',
        'videoSensing.videoToggle': '[VIDEO_STATE] video',
        'videoSensing.whenMotionGreaterThan': 'khi chuyển động video > [REFERENCE]',

        # Text to Speech extension
        'text2speech.categoryName': 'Chuyển văn bản thành giọng nói',
        'text2speech.defaultTextToSpeak': 'xin chào',
        'text2speech.alto': 'alto',
        'text2speech.giant': 'khổng lồ',
        'text2speech.kitten': 'mèo con',
        'text2speech.setVoiceBlock': 'đặt giọng nói thành [VOICE]',
        'text2speech.speakAndWaitBlock': 'nói [WORDS]',
        'text2speech.squeak': 'tiếng kêu',
        'text2speech.tenor': 'tenor',

        # Translate extension
        'translate.categoryName': 'Dịch',
        'translate.defaultTextToTranslate': 'xin chào',
        'translate.translateBlock': 'dịch [WORDS] sang [LANGUAGE]',
        'translate.viewerLanguage': 'ngôn ngữ',

        # Makey Makey extension
        'makeymakey.categoryName': 'Makey Makey',
        'makeymakey.downArrow': 'mũi tên xuống',
        'makeymakey.downArrowMenu': 'xuống',
        'makeymakey.leftArrow': 'mũi tên trái',
        'makeymakey.leftArrowMenu': 'trái',
        'makeymakey.rightArrow': 'mũi tên phải',
        'makeymakey.rightArrowMenu': 'phải',
        'makeymakey.spaceKey': 'phím cách',
        'makeymakey.upArrow': 'mũi tên lên',
        'makeymakey.upArrowMenu': 'lên',
        'makeymakey.whenKeyPressed': 'khi phím [KEY] được nhấn',
        'makeymakey.whenKeysPressedInOrder': 'khi phím [SEQUENCE] được nhấn theo thứ tự',

        # Micro:bit extension
        'microbit.categoryName': 'micro:bit',
        'microbit.clearDisplay': 'xóa màn hình',
        'microbit.defaultTextToDisplay': 'Xin chào!',
        'microbit.displaySymbol': 'hiển thị [MATRIX]',
        'microbit.displayText': 'hiển thị văn bản [TEXT]',
        'microbit.gesturesMenu.jumped': 'nhảy',
        'microbit.gesturesMenu.moved': 'di chuyển',
        'microbit.gesturesMenu.shaken': 'lắc',
        'microbit.isButtonPressed': 'nút [BTN] được nhấn?',
        'microbit.isTilted': 'nghiêng [DIRECTION]?',
        'microbit.pinStateMenu.off': 'tắt',
        'microbit.pinStateMenu.on': 'bật',
        'microbit.tiltAngle': 'góc nghiêng [DIRECTION]',
        'microbit.tiltDirectionMenu.any': 'bất kỳ',
        'microbit.tiltDirectionMenu.back': 'sau',
        'microbit.tiltDirectionMenu.front': 'trước',
        'microbit.tiltDirectionMenu.left': 'trái',
        'microbit.tiltDirectionMenu.right': 'phải',
        'microbit.whenButtonPressed': 'khi nút [BTN] được nhấn',
        'microbit.whenGesture': 'khi [GESTURE]',
        'microbit.whenPinConnected': 'khi chân [PIN] được kết nối',
        'microbit.whenTilted': 'khi nghiêng [DIRECTION]',

        # EV3 extension
        'ev3.categoryName': 'EV3',
        'ev3.beepNote': 'phát nốt nhạc [NOTE] trong [TIME] giây',
        'ev3.buttonPressed': 'nút [PORT] được nhấn?',
        'ev3.getBrightness': 'độ sáng',
        'ev3.getDistance': 'khoảng cách',
        'ev3.getMotorPosition': 'vị trí động cơ [PORT]',
        'ev3.motorSetPower': 'đặt công suất động cơ [PORT] thành [POWER]%',
        'ev3.motorTurnClockwise': 'quay động cơ [PORT] theo chiều kim đồng hồ trong [TIME] giây',
        'ev3.motorTurnCounterClockwise': 'quay động cơ [PORT] ngược chiều kim đồng hồ trong [TIME] giây',
        'ev3.whenBrightnessLessThan': 'khi độ sáng < [DISTANCE]',
        'ev3.whenButtonPressed': 'khi nút [PORT] được nhấn',
        'ev3.whenDistanceLessThan': 'khi khoảng cách < [DISTANCE]',

        # BOOST extension
        'boost.categoryName': 'BOOST',
        'boost.getMotorPosition': 'vị trí động cơ [MOTOR_REPORTER_ID]',
        'boost.getTiltAngle': 'góc nghiêng [TILT_DIRECTION]',
        'boost.motorDirection.backward': 'ngược chiều kim đồng hồ',
        'boost.motorDirection.forward': 'theo chiều kim đồng hồ',
        'boost.motorDirection.reverse': 'đảo ngược',
        'boost.motorOff': 'tắt động cơ [MOTOR_ID]',
        'boost.motorOn': 'bật động cơ [MOTOR_ID]',
        'boost.motorOnFor': 'bật động cơ [MOTOR_ID] trong [DURATION] giây',
        'boost.motorOnForRotation': 'bật động cơ [MOTOR_ID] cho [ROTATION] vòng quay',
        'boost.seeingColor': 'nhìn thấy khối [COLOR]?',
        'boost.setLightHue': 'đặt màu đèn thành [HUE]',
        'boost.setMotorDirection': 'đặt hướng động cơ [MOTOR_ID] [MOTOR_DIRECTION]',
        'boost.setMotorPower': 'đặt công suất động cơ [MOTOR_ID] thành [POWER]%',
        'boost.whenColor': 'khi khối là [COLOR]',
        'boost.whenTilted': 'khi nghiêng [TILT_DIRECTION_ANY]',

        # WeDo 2.0 extension
        'wedo2.categoryName': 'WeDo 2.0',
        'wedo2.getDistance': 'khoảng cách',
        'wedo2.getTiltAngle': 'góc nghiêng [TILT_DIRECTION]',
        'wedo2.isTilted': 'nghiêng [TILT_DIRECTION_ANY]?',
        'wedo2.motorDirection.backward': 'ngược chiều kim đồng hồ',
        'wedo2.motorDirection.forward': 'theo chiều kim đồng hồ',
        'wedo2.motorDirection.reverse': 'đảo ngược',
        'wedo2.motorId.a': 'động cơ A',
        'wedo2.motorId.all': 'tất cả động cơ',
        'wedo2.motorId.b': 'động cơ B',
        'wedo2.motorId.default': 'động cơ',
        'wedo2.motorOff': 'tắt [MOTOR_ID]',
        'wedo2.motorOn': 'bật [MOTOR_ID]',
        'wedo2.motorOnFor': 'bật [MOTOR_ID] trong [DURATION] giây',
        'wedo2.playNoteFor': 'chơi nốt nhạc [NOTE] trong [DURATION] giây',
        'wedo2.setLightHue': 'đặt màu đèn thành [HUE]',
        'wedo2.setMotorDirection': 'đặt hướng [MOTOR_ID] [MOTOR_DIRECTION]',
        'wedo2.startMotorPower': 'đặt công suất [MOTOR_ID] thành [POWER]',
        'wedo2.whenDistance': 'khi khoảng cách [OP] [REFERENCE]',
        'wedo2.whenTilted': 'khi nghiêng [TILT_DIRECTION_ANY]',
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
        f.write('\n')  # Add final newline

def find_untranslated(en_data, target_data):
    """Find entries that are empty or still in English"""
    untranslated = []
    for key, en_value in en_data.items():
        target_value = target_data.get(key, '')
        # Consider untranslated if empty or same as English
        if not target_value or target_value == en_value:
            untranslated.append(key)
    return untranslated

def translate_entry(key, en_value, lang_code, translations):
    """Translate a single entry"""
    # Check if we have a direct translation
    if key in translations:
        return translations[key]

    # If no direct translation, return the English value
    # (in a real scenario, you'd call a translation API)
    return en_value

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
            summary[lang_code] = {'translated': 0, 'total': len(en_data)}
            continue

        # Translate entries
        translations_dict = TRANSLATIONS.get(lang_code, {})
        translated_count = 0

        for key in untranslated:
            en_value = en_data[key]
            translated_value = translate_entry(key, en_value, lang_code, translations_dict)

            if translated_value and translated_value != en_value:
                target_data[key] = translated_value
                translated_count += 1
                print(f"  ✓ {key}")

        # Save updated file
        if translated_count > 0:
            save_json(target_path, target_data)
            print(f"\n✓ Saved {translated_count} translations to {lang_code}.json")

        summary[lang_code] = {
            'translated': translated_count,
            'total': len(untranslated),
            'remaining': len(untranslated) - translated_count
        }

    # Print summary
    print("\n" + "="*60)
    print("TRANSLATION SUMMARY")
    print("="*60)
    for lang_code, lang_name in languages.items():
        stats = summary[lang_code]
        print(f"{lang_name} ({lang_code}):")
        print(f"  - Translated: {stats['translated']}")
        print(f"  - Total untranslated found: {stats['total']}")
        print(f"  - Remaining: {stats['remaining']}")
        print()

if __name__ == '__main__':
    main()
