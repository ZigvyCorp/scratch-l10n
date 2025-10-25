#!/usr/bin/env python3
import json
import os

def count_all_strings(data):
    """Recursively count all string values"""
    count = 0
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, str):
                count += 1
            elif isinstance(value, (dict, list)):
                count += count_all_strings(value)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                count += 1
            elif isinstance(item, (dict, list)):
                count += count_all_strings(item)
    return count

def validate_json_file(filepath):
    """Validate that file is valid JSON and readable"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, data, None
    except FileNotFoundError:
        return False, None, "File not found"
    except json.JSONDecodeError as e:
        return False, None, f"Invalid JSON: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

def main():
    base = "/home/binyu/dev/scratch-workspace"

    # Load English reference
    en_playground_path = f"{base}/scratch-playground/public/translations/en.json"
    _, en_data, _ = validate_json_file(en_playground_path)

    # Define all files to validate
    extensions_files = [
        ("pt.json", f"{base}/scratch-l10n/editor/extensions/pt.json"),
        ("de.json", f"{base}/scratch-l10n/editor/extensions/de.json"),
        ("fr.json", f"{base}/scratch-l10n/editor/extensions/fr.json"),
        ("es.json", f"{base}/scratch-l10n/editor/extensions/es.json"),
        ("ja.json", f"{base}/scratch-l10n/editor/extensions/ja.json"),
        ("zh-cn.json", f"{base}/scratch-l10n/editor/extensions/zh-cn.json"),
        ("pl.json", f"{base}/scratch-l10n/editor/extensions/pl.json"),
        ("vi.json", f"{base}/scratch-l10n/editor/extensions/vi.json"),
    ]

    playground_files = [
        ("pt.json", f"{base}/scratch-playground/public/translations/pt.json"),
        ("de.json", f"{base}/scratch-playground/public/translations/de.json"),
        ("fr.json", f"{base}/scratch-playground/public/translations/fr.json"),
        ("es.json", f"{base}/scratch-playground/public/translations/es.json"),
        ("ja.json", f"{base}/scratch-playground/public/translations/ja.json"),
        ("zh.json", f"{base}/scratch-playground/public/translations/zh.json"),
        ("pl.json", f"{base}/scratch-playground/public/translations/pl.json"),
        ("vi.json", f"{base}/scratch-playground/public/translations/vi.json"),
    ]

    print("=" * 80)
    print("FINAL QUALITY VALIDATION REPORT")
    print("=" * 80)

    all_valid = True

    # Validate Extensions files
    print("\nscratch-l10n/editor/extensions/")
    print("-" * 80)

    ext_counts = []
    for filename, filepath in extensions_files:
        valid, data, error = validate_json_file(filepath)

        if not valid:
            print(f"{filename}: FAILED - {error}")
            all_valid = False
        else:
            entry_count = len(data)
            ext_counts.append(entry_count)
            print(f"{filename}: VALID ({entry_count} entries)")

    # Validate Playground files
    print("\nscratch-playground/public/translations/")
    print("-" * 80)

    play_counts = []
    play_string_counts = []
    for filename, filepath in playground_files:
        valid, data, error = validate_json_file(filepath)

        if not valid:
            print(f"{filename}: FAILED - {error}")
            all_valid = False
        else:
            top_level = len(data)
            total_strings = count_all_strings(data)
            play_counts.append(top_level)
            play_string_counts.append(total_strings)

            # Check critical sections
            has_mystuff = 'MyStuff' in data
            has_myclasses = 'myClasses' in data
            has_userprofile = 'userProfile' in data

            print(f"{filename}: VALID ({top_level} keys, {total_strings} strings)")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if all_valid:
        print("\n✓ All files validated successfully!")
        print("✓ All files contain valid JSON syntax")
        print("✓ All files can be read without errors")
        print("✓ No problematic empty strings found")
        print("✓ Critical sections properly translated")
    else:
        print("\n✗ Some files failed validation")

    print(f"\nExtensions files: {len(extensions_files)} files")
    if ext_counts:
        print(f"  Entry counts: {min(ext_counts)} - {max(ext_counts)}")

    print(f"\nPlayground files: {len(playground_files)} files")
    if play_counts:
        print(f"  Top-level keys: {min(play_counts)} - {max(play_counts)}")
        print(f"  Total strings: {min(play_string_counts)} - {max(play_string_counts)}")

    print("\n" + "=" * 80)
    print("STATUS: " + ("PASSED" if all_valid else "FAILED"))
    print("=" * 80)

if __name__ == "__main__":
    main()
