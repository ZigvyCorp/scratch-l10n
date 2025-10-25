#!/usr/bin/env python3
"""
Add missing translation entries to playground translation files.
Compares each language file against en.json and adds missing entries with translations.
"""

import json
import os
from typing import Dict, List, Tuple, Any

# Translation mappings for common terms
TRANSLATIONS = {
    'es': {
        'BlackList': {
            'header': 'Lista de Bloqueo',
            'description': 'Los usuarios en la lista de bloqueo no pueden acceder a tu perfil.',
            'empty': 'No tienes usuarios bloqueados en este momento.',
            'unblock': 'Desbloquear',
            'confirmUnblock': '¿Estás seguro de que quieres desbloquear a {username}?',
            'unblockSuccess': '{username} ha sido desbloqueado exitosamente.',
            'unblockError': 'Error al desbloquear al usuario. Por favor, intenta de nuevo.',
        },
        'CommunityGatePage': {
            'header': 'Bienvenido a la Comunidad de Scratch',
            'description': 'Scratch es una comunidad en línea donde puedes crear y compartir tus propias historias, juegos y animaciones interactivas.',
            'guidelines': {
                'title': 'Pautas de la Comunidad',
                'respectful': 'Ser respetuoso',
                'constructive': 'Ser constructivo',
                'share': 'Compartir',
                'respectfulDesc': 'Cuando compartes proyectos o publicas comentarios, recuerda que personas de diferentes edades y orígenes verán lo que compartes.',
                'constructiveDesc': 'Cuando comentes en proyectos, di algo que te guste y ofrece sugerencias útiles.',
                'shareDesc': 'Eres libre de remezclar proyectos, ideas, imágenes o cualquier cosa que encuentres en Scratch, y cualquiera puede usar cualquier cosa que compartas. Asegúrate de dar crédito cuando remezcles.',
            },
            'accept': 'Acepto las Pautas de la Comunidad',
            'decline': 'Cancelar',
        },
        'Dashboard': {
            'header': 'Panel de Control',
            'myStuff': 'Mis Cosas',
            'myProjects': 'Mis Proyectos',
            'myStudios': 'Mis Estudios',
            'myFavorites': 'Mis Favoritos',
            'recentProjects': 'Proyectos Recientes',
            'recentStudios': 'Estudios Recientes',
            'recentActivity': 'Actividad Reciente',
            'whatIsHappening': '¿Qué está pasando?',
            'noRecentActivity': 'No hay actividad reciente',
            'lovedByCount': '{count} persona le encanta esto',
            'lovedByCount_plural': '{count} personas les encanta esto',
            'favoriteCount': '{count} favorito',
            'favoriteCount_plural': '{count} favoritos',
            'remixCount': '{count} remezcla',
            'remixCount_plural': '{count} remezclas',
            'viewCount': '{count} vista',
            'viewCount_plural': '{count} vistas',
            'projectTitle': 'Título del Proyecto',
            'studioTitle': 'Título del Estudio',
            'shared': 'Compartido',
            'notShared': 'No Compartido',
            'shareProject': 'Compartir Proyecto',
            'seeAll': 'Ver Todo',
            'noProjects': 'No tienes proyectos todavía',
            'noStudios': 'No sigues ningún estudio todavía',
            'noFavorites': 'No tienes favoritos todavía',
            'createProject': 'Crear Proyecto',
            'exploreStudios': 'Explorar Estudios',
            'exploreProjects': 'Explorar Proyectos',
            'loading': 'Cargando...',
            'error': 'Error al cargar el panel de control',
        },
    },
    'fr': {
        'BlackList': {
            'header': 'Liste de Blocage',
            'description': 'Les utilisateurs sur la liste de blocage ne peuvent pas accéder à votre profil.',
            'empty': 'Vous n\'avez aucun utilisateur bloqué pour le moment.',
            'unblock': 'Débloquer',
            'confirmUnblock': 'Êtes-vous sûr de vouloir débloquer {username} ?',
            'unblockSuccess': '{username} a été débloqué avec succès.',
            'unblockError': 'Erreur lors du déblocage de l\'utilisateur. Veuillez réessayer.',
        },
        'CommunityGatePage': {
            'header': 'Bienvenue dans la Communauté Scratch',
            'description': 'Scratch est une communauté en ligne où vous pouvez créer et partager vos propres histoires, jeux et animations interactives.',
            'guidelines': {
                'title': 'Directives de la Communauté',
                'respectful': 'Être respectueux',
                'constructive': 'Être constructif',
                'share': 'Partager',
                'respectfulDesc': 'Lorsque vous partagez des projets ou publiez des commentaires, rappelez-vous que des personnes de différents âges et origines verront ce que vous partagez.',
                'constructiveDesc': 'Lorsque vous commentez des projets, dites quelque chose que vous aimez et offrez des suggestions utiles.',
                'shareDesc': 'Vous êtes libre de remixer des projets, des idées, des images ou tout ce que vous trouvez sur Scratch, et tout le monde peut utiliser tout ce que vous partagez. Assurez-vous de donner du crédit lorsque vous remixez.',
            },
            'accept': 'J\'accepte les Directives de la Communauté',
            'decline': 'Annuler',
        },
        'Dashboard': {
            'header': 'Tableau de Bord',
            'myStuff': 'Mes Affaires',
            'myProjects': 'Mes Projets',
            'myStudios': 'Mes Studios',
            'myFavorites': 'Mes Favoris',
            'recentProjects': 'Projets Récents',
            'recentStudios': 'Studios Récents',
            'recentActivity': 'Activité Récente',
            'whatIsHappening': 'Que se passe-t-il ?',
            'noRecentActivity': 'Aucune activité récente',
            'lovedByCount': '{count} personne aime ceci',
            'lovedByCount_plural': '{count} personnes aiment ceci',
            'favoriteCount': '{count} favori',
            'favoriteCount_plural': '{count} favoris',
            'remixCount': '{count} remix',
            'remixCount_plural': '{count} remixes',
            'viewCount': '{count} vue',
            'viewCount_plural': '{count} vues',
            'projectTitle': 'Titre du Projet',
            'studioTitle': 'Titre du Studio',
            'shared': 'Partagé',
            'notShared': 'Non Partagé',
            'shareProject': 'Partager le Projet',
            'seeAll': 'Voir Tout',
            'noProjects': 'Vous n\'avez pas encore de projets',
            'noStudios': 'Vous ne suivez aucun studio pour le moment',
            'noFavorites': 'Vous n\'avez pas encore de favoris',
            'createProject': 'Créer un Projet',
            'exploreStudios': 'Explorer les Studios',
            'exploreProjects': 'Explorer les Projets',
            'loading': 'Chargement...',
            'error': 'Erreur lors du chargement du tableau de bord',
        },
    },
    'zh': {
        'BlackList': {
            'header': '黑名单',
            'description': '黑名单中的用户无法访问您的个人资料。',
            'empty': '您目前没有屏蔽任何用户。',
            'unblock': '解除屏蔽',
            'confirmUnblock': '您确定要解除屏蔽 {username} 吗？',
            'unblockSuccess': '{username} 已成功解除屏蔽。',
            'unblockError': '解除屏蔽用户时出错。请重试。',
        },
        'CommunityGatePage': {
            'header': '欢迎来到 Scratch 社区',
            'description': 'Scratch 是一个在线社区，您可以在这里创建和分享自己的互动故事、游戏和动画。',
            'guidelines': {
                'title': '社区准则',
                'respectful': '相互尊重',
                'constructive': '建设性意见',
                'share': '分享',
                'respectfulDesc': '当您分享项目或发表评论时，请记住不同年龄和背景的人都会看到您分享的内容。',
                'constructiveDesc': '当您对项目发表评论时，请说出您喜欢的地方并提供有用的建议。',
                'shareDesc': '您可以自由地改编项目、创意、图片或您在 Scratch 上找到的任何内容，任何人都可以使用您分享的任何内容。请确保在改编时注明出处。',
            },
            'accept': '我接受社区准则',
            'decline': '取消',
        },
        'Dashboard': {
            'header': '仪表板',
            'myStuff': '我的东西',
            'myProjects': '我的项目',
            'myStudios': '我的工作室',
            'myFavorites': '我的收藏',
            'recentProjects': '最近的项目',
            'recentStudios': '最近的工作室',
            'recentActivity': '最近的活动',
            'whatIsHappening': '发生了什么？',
            'noRecentActivity': '没有最近的活动',
            'lovedByCount': '{count} 人喜欢',
            'lovedByCount_plural': '{count} 人喜欢',
            'favoriteCount': '{count} 个收藏',
            'favoriteCount_plural': '{count} 个收藏',
            'remixCount': '{count} 个改编',
            'remixCount_plural': '{count} 个改编',
            'viewCount': '{count} 次浏览',
            'viewCount_plural': '{count} 次浏览',
            'projectTitle': '项目标题',
            'studioTitle': '工作室标题',
            'shared': '已分享',
            'notShared': '未分享',
            'shareProject': '分享项目',
            'seeAll': '查看全部',
            'noProjects': '您还没有项目',
            'noStudios': '您还没有关注任何工作室',
            'noFavorites': '您还没有收藏',
            'createProject': '创建项目',
            'exploreStudios': '探索工作室',
            'exploreProjects': '探索项目',
            'loading': '加载中...',
            'error': '加载仪表板时出错',
        },
    },
    'vi': {
        'BlackList': {
            'header': 'Danh Sách Chặn',
            'description': 'Người dùng trong danh sách chặn không thể truy cập hồ sơ của bạn.',
            'empty': 'Bạn hiện không có người dùng bị chặn.',
            'unblock': 'Bỏ Chặn',
            'confirmUnblock': 'Bạn có chắc chắn muốn bỏ chặn {username} không?',
            'unblockSuccess': '{username} đã được bỏ chặn thành công.',
            'unblockError': 'Lỗi khi bỏ chặn người dùng. Vui lòng thử lại.',
        },
        'CommunityGatePage': {
            'header': 'Chào Mừng Đến Với Cộng Đồng Scratch',
            'description': 'Scratch là một cộng đồng trực tuyến nơi bạn có thể tạo và chia sẻ các câu chuyện, trò chơi và hoạt ảnh tương tác của riêng mình.',
            'guidelines': {
                'title': 'Hướng Dẫn Cộng Đồng',
                'respectful': 'Tôn trọng',
                'constructive': 'Xây dựng',
                'share': 'Chia sẻ',
                'respectfulDesc': 'Khi bạn chia sẻ dự án hoặc đăng bình luận, hãy nhớ rằng mọi người ở nhiều lứa tuổi và xuất thân khác nhau sẽ xem những gì bạn chia sẻ.',
                'constructiveDesc': 'Khi bình luận về dự án, hãy nói điều gì đó bạn thích và đưa ra các gợi ý hữu ích.',
                'shareDesc': 'Bạn được tự do phối lại dự án, ý tưởng, hình ảnh hoặc bất cứ điều gì bạn tìm thấy trên Scratch, và bất kỳ ai cũng có thể sử dụng bất cứ điều gì bạn chia sẻ. Hãy chắc chắn ghi công khi phối lại.',
            },
            'accept': 'Tôi Chấp Nhận Hướng Dẫn Cộng Đồng',
            'decline': 'Hủy',
        },
        'Dashboard': {
            'header': 'Bảng Điều Khiển',
            'myStuff': 'Đồ Của Tôi',
            'myProjects': 'Dự Án Của Tôi',
            'myStudios': 'Xưởng Của Tôi',
            'myFavorites': 'Yêu Thích Của Tôi',
            'recentProjects': 'Dự Án Gần Đây',
            'recentStudios': 'Xưởng Gần Đây',
            'recentActivity': 'Hoạt Động Gần Đây',
            'whatIsHappening': 'Đang xảy ra gì?',
            'noRecentActivity': 'Không có hoạt động gần đây',
            'lovedByCount': '{count} người yêu thích',
            'lovedByCount_plural': '{count} người yêu thích',
            'favoriteCount': '{count} lượt thích',
            'favoriteCount_plural': '{count} lượt thích',
            'remixCount': '{count} phối lại',
            'remixCount_plural': '{count} phối lại',
            'viewCount': '{count} lượt xem',
            'viewCount_plural': '{count} lượt xem',
            'projectTitle': 'Tiêu Đề Dự Án',
            'studioTitle': 'Tiêu Đề Xưởng',
            'shared': 'Đã Chia Sẻ',
            'notShared': 'Chưa Chia Sẻ',
            'shareProject': 'Chia Sẻ Dự Án',
            'seeAll': 'Xem Tất Cả',
            'noProjects': 'Bạn chưa có dự án nào',
            'noStudios': 'Bạn chưa theo dõi xưởng nào',
            'noFavorites': 'Bạn chưa có mục yêu thích nào',
            'createProject': 'Tạo Dự Án',
            'exploreStudios': 'Khám Phá Xưởng',
            'exploreProjects': 'Khám Phá Dự Án',
            'loading': 'Đang tải...',
            'error': 'Lỗi khi tải bảng điều khiển',
        },
    },
}


def load_json(filepath: str) -> Dict:
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath: str, data: Dict) -> None:
    """Save JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def get_missing_keys(reference: Dict, target: Dict, prefix: str = '') -> List[str]:
    """Recursively find all missing keys in target compared to reference."""
    missing = []

    for key, value in reference.items():
        current_path = f"{prefix}.{key}" if prefix else key

        if key not in target:
            missing.append(current_path)
        elif isinstance(value, dict) and isinstance(target.get(key), dict):
            missing.extend(get_missing_keys(value, target[key], current_path))

    return missing


def get_value_by_path(data: Dict, path: str) -> Any:
    """Get value from nested dict using dot-separated path."""
    keys = path.split('.')
    value = data
    for key in keys:
        value = value[key]
    return value


def set_value_by_path(data: Dict, path: str, value: Any) -> None:
    """Set value in nested dict using dot-separated path."""
    keys = path.split('.')
    current = data

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value


def translate_value(value: Any, lang_code: str, path: str) -> Any:
    """Translate a value based on predefined translations or use the English value."""
    if isinstance(value, dict):
        return {k: translate_value(v, lang_code, f"{path}.{k}") for k, v in value.items()}
    elif isinstance(value, str):
        # Try to find translation in our predefined translations
        path_parts = path.split('.')

        if lang_code in TRANSLATIONS:
            trans = TRANSLATIONS[lang_code]

            # Navigate through the translation structure
            for part in path_parts:
                if isinstance(trans, dict) and part in trans:
                    trans = trans[part]
                else:
                    # Translation not found, return original
                    return value

            if isinstance(trans, str):
                return trans

        # If no translation found, return the original English value
        return value
    else:
        return value


def add_missing_translations(en_data: Dict, target_data: Dict, lang_code: str) -> Tuple[Dict, int]:
    """Add missing translations to target data."""
    missing_keys = get_missing_keys(en_data, target_data)

    for key_path in missing_keys:
        en_value = get_value_by_path(en_data, key_path)
        translated_value = translate_value(en_value, lang_code, key_path)
        set_value_by_path(target_data, key_path, translated_value)

    return target_data, len(missing_keys)


def main():
    """Main execution function."""
    base_path = '/home/binyu/dev/scratch-workspace/scratch-playground/public/translations'
    en_file = os.path.join(base_path, 'en.json')

    # Language files to process (note: zh.json not zh-cn.json)
    languages = {
        'es': 'es.json',
        'fr': 'fr.json',
        'zh': 'zh.json',
        'vi': 'vi.json',
    }

    print("Loading English reference file...")
    en_data = load_json(en_file)
    print(f"English file loaded with {len(en_data)} top-level keys\n")

    results = {}

    for lang_code, filename in languages.items():
        print(f"Processing {lang_code}...")
        target_file = os.path.join(base_path, filename)

        # Load target language file
        target_data = load_json(target_file)
        print(f"  Loaded {filename} with {len(target_data)} top-level keys")

        # Find and add missing translations
        updated_data, added_count = add_missing_translations(en_data, target_data, lang_code)

        # Save updated file
        save_json(target_file, updated_data)
        print(f"  Added {added_count} missing entries")
        print(f"  Updated {filename}\n")

        results[lang_code] = added_count

    print("="*60)
    print("SUMMARY:")
    print("="*60)
    for lang_code, count in results.items():
        print(f"{lang_code}: {count} entries added")
    print("="*60)
    print(f"Total entries added: {sum(results.values())}")


if __name__ == '__main__':
    main()
