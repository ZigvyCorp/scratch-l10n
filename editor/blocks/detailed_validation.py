#!/usr/bin/env python3
import json
import os

def check_for_empty_strings(data, path=""):
    """Recursively check for empty strings in nested dict"""
    empty_found = []

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            if isinstance(value, str) and value == "":
                empty_found.append(current_path)
            elif isinstance(value, (dict, list)):
                empty_found.extend(check_for_empty_strings(value, current_path))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            current_path = f"{path}[{idx}]"
            if isinstance(item, str) and item == "":
                empty_found.append(current_path)
            elif isinstance(item, (dict, list)):
                empty_found.extend(check_for_empty_strings(item, current_path))

    return empty_found

def count_entries(data):
    """Count all string entries in nested structure"""
    count = 0

    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, str):
                count += 1
            elif isinstance(value, (dict, list)):
                count += count_entries(value)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                count += 1
            elif isinstance(item, (dict, list)):
                count += count_entries(item)

    return count

def check_critical_sections(data, lang):
    """Check specific sections for obvious issues"""
    issues = []

    # Check MyStuff
    if 'MyStuff' in data:
        mystuff = data['MyStuff']
        # These should definitely be translated
        critical_keys = ['note', 'difficulty', 'searchPlace', 'created', 'description', 'email']

        for key in critical_keys:
            if key in mystuff:
                value = str(mystuff[key])
                # Check if it starts with English words (case-insensitive)
                english_starts = ['Note:', 'Difficulty:', 'Search by', 'Created:', 'Description:', 'Email:']
                for eng in english_starts:
                    if value.startswith(eng):
                        issues.append(f"MyStuff.{key} starts with English: '{value[:30]}...'")

    # Check myClasses
    if 'myClasses' in data:
        myclasses = data['myClasses']
        critical_keys = ['student', 'teacher', 'viewProject']

        for key in critical_keys:
            if key in myclasses:
                value = str(myclasses[key])
                if value in ['student', 'teacher', 'view', 'Student', 'Teacher', 'View']:
                    issues.append(f"myClasses.{key} is untranslated English: '{value}'")

    # Check userProfile
    if 'userProfile' in data:
        profile = data['userProfile']
        if 'header' in profile:
            header = profile['header']
            if isinstance(header, dict):
                critical_keys = ['joined', 'country']
                for key in critical_keys:
                    if key in header:
                        value = str(header[key])
                        if value in ['Joined', 'Country', 'joined', 'country']:
                            issues.append(f"userProfile.header.{key} is untranslated: '{value}'")

    return issues

def validate_file(filepath, lang_code):
    """Validate a translation file"""
    if not os.path.exists(filepath):
        return {"error": "File does not exist"}

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check for empty strings
        empty_strings = check_for_empty_strings(data)

        # Count entries
        top_level_count = len(data)
        total_strings = count_entries(data)

        # Check critical sections (only for playground)
        critical_issues = []
        if 'MyStuff' in data or 'myClasses' in data:  # Playground file
            critical_issues = check_critical_sections(data, lang_code)

        return {
            "valid": True,
            "top_level_keys": top_level_count,
            "total_strings": total_strings,
            "empty_strings": empty_strings,
            "critical_issues": critical_issues
        }

    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

def main():
    base = "/home/binyu/dev/scratch-workspace"

    files_to_check = [
        ("scratch-l10n/editor/extensions", "pt.json", "pt"),
        ("scratch-l10n/editor/extensions", "de.json", "de"),
        ("scratch-l10n/editor/extensions", "fr.json", "fr"),
        ("scratch-l10n/editor/extensions", "es.json", "es"),
        ("scratch-l10n/editor/extensions", "ja.json", "ja"),
        ("scratch-l10n/editor/extensions", "zh-cn.json", "zh-cn"),
        ("scratch-l10n/editor/extensions", "pl.json", "pl"),
        ("scratch-l10n/editor/extensions", "vi.json", "vi"),
        ("scratch-playground/public/translations", "pt.json", "pt"),
        ("scratch-playground/public/translations", "de.json", "de"),
        ("scratch-playground/public/translations", "fr.json", "fr"),
        ("scratch-playground/public/translations", "es.json", "es"),
        ("scratch-playground/public/translations", "ja.json", "ja"),
        ("scratch-playground/public/translations", "zh.json", "zh"),
        ("scratch-playground/public/translations", "pl.json", "pl"),
        ("scratch-playground/public/translations", "vi.json", "vi"),
    ]

    print("=" * 80)
    print("DETAILED TRANSLATION VALIDATION REPORT")
    print("=" * 80)

    all_valid = True
    current_dir = None

    for dir_path, filename, lang in files_to_check:
        filepath = f"{base}/{dir_path}/{filename}"

        # Print directory header
        if dir_path != current_dir:
            print(f"\n{dir_path}/")
            print("-" * 80)
            current_dir = dir_path

        result = validate_file(filepath, lang)

        if "error" in result:
            print(f"\n{filename}: ERROR")
            print(f"  {result['error']}")
            all_valid = False
        else:
            has_issues = result['empty_strings'] or result['critical_issues']

            if has_issues:
                print(f"\n{filename}: ISSUES FOUND")
                all_valid = False
            else:
                print(f"{filename}: OK", end="")

            print(f" (Keys: {result['top_level_keys']}, Strings: {result['total_strings']})")

            if result['empty_strings']:
                print(f"  WARNING: {len(result['empty_strings'])} empty string(s) found:")
                for empty in result['empty_strings'][:5]:
                    print(f"    - {empty}")
                if len(result['empty_strings']) > 5:
                    print(f"    ... and {len(result['empty_strings']) - 5} more")

            if result['critical_issues']:
                print(f"  WARNING: {len(result['critical_issues'])} critical issue(s):")
                for issue in result['critical_issues']:
                    print(f"    - {issue}")

    # Summary
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    if all_valid:
        print("\nAll files validated successfully!")
        print("- No empty strings found")
        print("- No obvious untranslated text in critical sections")
        print("- All JSON files are valid")
    else:
        print("\nSome files have issues - see details above")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
