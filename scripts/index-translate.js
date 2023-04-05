/* eslint-disable global-require */
import {indexLanguage} from '../src/supported-locales';
import * as fs from 'fs';
import * as path from 'path';
import set from 'lodash.set';
import axios from 'axios';
var pinyin = require('chinese-to-pinyin');

const baseUrl = `${process.env.METEOR_DOMAIN}/api`;

let blockTransList = ['extensions', 'blocks'];
let result = {};

blockTransList.forEach((component) => {
    Object.keys(indexLanguage).forEach((lang) => {
        try {
            let langData = JSON.parse(
                fs.readFileSync(path.resolve('editor', component, lang + '.json'), 'utf8')
            );

            Object.entries(langData).forEach(([id, translated]) => {
                if (id.includes('.') || id.includes('_')) {
                    // Regex for remove %n and [] barack in translate string
                    const regex = /(?:%)\d+|\x5b|\x5D/g;
                    let newTranslate = translated.replace(regex, '');
                    let newId = id.toLowerCase();

                    // For convert extension key to have same format with block type --> <category>_<block_id>
                    newId = newId.replace('.', '_');
                    // For getting category name ---> for later use (if have)
                    const [category, blockName] = newId.split('_');
                    // For convert AI category blocks key to have same format with block type ---> <block_id>
                    newId = newId.replace('ai_', '');
                    // For convert operator blocks key to have same format with block type ---> <operator>_<block_id>
                    newId = newId.replace('operators_', 'operator_');
                    // For convert forever block to have same format with block type ---> forever
                    newId = newId.replace('control_forever', 'forever');
                    // For convert my blocks category return block to have same format with block type ---> procedure_return
                    newId = newId.replace('procedure_', 'procedures_');

                    set(result, [newId, lang], newTranslate);

                    if (category) set(result, [newId, 'category'], category);

                    if (lang === 'zh-cn' && newTranslate) {
                        const convertedPinyin = pinyin(newTranslate, {toneToNumber: true}).replace(/[0-9]/g, '');
                        set(result, [newId, 'pinyin'], convertedPinyin);
                    }
                }
            });
        } catch (e) {
            // missingLocales.push(component + ':' + lang + '\n');
        }
    });
});

let newResult = Object.entries(result).map(([id, value]) => ({id, ...value}));

const body = {data: newResult};

axios.post(`${baseUrl}/blocks/index-translate`, body).then(() => console.log('✨✨✨ Complete translate indexing..!!!'))
    .catch(err => console.log('Something went wrong while index translate', err));
