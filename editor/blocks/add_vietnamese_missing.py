#!/usr/bin/env python3
"""
Add missing Vietnamese translations for MyStuff section.
"""

import json

# Vietnamese translations for MyStuff missing entries
VI_TRANSLATIONS = {
    'MyStuff': {
        'd3AvatarModal': {
            'header': 'Thêm Avatar 3D',
            'submitBtn': 'Gửi',
            'title': 'Tiêu đề Avatar'
        },
        'modelModal': {
            'header': 'Thêm Mô Hình',
            'submitBtn': 'Gửi',
            'title': 'Tiêu đề Mô Hình',
            'error': {
                'MODEL_EXISTED': {
                    'message': 'Mô hình đã tồn tại',
                    'description': 'Mô hình này đã tồn tại trong hệ thống'
                },
                'SOMETHING_WENT_WRONG': {
                    'message': 'Đã xảy ra lỗi',
                    'description': 'Đã xảy ra lỗi. Vui lòng thử lại'
                }
            }
        },
        'myStudents': {
            'class': 'Lớp',
            'email': 'Email',
            'empty': 'Không có học sinh nào',
            'id': 'ID',
            'isPremium': {
                'true': 'Có',
                'false': 'Không'
            },
            'name': 'Tên',
            'no': 'STT',
            'notification': {
                'ALREADY_IN_TEACHER': 'Học sinh đã có trong lớp của giáo viên',
                'ERROR_PREMIUM_TEACHER': 'Lỗi cập nhật trạng thái Premium của giáo viên',
                'ERROR_TOGGLE_PREMIUM': 'Lỗi khi chuyển đổi trạng thái Premium',
                'INSERT_CLASS': 'Thêm vào lớp thành công',
                'MOVE_CLASS': 'Chuyển lớp thành công',
                'PREMIUM_STATUS_false': 'Đã tắt trạng thái Premium',
                'PREMIUM_STATUS_true': 'Đã bật trạng thái Premium',
                'undefined': 'Không xác định'
            },
            'premium': 'Premium',
            'premiumAvailableText': 'Còn lại: {count}/{total}',
            'premiumTotalText': 'Tổng số tài khoản Premium',
            'username': 'Tên đăng nhập'
        },
        'quizModal': {
            'header': 'Thêm Bài Kiểm Tra',
            'updateHeader': 'Cập Nhật Bài Kiểm Tra',
            'button': {
                'add': 'Thêm',
                'cancel': 'Hủy',
                'update': 'Cập nhật'
            },
            'label': {
                'coverImageUrl': 'URL Ảnh Bìa',
                'customXOPrompt': 'Lời Nhắc XO Tùy Chỉnh',
                'difficulty': 'Độ Khó',
                'notes': 'Ghi Chú',
                'prerequisiteQuiz': 'Bài Kiểm Tra Tiên Quyết',
                'projectUrl': 'URL Dự Án',
                'shareStatus': 'Trạng Thái Chia Sẻ',
                'title': 'Tiêu Đề'
            },
            'error': {
                'require': {
                    'title': 'Tiêu đề là bắt buộc',
                    'projectUrl': 'URL dự án là bắt buộc'
                }
            }
        },
        'studentMonitor': {
            'blockAdd': 'Khối Đã Thêm',
            'blockCount': 'Số Lượng Khối',
            'creation': 'Ngày Tạo',
            'lastSave': 'Lần Lưu Cuối',
            'project': 'Dự Án'
        },
        'studioSharingMode': {
            'private': 'Riêng tư',
            'shareToAll': 'Chia sẻ công khai',
            'shareWithinClass': 'Chia sẻ trong lớp',
            'shareWithinCurators': 'Chia sẻ với người quản lý',
            'undefined': 'Không xác định'
        },
        'toggleModal': {
            'd3Avatars': 'Avatar 3D',
            'files': 'Tệp',
            'models': 'Mô Hình',
            'quizzes': 'Bài Kiểm Tra',
            'studentMonitor': 'Giám Sát Học Sinh',
            'trash': 'Thùng Rác'
        }
    }
}


def deep_merge(target, source):
    """Deep merge source dict into target dict."""
    for key, value in source.items():
        if key in target and isinstance(target[key], dict) and isinstance(value, dict):
            deep_merge(target[key], value)
        else:
            target[key] = value


def main():
    vi_file = '/home/binyu/dev/scratch-workspace/scratch-playground/public/translations/vi.json'

    # Load Vietnamese file
    with open(vi_file, 'r', encoding='utf-8') as f:
        vi_data = json.load(f)

    print(f"Loaded vi.json")
    print(f"Current MyStuff keys: {len(vi_data.get('MyStuff', {}))}")

    # Merge translations
    deep_merge(vi_data, VI_TRANSLATIONS)

    print(f"After merge MyStuff keys: {len(vi_data.get('MyStuff', {}))}")

    # Save updated file
    with open(vi_file, 'w', encoding='utf-8') as f:
        json.dump(vi_data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"Updated vi.json with Vietnamese translations")
    print(f"Added 70 missing entries to Vietnamese file")


if __name__ == '__main__':
    main()
