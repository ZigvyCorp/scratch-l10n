/**
 * Locale loader for lazy loading translation files
 */

// Cache for loaded locales
const localeCache = new Map();

// Import English as default (always bundled)
import editorMessagesEn from '../locales/editor-msgs-en.js';
import blocksMessagesEn from '../locales/blocks-msgs-en.js';

// Pre-populate cache with English
localeCache.set('editor-en', editorMessagesEn);
localeCache.set('blocks-en', blocksMessagesEn);

/**
 * Load locale messages dynamically
 * @param {string} locale - The locale to load (e.g., 'pl', 'zh-cn')
 * @param {string} component - The component type ('editor', 'blocks', etc.)
 * @returns {Promise<Object>} The loaded messages
 */
export async function loadLocaleMessages(locale, component = 'editor') {
    // Always return English synchronously if requested
    if (locale === 'en') {
        return localeCache.get(`${component}-en`);
    }

    const cacheKey = `${component}-${locale}`;

    // Return cached locale if available
    if (localeCache.has(cacheKey)) {
        return localeCache.get(cacheKey);
    }

    try {
        // Dynamic import with webpack chunk naming
        const messages = await import(
            /* webpackChunkName: "[request]" */
            /* webpackMode: "lazy" */
            `../locales/${component}-msgs-${locale}.js`
        );

        const loadedMessages = messages.default || messages;
        localeCache.set(cacheKey, loadedMessages);
        return loadedMessages;
    } catch (error) {
        console.error(`Failed to load ${component} messages for locale: ${locale}`, error);

        // Fall back to English
        console.warn(`Falling back to English for ${component}`);
        return localeCache.get(`${component}-en`);
    }
}

/**
 * Load all component messages for a locale
 * @param {string} locale - The locale to load
 * @returns {Promise<Object>} Combined messages for all components
 */
export async function loadAllMessages(locale) {
    if (locale === 'en') {
        // Return English synchronously
        return {
            editor: editorMessagesEn,
            blocks: blocksMessagesEn
        };
    }

    try {
        const [editor, blocks] = await Promise.all([
            loadLocaleMessages(locale, 'editor'),
            loadLocaleMessages(locale, 'blocks')
        ]);

        return { editor, blocks };
    } catch (error) {
        console.error(`Failed to load all messages for locale: ${locale}`, error);
        // Fall back to English
        return {
            editor: editorMessagesEn,
            blocks: blocksMessagesEn
        };
    }
}

/**
 * Preload a locale for faster switching
 * @param {string} locale - The locale to preload
 */
export async function preloadLocale(locale) {
    if (locale === 'en') return; // English is already loaded

    try {
        await Promise.all([
            loadLocaleMessages(locale, 'editor'),
            loadLocaleMessages(locale, 'blocks')
        ]);
        console.log(`Preloaded locale: ${locale}`);
    } catch (error) {
        console.error(`Failed to preload locale: ${locale}`, error);
    }
}

/**
 * Clear locale cache (useful for memory management)
 * @param {string} locale - The locale to clear (optional, clears all if not specified)
 */
export function clearLocaleCache(locale) {
    if (locale) {
        // Clear specific locale
        const keysToDelete = [];
        for (const key of localeCache.keys()) {
            if (key.endsWith(`-${locale}`) && !key.endsWith('-en')) {
                keysToDelete.push(key);
            }
        }
        keysToDelete.forEach(key => localeCache.delete(key));
    } else {
        // Clear all except English
        const keysToDelete = [];
        for (const key of localeCache.keys()) {
            if (!key.endsWith('-en')) {
                keysToDelete.push(key);
            }
        }
        keysToDelete.forEach(key => localeCache.delete(key));
    }
}

/**
 * Get currently cached locales
 * @returns {Array<string>} List of cached locale codes
 */
export function getCachedLocales() {
    const locales = new Set();
    for (const key of localeCache.keys()) {
        const locale = key.split('-').slice(1).join('-');
        locales.add(locale);
    }
    return Array.from(locales);
}

// Export for backward compatibility
export default {
    loadLocaleMessages,
    loadAllMessages,
    preloadLocale,
    clearLocaleCache,
    getCachedLocales
};