#!/usr/bin/env node

/*
Generates individual locale files for lazy loading.
Creates:
- locales/editor-msgs-en.js (bundled with main app)
- locales/editor-msgs-[locale].js (lazy loaded)
- locales/locale-manifest.json (list of available locales)
*/

import * as fs from 'fs';
import * as path from 'path';
import {sync as mkdirpSync} from 'mkdirp';
import defaultsDeep from 'lodash.defaultsdeep';
import locales from '../src/supported-locales.js';

const MSGS_DIR = './locales/';
mkdirpSync(MSGS_DIR);
let missingLocales = [];
let availableLocales = [];

const combineJson = (component) => {
    return Object.keys(locales).reduce((collection, lang) => {
        try {
            let langData = JSON.parse(
                fs.readFileSync(path.resolve('editor', component, lang + '.json'), 'utf8')
            );
            collection[lang] = langData;
        } catch (e) {
            missingLocales.push(component + ':' + lang + '\n');
        }
        return collection;
    }, {});
};

// Generate individual block message files per language
let blocksMessages = combineJson('blocks');
Object.keys(blocksMessages).forEach((lang) => {
    let blockData =
        '// GENERATED FILE:\n' +
        'export default ' +
        JSON.stringify(blocksMessages[lang], null, 2) +
        ';\n';
    fs.writeFileSync(MSGS_DIR + `blocks-msgs-${lang}.js`, blockData);

    // Also generate CommonJS version for compatibility
    let blockData2 =
        '// GENERATED FILE:\n' +
        'module.exports = ' +
        JSON.stringify(blocksMessages[lang], null, 2) +
        ';\n';
    fs.writeFileSync(MSGS_DIR + `blocks-msgs-${lang}-cjs.js`, blockData2);
});

// Generate messages for GUI components per language
let components = ['interface', 'extensions', 'paint-editor'];
let editorMsgsByLang = {};

// First collect all messages by language
Object.keys(locales).forEach((lang) => {
    editorMsgsByLang[lang] = {};
});

components.forEach((component) => {
    let messages = combineJson(component);

    // Generate individual component files per language
    Object.keys(messages).forEach((lang) => {
        let data =
            '// GENERATED FILE:\n' +
            'export default ' +
            JSON.stringify(messages[lang], null, 2) +
            ';\n';
        fs.writeFileSync(MSGS_DIR + `${component}-msgs-${lang}.js`, data);

        // Merge into editor messages
        defaultsDeep(editorMsgsByLang[lang], messages[lang]);
    });
});

// Generate combined editor-msgs files per language
Object.keys(editorMsgsByLang).forEach((lang) => {
    if (Object.keys(editorMsgsByLang[lang]).length > 0) {
        let editorData =
            '// GENERATED FILE:\n' +
            'export default ' +
            JSON.stringify(editorMsgsByLang[lang], null, 2) +
            ';\n';
        fs.writeFileSync(MSGS_DIR + `editor-msgs-${lang}.js`, editorData);
        availableLocales.push(lang);
    }
});

// Create locale manifest for dynamic loading
const manifest = {
    locales: availableLocales,
    default: 'en',
    chunks: availableLocales.reduce((acc, locale) => {
        acc[locale] = {
            editor: `editor-msgs-${locale}.js`,
            blocks: `blocks-msgs-${locale}.js`,
            interface: `interface-msgs-${locale}.js`,
            extensions: `extensions-msgs-${locale}.js`,
            paintEditor: `paint-editor-msgs-${locale}.js`
        };
        return acc;
    }, {})
};

fs.writeFileSync(
    MSGS_DIR + 'locale-manifest.json',
    JSON.stringify(manifest, null, 2)
);

// Also create the traditional combined files for backward compatibility
let allEditorMsgs = {};
let allBlocksMsgs = {};

Object.keys(editorMsgsByLang).forEach((lang) => {
    allEditorMsgs[lang] = editorMsgsByLang[lang];
    if (blocksMessages[lang]) {
        allBlocksMsgs[lang] = blocksMessages[lang];
    }
});

// Write backward-compatible combined files
let editorData =
    '// GENERATED FILE:\n' +
    '// This file is for backward compatibility only.\n' +
    '// New code should use per-language imports.\n' +
    'export default ' +
    JSON.stringify(allEditorMsgs, null, 2) +
    ';\n';
fs.writeFileSync(MSGS_DIR + 'editor-msgs.js', editorData);

let blockData =
    '// GENERATED FILE:\n' +
    '// This file is for backward compatibility only.\n' +
    '// New code should use per-language imports.\n' +
    'export default ' +
    JSON.stringify(allBlocksMsgs, null, 2) +
    ';\n';
fs.writeFileSync(MSGS_DIR + 'blocks-msgs.js', blockData);

// Write CommonJS version for compatibility
let blockData2 =
    '// GENERATED FILE:\n' +
    '// This file is for backward compatibility only.\n' +
    '// New code should use per-language imports.\n' +
    'module.exports = ' +
    JSON.stringify(allBlocksMsgs, null, 2) +
    ';\n';
fs.writeFileSync(MSGS_DIR + 'blocks-msgs-2.js', blockData2);

console.log(`Generated locale files for ${availableLocales.length} languages`);
console.log('Available locales:', availableLocales.join(', '));

if (missingLocales.length > 0) {
    process.stdout.write('missing locales:\n' + missingLocales.toString());
    // Don't exit with error for missing locales in lazy loading
    // process.exit(1);
}