module.exports =
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/supported-locales.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/supported-locales.js":
/*!**********************************!*\
  !*** ./src/supported-locales.js ***!
  \**********************************/
/*! exports provided: default, customLocales, localeMap, isRtl */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return locales; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "customLocales", function() { return customLocales; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "localeMap", function() { return localeMap; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "isRtl", function() { return isRtl; });
/**
 * Currently supported locales for the Scratch Project
 * @type {Object} Key Value pairs of locale code: Language name written in the language
 */
var locales = {
  'en': {
    name: 'English'
  },
  'es': {
    name: 'Español (España)'
  },
  'fr': {
    name: 'Français'
  },
  'zh-cn': {
    name: '简体中文'
  }
};
var customLocales = {
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
var localeMap = {
  'aa-dj': 'aa_DJ',
  'es-419': 'es_419',
  // ja-Hira: no map - it's 'ja-Hira' on transifex
  'pt-br': 'pt_BR',
  'zh-cn': 'zh_CN',
  'zh-tw': 'zh_TW'
}; // list of RTL locales supported, and a function to check whether a locale is RTL

var rtlLocales = ['ar', 'ckb', 'fa', 'he'];

var isRtl = function isRtl(locale) {
  return rtlLocales.indexOf(locale) !== -1;
};



/***/ })

/******/ });
//# sourceMappingURL=supportedLocales.js.map