/**
 * Currently supported locales for the Scratch Project
 * @type {Object} Key Value pairs of locale code: Language name written in the language
 */

const locales = {
    'en': {name: 'English'},
    'es': {name: 'Español (España)'},
    'fr': {name: 'Français'},
    'de': {name: 'Deutsch'},
    'zh-cn': {name: '简体中文'},
    'zh-tw': {name: '繁體中文'},
    'ja': {name: '日本語'},
    'ab': {name: 'Аҧсшәа'},
    'af': {name: 'Afrikaans'},
    'ar': {name: 'العربية'},
    'am': {name: 'አማርኛ'},
    'an': {name: 'Aragonés'},
    'az': {name: 'Azeri'},
    'id': {name: 'Bahasa Indonesia'},
    'bn': {name: 'বাংলা'},
    'be': {name: 'Беларуская'},
    'bg': {name: 'Български'},
    'ca': {name: 'Català'},
    'cs': {name: 'Česky'},
    'cy': {name: 'Cymraeg'},
    'da': {name: 'Dansk'},
    'et': {name: 'Eesti'},
    'el': {name: 'Ελληνικά'},
    'es-419': {name: 'Español Latinoamericano'},
    'eu': {name: 'Euskara'},
    'fa': {name: 'فارسی'},
    'fy': {name: 'Frysk'},
    'ga': {name: 'Gaeilge'},
    'gd': {name: 'Gàidhlig'},
    'gl': {name: 'Galego'},
    'ko': {name: '한국어'},
    'hy': {name: 'Հայերեն'},
    'he': {name: 'עִבְרִית'},
    'hr': {name: 'Hrvatski'},
    'xh': {name: 'isiXhosa'},
    'zu': {name: 'isiZulu'},
    'is': {name: 'Íslenska'},
    'it': {name: 'Italiano'},
    'ka': {name: 'ქართული ენა'},
    'kk': {name: 'қазақша'},
    'qu': {name: 'Kichwa'},
    'sw': {name: 'Kiswahili'},
    'ht': {name: 'Kreyòl ayisyen'},
    'ku': {name: 'Kurdî'},
    'ckb': {name: 'کوردیی ناوەندی'},
    'lv': {name: 'Latviešu'},
    'lt': {name: 'Lietuvių'},
    'hu': {name: 'Magyar'},
    'mi': {name: 'Māori'},
    'mn': {name: 'Монгол хэл'},
    'nl': {name: 'Nederlands'},
    'ja-Hira': {name: 'にほんご'},
    'nb': {name: 'Norsk Bokmål'},
    'nn': {name: 'Norsk Nynorsk'},
    'or': {name: 'ଓଡ଼ିଆ'},
    'uz': {name: 'Oʻzbekcha'},
    'th': {name: 'ไทย'},
    'km': {name: 'ភាសាខ្មែរ'},
    'pl': {name: 'Polski'},
    'pt': {name: 'Português'},
    'pt-br': {name: 'Português Brasileiro'},
    'rap': {name: 'Rapa Nui'},
    'ro': {name: 'Română'},
    'ru': {name: 'Русский'},
    'nso': {name: 'Sepedi'},
    'tn': {name: 'Setswana'},
    'sk': {name: 'Slovenčina'},
    'sl': {name: 'Slovenščina'},
    'sr': {name: 'Српски'},
    'fi': {name: 'Suomi'},
    'sv': {name: 'Svenska'},
    'vi': {name: 'Tiếng Việt'},
    'tr': {name: 'Türkçe'},
    'uk': {name: 'Українська'}
};

const indexLanguage = {
    'en': {name: 'English'},
    'es': {name: 'Español (España)'},
    'fr': {name: 'Français'},
    'zh-cn': {name: '简体中文'},
    'zh-tw': {name: '繁體中文'}
};

const customLocales = {
    'ab': {
        locale: 'ab',
        parentLocale: 'ru'
    },
    // Aragonese is not in the locale data, using es for Spain
    'an': {
        locale: 'an',
        parentLocale: 'es'
    },
    // haitian creole is not in locale-langData
    'ht': {
        locale: 'ht',
        parentLocale: 'fr'
    },
    'rap': {
        locale: 'rap',
        parentLocale: 'es'
    },
    // TODO: replace zh-cn, zh-tw with zh-Hans and zh-Hant then customLocales is unnecessary
    'zh-cn': {
        locale: 'zh-cn',
        parentLocale: 'zh'
    },
    'zh-tw': {
        locale: 'zh-tw',
        parentLocale: 'zh'
    }
};

const localeMap = {
    'aa-dj': 'aa_DJ',
    'es-419': 'es_419',
    // ja-Hira: no map - it's 'ja-Hira' on transifex
    'pt-br': 'pt_BR',
    'zh-cn': 'zh_CN',
    'zh-tw': 'zh_TW'
};

// list of RTL locales supported, and a function to check whether a locale is RTL
const rtlLocales = [
    'ar',
    'ckb',
    'fa',
    'he'
];

const isRtl = locale => {
    return rtlLocales.indexOf(locale) !== -1;
};

export {locales as default, customLocales, localeMap, isRtl, indexLanguage};
