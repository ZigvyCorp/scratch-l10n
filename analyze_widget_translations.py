#!/usr/bin/env python3
"""
Comprehensive analysis of widget translations in GUI locale files.
Compares against English source and reference l10n files.
"""

import json
import re

# File paths
GUI_EN = '/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/en.json'
GUI_JA = '/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/ja.json'
GUI_DE = '/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/de.json'
GUI_PT = '/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/pt.json'

L10N_JA = '/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/ja.json'
L10N_DE = '/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/de.json'
L10N_PT = '/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/pt.json'

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_widget_entries(data):
    """Extract all entries starting with 'widget.'"""
    return {k: v for k, v in data.items() if k.startswith('widget.')}

def detect_corruption(text, lang):
    """Detect obvious corruption patterns in text."""
    corruption_patterns = {
        'de': [
            r'saufppe', r'pareped', r'Rest veine', r'butaufn', r'ceinfirm',
            r'neindermal', r'regehe', r'hinterstegrunde', r'boderder',
            r'feint', r'Neine', r'auftal', r'icein', r'Eingabetastes',
            r'playhinterste', r'Positiein', r'rotan', r'hoderizeintal',
            r'ceintainer', r'can Positieinegodery', r'chan Positiein',
            r'upDan Positieinum', r'pfügeing'
        ],
        'pt': [
            r'adiciligadoe', r'padiciligadoeing', r'queo', r'fou',
            r'butparan', r'pareped', r'cligadofirm', r'trásgarredligadode',
            r'bouder', r'fligadot', r'nãomed', r'na posiçãoual',
            r'rna posiçãoio', r'sengle', r'ligadoly', r'nãoumal',
            r'escligadoda', r'Nligadoe', r'houizligadotal', r'cligadotainer',
            r'cna posiçãoegouy', r'parna posiçãoal', r'chna posição',
            r'icligado', r'updna posiçãoa', r'reste dee', r'useng'
        ],
        'ja': []
    }

    if lang not in corruption_patterns:
        return False

    for pattern in corruption_patterns[lang]:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def is_english_like(text, en_text):
    """Check if text is identical to English or contains mostly English words."""
    if text == en_text:
        return True

    # Check for common English words that shouldn't appear in translations
    english_words = [
        'widget', 'add', 'button', 'text', 'value', 'width', 'height',
        'padding', 'scroll', 'mode', 'named', 'click', 'video', 'table',
        'chart', 'using', 'from', 'line', 'bar', 'pie', 'percentage',
        'single', 'multiple', 'input', 'read only', 'normal', 'bold',
        'show', 'hide', 'None', 'Please select', 'start', 'pause', 'stop',
        'mute', 'unmute', 'yes', 'no', 'background', 'border', 'current',
        'seek', 'position', 'menu', 'alignment', 'transparency'
    ]

    # Count English words (case insensitive)
    text_lower = text.lower()
    english_count = sum(1 for word in english_words if word in text_lower)

    # If more than 5 English words appear, likely not properly translated
    return english_count > 5

def analyze_language(gui_data, l10n_data, en_data, lang_code, lang_name):
    """Analyze widget translations for a specific language."""
    gui_widgets = extract_widget_entries(gui_data)
    l10n_widgets = extract_widget_entries(l10n_data)
    en_widgets = extract_widget_entries(en_data)

    problems = []

    for key, gui_value in gui_widgets.items():
        en_value = en_widgets.get(key, '')
        l10n_value = l10n_widgets.get(key, None)

        issues = []

        # Check for corruption
        if detect_corruption(gui_value, lang_code):
            issues.append('CORRUPTED')

        # Check if identical to English
        if gui_value == en_value:
            issues.append('IDENTICAL_TO_ENGLISH')

        # Check if mostly English
        elif is_english_like(gui_value, en_value):
            issues.append('CONTAINS_TOO_MUCH_ENGLISH')

        # Check if different from reference l10n
        if l10n_value and gui_value != l10n_value:
            issues.append('DIFFERS_FROM_L10N')

        if issues:
            problems.append({
                'key': key,
                'gui_value': gui_value,
                'l10n_value': l10n_value if l10n_value else '(not found in l10n)',
                'en_value': en_value,
                'issues': issues
            })

    return {
        'total': len(gui_widgets),
        'problematic': len(problems),
        'problems': problems
    }

def main():
    """Main analysis function."""
    print("=" * 80)
    print("COMPREHENSIVE WIDGET TRANSLATION ANALYSIS")
    print("=" * 80)
    print()

    # Load all files
    print("Loading files...")
    en_data = load_json(GUI_EN)
    ja_gui = load_json(GUI_JA)
    de_gui = load_json(GUI_DE)
    pt_gui = load_json(GUI_PT)

    ja_l10n = load_json(L10N_JA)
    de_l10n = load_json(L10N_DE)
    pt_l10n = load_json(L10N_PT)

    print("Files loaded successfully.\n")

    # Analyze each language
    languages = [
        ('ja', 'Japanese', ja_gui, ja_l10n),
        ('de', 'German', de_gui, de_l10n),
        ('pt', 'Portuguese', pt_gui, pt_l10n)
    ]

    total_problems = 0

    for lang_code, lang_name, gui_data, l10n_data in languages:
        print("=" * 80)
        print(f"### {lang_name} (scratch-gui/src/lib/locales/{lang_code}.json)")
        print("=" * 80)

        result = analyze_language(gui_data, l10n_data, en_data, lang_code, lang_name)

        print(f"**Total widget entries:** {result['total']}")
        print(f"**Problematic entries:** {result['problematic']}")
        print()

        if result['problems']:
            print("**Issues found:**\n")

            for problem in result['problems']:
                print(f"- {problem['key']}")
                print(f"  Issues: {', '.join(problem['issues'])}")
                print(f"  GUI value: \"{problem['gui_value']}\"")
                if problem['l10n_value'] != '(not found in l10n)':
                    print(f"  L10N value: \"{problem['l10n_value']}\"")
                print(f"  EN value: \"{problem['en_value']}\"")
                print()

        total_problems += result['problematic']
        print()

    # Summary
    print("=" * 80)
    print("### SUMMARY")
    print("=" * 80)
    print(f"Total widget entries that need fixing across all languages: {total_problems}")
    print()
    print("**Recommendation:**")
    print("Copy all correct translations from scratch-l10n/editor/extensions/*.json")
    print("to scratch-gui/src/lib/locales/*.json")
    print()

if __name__ == '__main__':
    main()
