#!/usr/bin/env python3
import json
import os
import re

def validate_file(file_path, file_type):
    """Validate a single translation file"""
    issues = []

    # Check if file exists
    if not os.path.exists(file_path):
        return {"exists": False, "issues": ["File does not exist"]}

    try:
        # Read and parse JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        entry_count = len(data)

        # Check for empty strings
        empty_strings = [key for key, value in data.items() if value == ""]
        if empty_strings:
            issues.append(f"Found {len(empty_strings)} empty string(s): {', '.join(empty_strings[:5])}" +
                         ("..." if len(empty_strings) > 5 else ""))

        # Check for obvious English in critical sections (playground files only)
        if file_type == "playground":
            critical_sections = ["MyStuff", "myStuff", "userProfile", "myClasses"]
            english_patterns = [
                r'\b(my stuff|my classes|user profile)\b',
                r'\b(create|delete|share|unshare|view)\b',
                r'\b(class|student|teacher|project)\b'
            ]

            english_found = []
            for section in critical_sections:
                if section in data:
                    value = str(data[section]).lower()
                    for pattern in english_patterns:
                        if re.search(pattern, value, re.IGNORECASE):
                            text_snippet = str(data[section])[:50]
                            english_found.append(f"{section}: {text_snippet}")
                            break

            if english_found:
                issues.append(f"Possible English text in critical sections: {', '.join(english_found[:3])}")

        return {
            "exists": True,
            "valid_json": True,
            "entry_count": entry_count,
            "issues": issues
        }

    except json.JSONDecodeError as e:
        return {
            "exists": True,
            "valid_json": False,
            "issues": [f"JSON syntax error: {str(e)}"]
        }
    except Exception as e:
        return {
            "exists": True,
            "valid_json": False,
            "issues": [f"Error reading file: {str(e)}"]
        }

def main():
    base_path = "/home/binyu/dev/scratch-workspace"

    # Define files to validate
    extensions_files = [
        ("pt.json", f"{base_path}/scratch-l10n/editor/extensions/pt.json"),
        ("de.json", f"{base_path}/scratch-l10n/editor/extensions/de.json"),
        ("fr.json", f"{base_path}/scratch-l10n/editor/extensions/fr.json"),
        ("es.json", f"{base_path}/scratch-l10n/editor/extensions/es.json"),
        ("ja.json", f"{base_path}/scratch-l10n/editor/extensions/ja.json"),
        ("zh-cn.json", f"{base_path}/scratch-l10n/editor/extensions/zh-cn.json"),
        ("pl.json", f"{base_path}/scratch-l10n/editor/extensions/pl.json"),
        ("vi.json", f"{base_path}/scratch-l10n/editor/extensions/vi.json"),
    ]

    playground_files = [
        ("pt.json", f"{base_path}/scratch-playground/public/translations/pt.json"),
        ("de.json", f"{base_path}/scratch-playground/public/translations/de.json"),
        ("fr.json", f"{base_path}/scratch-playground/public/translations/fr.json"),
        ("es.json", f"{base_path}/scratch-playground/public/translations/es.json"),
        ("ja.json", f"{base_path}/scratch-playground/public/translations/ja.json"),
        ("zh.json", f"{base_path}/scratch-playground/public/translations/zh.json"),
        ("pl.json", f"{base_path}/scratch-playground/public/translations/pl.json"),
        ("vi.json", f"{base_path}/scratch-playground/public/translations/vi.json"),
    ]

    print("=" * 80)
    print("TRANSLATION FILES VALIDATION REPORT")
    print("=" * 80)

    all_valid = True

    # Validate extensions files
    print("\n\nscratch-l10n/editor/extensions/")
    print("-" * 80)
    ext_counts = []
    for filename, filepath in extensions_files:
        result = validate_file(filepath, "extensions")
        ext_counts.append(result.get("entry_count", 0))

        if not result["exists"]:
            print(f"\n{filename}: MISSING")
            all_valid = False
        elif not result["valid_json"]:
            print(f"\n{filename}: INVALID JSON")
            for issue in result["issues"]:
                print(f"  - {issue}")
            all_valid = False
        elif result["issues"]:
            print(f"\n{filename}: ISSUES FOUND")
            print(f"  Entries: {result['entry_count']}")
            for issue in result["issues"]:
                print(f"  - {issue}")
            all_valid = False
        else:
            print(f"{filename}: OK ({result['entry_count']} entries)")

    # Validate playground files
    print("\n\nscratch-playground/public/translations/")
    print("-" * 80)
    play_counts = []
    for filename, filepath in playground_files:
        result = validate_file(filepath, "playground")
        play_counts.append(result.get("entry_count", 0))

        if not result["exists"]:
            print(f"\n{filename}: MISSING")
            all_valid = False
        elif not result["valid_json"]:
            print(f"\n{filename}: INVALID JSON")
            for issue in result["issues"]:
                print(f"  - {issue}")
            all_valid = False
        elif result["issues"]:
            print(f"\n{filename}: ISSUES FOUND")
            print(f"  Entries: {result['entry_count']}")
            for issue in result["issues"]:
                print(f"  - {issue}")
            all_valid = False
        else:
            print(f"{filename}: OK ({result['entry_count']} entries)")

    # Summary
    print("\n\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if all_valid:
        print("\nAll files validated successfully!")
    else:
        print("\nSome files have issues - see details above")

    print(f"\nExtensions files: {len(extensions_files)} files")
    if ext_counts:
        print(f"  Average entries: {sum(ext_counts) // len(ext_counts)}")
        print(f"  Range: {min(ext_counts)} - {max(ext_counts)} entries")

    print(f"\nPlayground files: {len(playground_files)} files")
    if play_counts:
        print(f"  Average entries: {sum(play_counts) // len(play_counts)}")
        print(f"  Range: {min(play_counts)} - {max(play_counts)} entries")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
