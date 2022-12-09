/* eslint-disable global-require */
import {indexLanguage} from '../src/supported-locales';
import * as fs from 'fs';
import * as path from 'path';
import set from 'lodash/set';
import axios from 'axios';

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
                    set(result, [id.toLowerCase().replaceAll('.', '_'), lang], translated);
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
