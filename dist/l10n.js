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
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/*! exports provided: default, localeData, localeMap, isRtl */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _locale_data_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./locale-data.js */ "./src/locale-data.js");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "localeData", function() { return _locale_data_js__WEBPACK_IMPORTED_MODULE_0__["default"]; });

/* harmony import */ var _supported_locales_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./supported-locales.js */ "./src/supported-locales.js");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "default", function() { return _supported_locales_js__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "localeMap", function() { return _supported_locales_js__WEBPACK_IMPORTED_MODULE_1__["localeMap"]; });

/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "isRtl", function() { return _supported_locales_js__WEBPACK_IMPORTED_MODULE_1__["isRtl"]; });





/***/ }),

/***/ "./src/locale-data.js":
/*!****************************!*\
  !*** ./src/locale-data.js ***!
  \****************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return localeData; });
/* harmony import */ var _locale_data_en__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./locale-data/en */ "./src/locale-data/en.js");
/* harmony import */ var _locale_data_en__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_locale_data_en__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _locale_data_es__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./locale-data/es */ "./src/locale-data/es.js");
/* harmony import */ var _locale_data_es__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_locale_data_es__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _locale_data_fr__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./locale-data/fr */ "./src/locale-data/fr.js");
/* harmony import */ var _locale_data_fr__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_locale_data_fr__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _locale_data_zh__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./locale-data/zh */ "./src/locale-data/zh.js");
/* harmony import */ var _locale_data_zh__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_locale_data_zh__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _supported_locales_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./supported-locales.js */ "./src/supported-locales.js");
// temporarily we have all the locale data in scratch-l10n





var localeData = [].concat(_locale_data_en__WEBPACK_IMPORTED_MODULE_0___default.a, _locale_data_es__WEBPACK_IMPORTED_MODULE_1___default.a, _locale_data_fr__WEBPACK_IMPORTED_MODULE_2___default.a, _locale_data_zh__WEBPACK_IMPORTED_MODULE_3___default.a);

for (var lang in _supported_locales_js__WEBPACK_IMPORTED_MODULE_4__["customLocales"]) {
  localeData.push(_supported_locales_js__WEBPACK_IMPORTED_MODULE_4__["customLocales"][lang]);
}



/***/ }),

/***/ "./src/locale-data/en.js":
/*!*******************************!*\
  !*** ./src/locale-data/en.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

var __WEBPACK_AMD_DEFINE_FACTORY__, __WEBPACK_AMD_DEFINE_RESULT__;function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

!function (e, a) {
  "object" == ( false ? undefined : _typeof(exports)) && "undefined" != typeof module ? module.exports = a() :  true ? !(__WEBPACK_AMD_DEFINE_FACTORY__ = (a),
				__WEBPACK_AMD_DEFINE_RESULT__ = (typeof __WEBPACK_AMD_DEFINE_FACTORY__ === 'function' ?
				(__WEBPACK_AMD_DEFINE_FACTORY__.call(exports, __webpack_require__, exports, module)) :
				__WEBPACK_AMD_DEFINE_FACTORY__),
				__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)) : (undefined);
}(this, function () {
  "use strict";

  return [{
    locale: "en",
    pluralRuleFunction: function pluralRuleFunction(e, a) {
      var t = String(e).split("."),
          o = !t[1],
          n = Number(t[0]) == e,
          r = n && t[0].slice(-1),
          i = n && t[0].slice(-2);
      return a ? 1 == r && 11 != i ? "one" : 2 == r && 12 != i ? "two" : 3 == r && 13 != i ? "few" : "other" : 1 == e && o ? "one" : "other";
    },
    fields: {
      year: {
        displayName: "year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            one: "in {0} year",
            other: "in {0} years"
          },
          past: {
            one: "{0} year ago",
            other: "{0} years ago"
          }
        }
      },
      "year-short": {
        displayName: "yr.",
        relative: {
          0: "this yr.",
          1: "next yr.",
          "-1": "last yr."
        },
        relativeTime: {
          future: {
            one: "in {0} yr.",
            other: "in {0} yr."
          },
          past: {
            one: "{0} yr. ago",
            other: "{0} yr. ago"
          }
        }
      },
      month: {
        displayName: "month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            one: "in {0} month",
            other: "in {0} months"
          },
          past: {
            one: "{0} month ago",
            other: "{0} months ago"
          }
        }
      },
      "month-short": {
        displayName: "mo.",
        relative: {
          0: "this mo.",
          1: "next mo.",
          "-1": "last mo."
        },
        relativeTime: {
          future: {
            one: "in {0} mo.",
            other: "in {0} mo."
          },
          past: {
            one: "{0} mo. ago",
            other: "{0} mo. ago"
          }
        }
      },
      day: {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      "day-short": {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      hour: {
        displayName: "hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hour",
            other: "in {0} hours"
          },
          past: {
            one: "{0} hour ago",
            other: "{0} hours ago"
          }
        }
      },
      "hour-short": {
        displayName: "hr.",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hr.",
            other: "in {0} hr."
          },
          past: {
            one: "{0} hr. ago",
            other: "{0} hr. ago"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} minute",
            other: "in {0} minutes"
          },
          past: {
            one: "{0} minute ago",
            other: "{0} minutes ago"
          }
        }
      },
      "minute-short": {
        displayName: "min.",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} min.",
            other: "in {0} min."
          },
          past: {
            one: "{0} min. ago",
            other: "{0} min. ago"
          }
        }
      },
      second: {
        displayName: "second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} second",
            other: "in {0} seconds"
          },
          past: {
            one: "{0} second ago",
            other: "{0} seconds ago"
          }
        }
      },
      "second-short": {
        displayName: "sec.",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} sec.",
            other: "in {0} sec."
          },
          past: {
            one: "{0} sec. ago",
            other: "{0} sec. ago"
          }
        }
      }
    }
  }, {
    locale: "en-001",
    parentLocale: "en",
    fields: {
      year: {
        displayName: "year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            one: "in {0} year",
            other: "in {0} years"
          },
          past: {
            one: "{0} year ago",
            other: "{0} years ago"
          }
        }
      },
      "year-short": {
        displayName: "yr",
        relative: {
          0: "this yr.",
          1: "next yr.",
          "-1": "last yr."
        },
        relativeTime: {
          future: {
            one: "in {0} yr",
            other: "in {0} yr"
          },
          past: {
            one: "{0} yr ago",
            other: "{0} yr ago"
          }
        }
      },
      month: {
        displayName: "month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            one: "in {0} month",
            other: "in {0} months"
          },
          past: {
            one: "{0} month ago",
            other: "{0} months ago"
          }
        }
      },
      "month-short": {
        displayName: "mo",
        relative: {
          0: "this mo.",
          1: "next mo.",
          "-1": "last mo."
        },
        relativeTime: {
          future: {
            one: "in {0} mo",
            other: "in {0} mo"
          },
          past: {
            one: "{0} mo ago",
            other: "{0} mo ago"
          }
        }
      },
      day: {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      "day-short": {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      hour: {
        displayName: "hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hour",
            other: "in {0} hours"
          },
          past: {
            one: "{0} hour ago",
            other: "{0} hours ago"
          }
        }
      },
      "hour-short": {
        displayName: "hr",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hr",
            other: "in {0} hr"
          },
          past: {
            one: "{0} hr ago",
            other: "{0} hr ago"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} minute",
            other: "in {0} minutes"
          },
          past: {
            one: "{0} minute ago",
            other: "{0} minutes ago"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} min",
            other: "in {0} min"
          },
          past: {
            one: "{0} min ago",
            other: "{0} min ago"
          }
        }
      },
      second: {
        displayName: "second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} second",
            other: "in {0} seconds"
          },
          past: {
            one: "{0} second ago",
            other: "{0} seconds ago"
          }
        }
      },
      "second-short": {
        displayName: "sec",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} sec",
            other: "in {0} sec"
          },
          past: {
            one: "{0} sec ago",
            other: "{0} sec ago"
          }
        }
      }
    }
  }, {
    locale: "en-150",
    parentLocale: "en-001"
  }, {
    locale: "en-AG",
    parentLocale: "en-001"
  }, {
    locale: "en-AI",
    parentLocale: "en-001"
  }, {
    locale: "en-AS",
    parentLocale: "en"
  }, {
    locale: "en-AT",
    parentLocale: "en-150"
  }, {
    locale: "en-AU",
    parentLocale: "en-001",
    fields: {
      year: {
        displayName: "year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            one: "in {0} year",
            other: "in {0} years"
          },
          past: {
            one: "{0} year ago",
            other: "{0} years ago"
          }
        }
      },
      "year-short": {
        displayName: "yr",
        relative: {
          0: "this yr.",
          1: "next yr.",
          "-1": "last yr."
        },
        relativeTime: {
          future: {
            one: "in {0} yr",
            other: "in {0} yrs"
          },
          past: {
            one: "{0} yr ago",
            other: "{0} yrs ago"
          }
        }
      },
      month: {
        displayName: "month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            one: "in {0} month",
            other: "in {0} months"
          },
          past: {
            one: "{0} month ago",
            other: "{0} months ago"
          }
        }
      },
      "month-short": {
        displayName: "mo.",
        relative: {
          0: "this mo.",
          1: "next mo.",
          "-1": "last mo."
        },
        relativeTime: {
          future: {
            one: "in {0} mo.",
            other: "in {0} mo."
          },
          past: {
            one: "{0} mo. ago",
            other: "{0} mo. ago"
          }
        }
      },
      day: {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      "day-short": {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      hour: {
        displayName: "hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hour",
            other: "in {0} hours"
          },
          past: {
            one: "{0} hour ago",
            other: "{0} hours ago"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hr",
            other: "in {0} hrs"
          },
          past: {
            one: "{0} hr ago",
            other: "{0} hrs ago"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} minute",
            other: "in {0} minutes"
          },
          past: {
            one: "{0} minute ago",
            other: "{0} minutes ago"
          }
        }
      },
      "minute-short": {
        displayName: "min.",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} min.",
            other: "in {0} mins"
          },
          past: {
            one: "{0} min. ago",
            other: "{0} mins ago"
          }
        }
      },
      second: {
        displayName: "second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} second",
            other: "in {0} seconds"
          },
          past: {
            one: "{0} second ago",
            other: "{0} seconds ago"
          }
        }
      },
      "second-short": {
        displayName: "sec.",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} sec.",
            other: "in {0} secs"
          },
          past: {
            one: "{0} sec. ago",
            other: "{0} secs ago"
          }
        }
      }
    }
  }, {
    locale: "en-BB",
    parentLocale: "en-001"
  }, {
    locale: "en-BE",
    parentLocale: "en-001"
  }, {
    locale: "en-BI",
    parentLocale: "en"
  }, {
    locale: "en-BM",
    parentLocale: "en-001"
  }, {
    locale: "en-BS",
    parentLocale: "en-001"
  }, {
    locale: "en-BW",
    parentLocale: "en-001"
  }, {
    locale: "en-BZ",
    parentLocale: "en-001"
  }, {
    locale: "en-CA",
    parentLocale: "en-001",
    fields: {
      year: {
        displayName: "year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            one: "in {0} year",
            other: "in {0} years"
          },
          past: {
            one: "{0} year ago",
            other: "{0} years ago"
          }
        }
      },
      "year-short": {
        displayName: "yr.",
        relative: {
          0: "this yr.",
          1: "next yr.",
          "-1": "last yr."
        },
        relativeTime: {
          future: {
            one: "in {0} yr.",
            other: "in {0} yrs."
          },
          past: {
            one: "{0} yr. ago",
            other: "{0} yrs. ago"
          }
        }
      },
      month: {
        displayName: "month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            one: "in {0} month",
            other: "in {0} months"
          },
          past: {
            one: "{0} month ago",
            other: "{0} months ago"
          }
        }
      },
      "month-short": {
        displayName: "mo.",
        relative: {
          0: "this mo.",
          1: "next mo.",
          "-1": "last mo."
        },
        relativeTime: {
          future: {
            one: "in {0} mo.",
            other: "in {0} mos."
          },
          past: {
            one: "{0} mo. ago",
            other: "{0} mos. ago"
          }
        }
      },
      day: {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      "day-short": {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      hour: {
        displayName: "hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hour",
            other: "in {0} hours"
          },
          past: {
            one: "{0} hour ago",
            other: "{0} hours ago"
          }
        }
      },
      "hour-short": {
        displayName: "hr.",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hr.",
            other: "in {0} hrs."
          },
          past: {
            one: "{0} hr. ago",
            other: "{0} hrs. ago"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} minute",
            other: "in {0} minutes"
          },
          past: {
            one: "{0} minute ago",
            other: "{0} minutes ago"
          }
        }
      },
      "minute-short": {
        displayName: "min.",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} min.",
            other: "in {0} mins."
          },
          past: {
            one: "{0} min. ago",
            other: "{0} mins. ago"
          }
        }
      },
      second: {
        displayName: "second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} second",
            other: "in {0} seconds"
          },
          past: {
            one: "{0} second ago",
            other: "{0} seconds ago"
          }
        }
      },
      "second-short": {
        displayName: "sec.",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} sec.",
            other: "in {0} secs."
          },
          past: {
            one: "{0} sec. ago",
            other: "{0} secs. ago"
          }
        }
      }
    }
  }, {
    locale: "en-CC",
    parentLocale: "en-001"
  }, {
    locale: "en-CH",
    parentLocale: "en-150"
  }, {
    locale: "en-CK",
    parentLocale: "en-001"
  }, {
    locale: "en-CM",
    parentLocale: "en-001"
  }, {
    locale: "en-CX",
    parentLocale: "en-001"
  }, {
    locale: "en-CY",
    parentLocale: "en-001"
  }, {
    locale: "en-DE",
    parentLocale: "en-150"
  }, {
    locale: "en-DG",
    parentLocale: "en-001"
  }, {
    locale: "en-DK",
    parentLocale: "en-150"
  }, {
    locale: "en-DM",
    parentLocale: "en-001"
  }, {
    locale: "en-Dsrt",
    pluralRuleFunction: function pluralRuleFunction(e, a) {
      return "other";
    },
    fields: {
      year: {
        displayName: "Year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            other: "+{0} y"
          },
          past: {
            other: "-{0} y"
          }
        }
      },
      "year-short": {
        displayName: "Year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            other: "+{0} y"
          },
          past: {
            other: "-{0} y"
          }
        }
      },
      month: {
        displayName: "Month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            other: "+{0} m"
          },
          past: {
            other: "-{0} m"
          }
        }
      },
      "month-short": {
        displayName: "Month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            other: "+{0} m"
          },
          past: {
            other: "-{0} m"
          }
        }
      },
      day: {
        displayName: "Day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            other: "+{0} d"
          },
          past: {
            other: "-{0} d"
          }
        }
      },
      "day-short": {
        displayName: "Day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            other: "+{0} d"
          },
          past: {
            other: "-{0} d"
          }
        }
      },
      hour: {
        displayName: "Hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            other: "+{0} h"
          },
          past: {
            other: "-{0} h"
          }
        }
      },
      "hour-short": {
        displayName: "Hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            other: "+{0} h"
          },
          past: {
            other: "-{0} h"
          }
        }
      },
      minute: {
        displayName: "Minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            other: "+{0} min"
          },
          past: {
            other: "-{0} min"
          }
        }
      },
      "minute-short": {
        displayName: "Minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            other: "+{0} min"
          },
          past: {
            other: "-{0} min"
          }
        }
      },
      second: {
        displayName: "Second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            other: "+{0} s"
          },
          past: {
            other: "-{0} s"
          }
        }
      },
      "second-short": {
        displayName: "Second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            other: "+{0} s"
          },
          past: {
            other: "-{0} s"
          }
        }
      }
    }
  }, {
    locale: "en-ER",
    parentLocale: "en-001"
  }, {
    locale: "en-FI",
    parentLocale: "en-150"
  }, {
    locale: "en-FJ",
    parentLocale: "en-001"
  }, {
    locale: "en-FK",
    parentLocale: "en-001"
  }, {
    locale: "en-FM",
    parentLocale: "en-001"
  }, {
    locale: "en-GB",
    parentLocale: "en-001"
  }, {
    locale: "en-GD",
    parentLocale: "en-001"
  }, {
    locale: "en-GG",
    parentLocale: "en-001"
  }, {
    locale: "en-GH",
    parentLocale: "en-001"
  }, {
    locale: "en-GI",
    parentLocale: "en-001"
  }, {
    locale: "en-GM",
    parentLocale: "en-001"
  }, {
    locale: "en-GU",
    parentLocale: "en"
  }, {
    locale: "en-GY",
    parentLocale: "en-001"
  }, {
    locale: "en-HK",
    parentLocale: "en-001"
  }, {
    locale: "en-IE",
    parentLocale: "en-001"
  }, {
    locale: "en-IL",
    parentLocale: "en-001"
  }, {
    locale: "en-IM",
    parentLocale: "en-001"
  }, {
    locale: "en-IN",
    parentLocale: "en-001"
  }, {
    locale: "en-IO",
    parentLocale: "en-001"
  }, {
    locale: "en-JE",
    parentLocale: "en-001"
  }, {
    locale: "en-JM",
    parentLocale: "en-001"
  }, {
    locale: "en-KE",
    parentLocale: "en-001"
  }, {
    locale: "en-KI",
    parentLocale: "en-001"
  }, {
    locale: "en-KN",
    parentLocale: "en-001"
  }, {
    locale: "en-KY",
    parentLocale: "en-001"
  }, {
    locale: "en-LC",
    parentLocale: "en-001"
  }, {
    locale: "en-LR",
    parentLocale: "en-001"
  }, {
    locale: "en-LS",
    parentLocale: "en-001"
  }, {
    locale: "en-MG",
    parentLocale: "en-001"
  }, {
    locale: "en-MH",
    parentLocale: "en"
  }, {
    locale: "en-MO",
    parentLocale: "en-001"
  }, {
    locale: "en-MP",
    parentLocale: "en"
  }, {
    locale: "en-MS",
    parentLocale: "en-001"
  }, {
    locale: "en-MT",
    parentLocale: "en-001"
  }, {
    locale: "en-MU",
    parentLocale: "en-001"
  }, {
    locale: "en-MW",
    parentLocale: "en-001"
  }, {
    locale: "en-MY",
    parentLocale: "en-001"
  }, {
    locale: "en-NA",
    parentLocale: "en-001"
  }, {
    locale: "en-NF",
    parentLocale: "en-001"
  }, {
    locale: "en-NG",
    parentLocale: "en-001"
  }, {
    locale: "en-NL",
    parentLocale: "en-150"
  }, {
    locale: "en-NR",
    parentLocale: "en-001"
  }, {
    locale: "en-NU",
    parentLocale: "en-001"
  }, {
    locale: "en-NZ",
    parentLocale: "en-001"
  }, {
    locale: "en-PG",
    parentLocale: "en-001"
  }, {
    locale: "en-PH",
    parentLocale: "en-001"
  }, {
    locale: "en-PK",
    parentLocale: "en-001"
  }, {
    locale: "en-PN",
    parentLocale: "en-001"
  }, {
    locale: "en-PR",
    parentLocale: "en"
  }, {
    locale: "en-PW",
    parentLocale: "en-001"
  }, {
    locale: "en-RW",
    parentLocale: "en-001"
  }, {
    locale: "en-SB",
    parentLocale: "en-001"
  }, {
    locale: "en-SC",
    parentLocale: "en-001"
  }, {
    locale: "en-SD",
    parentLocale: "en-001"
  }, {
    locale: "en-SE",
    parentLocale: "en-150"
  }, {
    locale: "en-SG",
    parentLocale: "en-001",
    fields: {
      year: {
        displayName: "year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            one: "in {0} year",
            other: "in {0} years"
          },
          past: {
            one: "{0} year ago",
            other: "{0} years ago"
          }
        }
      },
      "year-short": {
        displayName: "yr",
        relative: {
          0: "this yr",
          1: "next yr",
          "-1": "last yr"
        },
        relativeTime: {
          future: {
            one: "in {0} yr",
            other: "in {0} yr"
          },
          past: {
            one: "{0} yr ago",
            other: "{0} yr ago"
          }
        }
      },
      month: {
        displayName: "month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            one: "in {0} month",
            other: "in {0} months"
          },
          past: {
            one: "{0} month ago",
            other: "{0} months ago"
          }
        }
      },
      "month-short": {
        displayName: "mth",
        relative: {
          0: "this mth",
          1: "next mth",
          "-1": "last mth"
        },
        relativeTime: {
          future: {
            one: "in {0} mth",
            other: "in {0} mth"
          },
          past: {
            one: "{0} mth ago",
            other: "{0} mth ago"
          }
        }
      },
      day: {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      "day-short": {
        displayName: "day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            one: "in {0} day",
            other: "in {0} days"
          },
          past: {
            one: "{0} day ago",
            other: "{0} days ago"
          }
        }
      },
      hour: {
        displayName: "hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hour",
            other: "in {0} hours"
          },
          past: {
            one: "{0} hour ago",
            other: "{0} hours ago"
          }
        }
      },
      "hour-short": {
        displayName: "hr",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            one: "in {0} hr",
            other: "in {0} hr"
          },
          past: {
            one: "{0} hr ago",
            other: "{0} hr ago"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} minute",
            other: "in {0} minutes"
          },
          past: {
            one: "{0} minute ago",
            other: "{0} minutes ago"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            one: "in {0} min",
            other: "in {0} min"
          },
          past: {
            one: "{0} min ago",
            other: "{0} min ago"
          }
        }
      },
      second: {
        displayName: "second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} second",
            other: "in {0} seconds"
          },
          past: {
            one: "{0} second ago",
            other: "{0} seconds ago"
          }
        }
      },
      "second-short": {
        displayName: "sec",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            one: "in {0} sec",
            other: "in {0} sec"
          },
          past: {
            one: "{0} sec ago",
            other: "{0} sec ago"
          }
        }
      }
    }
  }, {
    locale: "en-SH",
    parentLocale: "en-001"
  }, {
    locale: "en-SI",
    parentLocale: "en-150"
  }, {
    locale: "en-SL",
    parentLocale: "en-001"
  }, {
    locale: "en-SS",
    parentLocale: "en-001"
  }, {
    locale: "en-SX",
    parentLocale: "en-001"
  }, {
    locale: "en-SZ",
    parentLocale: "en-001"
  }, {
    locale: "en-Shaw",
    pluralRuleFunction: function pluralRuleFunction(e, a) {
      return "other";
    },
    fields: {
      year: {
        displayName: "Year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            other: "+{0} y"
          },
          past: {
            other: "-{0} y"
          }
        }
      },
      "year-short": {
        displayName: "Year",
        relative: {
          0: "this year",
          1: "next year",
          "-1": "last year"
        },
        relativeTime: {
          future: {
            other: "+{0} y"
          },
          past: {
            other: "-{0} y"
          }
        }
      },
      month: {
        displayName: "Month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            other: "+{0} m"
          },
          past: {
            other: "-{0} m"
          }
        }
      },
      "month-short": {
        displayName: "Month",
        relative: {
          0: "this month",
          1: "next month",
          "-1": "last month"
        },
        relativeTime: {
          future: {
            other: "+{0} m"
          },
          past: {
            other: "-{0} m"
          }
        }
      },
      day: {
        displayName: "Day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            other: "+{0} d"
          },
          past: {
            other: "-{0} d"
          }
        }
      },
      "day-short": {
        displayName: "Day",
        relative: {
          0: "today",
          1: "tomorrow",
          "-1": "yesterday"
        },
        relativeTime: {
          future: {
            other: "+{0} d"
          },
          past: {
            other: "-{0} d"
          }
        }
      },
      hour: {
        displayName: "Hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            other: "+{0} h"
          },
          past: {
            other: "-{0} h"
          }
        }
      },
      "hour-short": {
        displayName: "Hour",
        relative: {
          0: "this hour"
        },
        relativeTime: {
          future: {
            other: "+{0} h"
          },
          past: {
            other: "-{0} h"
          }
        }
      },
      minute: {
        displayName: "Minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            other: "+{0} min"
          },
          past: {
            other: "-{0} min"
          }
        }
      },
      "minute-short": {
        displayName: "Minute",
        relative: {
          0: "this minute"
        },
        relativeTime: {
          future: {
            other: "+{0} min"
          },
          past: {
            other: "-{0} min"
          }
        }
      },
      second: {
        displayName: "Second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            other: "+{0} s"
          },
          past: {
            other: "-{0} s"
          }
        }
      },
      "second-short": {
        displayName: "Second",
        relative: {
          0: "now"
        },
        relativeTime: {
          future: {
            other: "+{0} s"
          },
          past: {
            other: "-{0} s"
          }
        }
      }
    }
  }, {
    locale: "en-TC",
    parentLocale: "en-001"
  }, {
    locale: "en-TK",
    parentLocale: "en-001"
  }, {
    locale: "en-TO",
    parentLocale: "en-001"
  }, {
    locale: "en-TT",
    parentLocale: "en-001"
  }, {
    locale: "en-TV",
    parentLocale: "en-001"
  }, {
    locale: "en-TZ",
    parentLocale: "en-001"
  }, {
    locale: "en-UG",
    parentLocale: "en-001"
  }, {
    locale: "en-UM",
    parentLocale: "en"
  }, {
    locale: "en-US",
    parentLocale: "en"
  }, {
    locale: "en-VC",
    parentLocale: "en-001"
  }, {
    locale: "en-VG",
    parentLocale: "en-001"
  }, {
    locale: "en-VI",
    parentLocale: "en"
  }, {
    locale: "en-VU",
    parentLocale: "en-001"
  }, {
    locale: "en-WS",
    parentLocale: "en-001"
  }, {
    locale: "en-ZA",
    parentLocale: "en-001"
  }, {
    locale: "en-ZM",
    parentLocale: "en-001"
  }, {
    locale: "en-ZW",
    parentLocale: "en-001"
  }];
});

/***/ }),

/***/ "./src/locale-data/es.js":
/*!*******************************!*\
  !*** ./src/locale-data/es.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

var __WEBPACK_AMD_DEFINE_FACTORY__, __WEBPACK_AMD_DEFINE_RESULT__;function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

!function (e, a) {
  "object" == ( false ? undefined : _typeof(exports)) && "undefined" != typeof module ? module.exports = a() :  true ? !(__WEBPACK_AMD_DEFINE_FACTORY__ = (a),
				__WEBPACK_AMD_DEFINE_RESULT__ = (typeof __WEBPACK_AMD_DEFINE_FACTORY__ === 'function' ?
				(__WEBPACK_AMD_DEFINE_FACTORY__.call(exports, __webpack_require__, exports, module)) :
				__WEBPACK_AMD_DEFINE_FACTORY__),
				__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)) : (undefined);
}(this, function () {
  "use strict";

  return [{
    locale: "es",
    pluralRuleFunction: function pluralRuleFunction(e, a) {
      return a ? "other" : 1 == e ? "one" : "other";
    },
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} s",
            other: "dentro de {0} s"
          },
          past: {
            one: "hace {0} s",
            other: "hace {0} s"
          }
        }
      }
    }
  }, {
    locale: "es-419",
    parentLocale: "es"
  }, {
    locale: "es-AR",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} días",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} días",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "seg.",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} seg.",
            other: "dentro de {0} seg."
          },
          past: {
            one: "hace {0} seg.",
            other: "hace {0} seg."
          }
        }
      }
    }
  }, {
    locale: "es-BO",
    parentLocale: "es-419"
  }, {
    locale: "es-BR",
    parentLocale: "es-419"
  }, {
    locale: "es-BZ",
    parentLocale: "es-419"
  }, {
    locale: "es-CL",
    parentLocale: "es-419"
  }, {
    locale: "es-CO",
    parentLocale: "es-419"
  }, {
    locale: "es-CR",
    parentLocale: "es-419"
  }, {
    locale: "es-CU",
    parentLocale: "es-419"
  }, {
    locale: "es-DO",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "Año",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "Mes",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "Día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "Minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "Segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} s",
            other: "dentro de {0} s"
          },
          past: {
            one: "hace {0} s",
            other: "hace {0} s"
          }
        }
      }
    }
  }, {
    locale: "es-EA",
    parentLocale: "es"
  }, {
    locale: "es-EC",
    parentLocale: "es-419"
  }, {
    locale: "es-GQ",
    parentLocale: "es"
  }, {
    locale: "es-GT",
    parentLocale: "es-419"
  }, {
    locale: "es-HN",
    parentLocale: "es-419"
  }, {
    locale: "es-IC",
    parentLocale: "es"
  }, {
    locale: "es-MX",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el año próximo",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "en {0} a",
            other: "en {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el mes próximo",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "en {0} mes",
            other: "en {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "en {0} m",
            other: "en {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "en {0} día",
            other: "en {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "en {0} h",
            other: "en {0} n"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "en {0} min",
            other: "en {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "en {0} s",
            other: "en {0} s"
          },
          past: {
            one: "hace {0} s",
            other: "hace {0} s"
          }
        }
      }
    }
  }, {
    locale: "es-NI",
    parentLocale: "es-419"
  }, {
    locale: "es-PA",
    parentLocale: "es-419"
  }, {
    locale: "es-PE",
    parentLocale: "es-419"
  }, {
    locale: "es-PH",
    parentLocale: "es"
  }, {
    locale: "es-PR",
    parentLocale: "es-419"
  }, {
    locale: "es-PY",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "seg.",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} seg.",
            other: "dentro de {0} seg."
          },
          past: {
            one: "hace {0} seg.",
            other: "hace {0} seg."
          }
        }
      }
    }
  }, {
    locale: "es-SV",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "antier",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} s",
            other: "dentro de {0} s"
          },
          past: {
            one: "hace {0} s",
            other: "hace {0} s"
          }
        }
      }
    }
  }, {
    locale: "es-US",
    parentLocale: "es-419",
    fields: {
      year: {
        displayName: "año",
        relative: {
          0: "este año",
          1: "el año próximo",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} año",
            other: "dentro de {0} años"
          },
          past: {
            one: "hace {0} año",
            other: "hace {0} años"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "este año",
          1: "el próximo año",
          "-1": "el año pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} a",
            other: "dentro de {0} a"
          },
          past: {
            one: "hace {0} a",
            other: "hace {0} a"
          }
        }
      },
      month: {
        displayName: "mes",
        relative: {
          0: "este mes",
          1: "el mes próximo",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} mes",
            other: "dentro de {0} meses"
          },
          past: {
            one: "hace {0} mes",
            other: "hace {0} meses"
          }
        }
      },
      "month-short": {
        displayName: "m",
        relative: {
          0: "este mes",
          1: "el próximo mes",
          "-1": "el mes pasado"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} m",
            other: "dentro de {0} m"
          },
          past: {
            one: "hace {0} m",
            other: "hace {0} m"
          }
        }
      },
      day: {
        displayName: "día",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      "day-short": {
        displayName: "d",
        relative: {
          0: "hoy",
          1: "mañana",
          2: "pasado mañana",
          "-2": "anteayer",
          "-1": "ayer"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} día",
            other: "dentro de {0} días"
          },
          past: {
            one: "hace {0} día",
            other: "hace {0} días"
          }
        }
      },
      hour: {
        displayName: "hora",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} hora",
            other: "dentro de {0} horas"
          },
          past: {
            one: "hace {0} hora",
            other: "hace {0} horas"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "esta hora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} h",
            other: "dentro de {0} h"
          },
          past: {
            one: "hace {0} h",
            other: "hace {0} h"
          }
        }
      },
      minute: {
        displayName: "minuto",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} minuto",
            other: "dentro de {0} minutos"
          },
          past: {
            one: "hace {0} minuto",
            other: "hace {0} minutos"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "este minuto"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} min",
            other: "dentro de {0} min"
          },
          past: {
            one: "hace {0} min",
            other: "hace {0} min"
          }
        }
      },
      second: {
        displayName: "segundo",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} segundo",
            other: "dentro de {0} segundos"
          },
          past: {
            one: "hace {0} segundo",
            other: "hace {0} segundos"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "ahora"
        },
        relativeTime: {
          future: {
            one: "dentro de {0} s",
            other: "dentro de {0} s"
          },
          past: {
            one: "hace {0} s",
            other: "hace {0} s"
          }
        }
      }
    }
  }, {
    locale: "es-UY",
    parentLocale: "es-419"
  }, {
    locale: "es-VE",
    parentLocale: "es-419"
  }];
});

/***/ }),

/***/ "./src/locale-data/fr.js":
/*!*******************************!*\
  !*** ./src/locale-data/fr.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

var __WEBPACK_AMD_DEFINE_FACTORY__, __WEBPACK_AMD_DEFINE_RESULT__;function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

!function (e, a) {
  "object" == ( false ? undefined : _typeof(exports)) && "undefined" != typeof module ? module.exports = a() :  true ? !(__WEBPACK_AMD_DEFINE_FACTORY__ = (a),
				__WEBPACK_AMD_DEFINE_RESULT__ = (typeof __WEBPACK_AMD_DEFINE_FACTORY__ === 'function' ?
				(__WEBPACK_AMD_DEFINE_FACTORY__.call(exports, __webpack_require__, exports, module)) :
				__WEBPACK_AMD_DEFINE_FACTORY__),
				__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)) : (undefined);
}(this, function () {
  "use strict";

  return [{
    locale: "fr",
    pluralRuleFunction: function pluralRuleFunction(e, a) {
      return a ? 1 == e ? "one" : "other" : e >= 0 && e < 2 ? "one" : "other";
    },
    fields: {
      year: {
        displayName: "année",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "dans {0} an",
            other: "dans {0} ans"
          },
          past: {
            one: "il y a {0} an",
            other: "il y a {0} ans"
          }
        }
      },
      "year-short": {
        displayName: "an",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "dans {0} a",
            other: "dans {0} a"
          },
          past: {
            one: "il y a {0} a",
            other: "il y a {0} a"
          }
        }
      },
      month: {
        displayName: "mois",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} mois",
            other: "dans {0} mois"
          },
          past: {
            one: "il y a {0} mois",
            other: "il y a {0} mois"
          }
        }
      },
      "month-short": {
        displayName: "m.",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} m.",
            other: "dans {0} m."
          },
          past: {
            one: "il y a {0} m.",
            other: "il y a {0} m."
          }
        }
      },
      day: {
        displayName: "jour",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} jour",
            other: "dans {0} jours"
          },
          past: {
            one: "il y a {0} jour",
            other: "il y a {0} jours"
          }
        }
      },
      "day-short": {
        displayName: "j",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} j",
            other: "dans {0} j"
          },
          past: {
            one: "il y a {0} j",
            other: "il y a {0} j"
          }
        }
      },
      hour: {
        displayName: "heure",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} heure",
            other: "dans {0} heures"
          },
          past: {
            one: "il y a {0} heure",
            other: "il y a {0} heures"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} h",
            other: "dans {0} h"
          },
          past: {
            one: "il y a {0} h",
            other: "il y a {0} h"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} minute",
            other: "dans {0} minutes"
          },
          past: {
            one: "il y a {0} minute",
            other: "il y a {0} minutes"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} min",
            other: "dans {0} min"
          },
          past: {
            one: "il y a {0} min",
            other: "il y a {0} min"
          }
        }
      },
      second: {
        displayName: "seconde",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} seconde",
            other: "dans {0} secondes"
          },
          past: {
            one: "il y a {0} seconde",
            other: "il y a {0} secondes"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} s",
            other: "dans {0} s"
          },
          past: {
            one: "il y a {0} s",
            other: "il y a {0} s"
          }
        }
      }
    }
  }, {
    locale: "fr-BE",
    parentLocale: "fr"
  }, {
    locale: "fr-BF",
    parentLocale: "fr"
  }, {
    locale: "fr-BI",
    parentLocale: "fr"
  }, {
    locale: "fr-BJ",
    parentLocale: "fr"
  }, {
    locale: "fr-BL",
    parentLocale: "fr"
  }, {
    locale: "fr-CA",
    parentLocale: "fr",
    fields: {
      year: {
        displayName: "année",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "Dans {0} an",
            other: "Dans {0} ans"
          },
          past: {
            one: "Il y a {0} an",
            other: "Il y a {0} ans"
          }
        }
      },
      "year-short": {
        displayName: "a",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "dans {0} a",
            other: "dans {0} a"
          },
          past: {
            one: "il y a {0} a",
            other: "il y a {0} a"
          }
        }
      },
      month: {
        displayName: "mois",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} mois",
            other: "dans {0} mois"
          },
          past: {
            one: "il y a {0} mois",
            other: "il y a {0} mois"
          }
        }
      },
      "month-short": {
        displayName: "m.",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} m.",
            other: "dans {0} m."
          },
          past: {
            one: "il y a {0} m.",
            other: "il y a {0} m."
          }
        }
      },
      day: {
        displayName: "jour",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} jour",
            other: "dans {0} jours"
          },
          past: {
            one: "il y a {0} jour",
            other: "il y a {0} jours"
          }
        }
      },
      "day-short": {
        displayName: "j",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} j",
            other: "dans {0} j"
          },
          past: {
            one: "il y a {0} j",
            other: "il y a {0} j"
          }
        }
      },
      hour: {
        displayName: "heure",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} heure",
            other: "dans {0} heures"
          },
          past: {
            one: "il y a {0} heure",
            other: "il y a {0} heures"
          }
        }
      },
      "hour-short": {
        displayName: "h",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} h",
            other: "dans {0} h"
          },
          past: {
            one: "il y a {0} h",
            other: "il y a {0} h"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} minute",
            other: "dans {0} minutes"
          },
          past: {
            one: "il y a {0} minute",
            other: "il y a {0} minutes"
          }
        }
      },
      "minute-short": {
        displayName: "min",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} min",
            other: "dans {0} min"
          },
          past: {
            one: "il y a {0} min",
            other: "il y a {0} min"
          }
        }
      },
      second: {
        displayName: "seconde",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} seconde",
            other: "dans {0} secondes"
          },
          past: {
            one: "il y a {0} seconde",
            other: "il y a {0} secondes"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} s",
            other: "dans {0} s"
          },
          past: {
            one: "il y a {0} s",
            other: "il y a {0} s"
          }
        }
      }
    }
  }, {
    locale: "fr-CD",
    parentLocale: "fr"
  }, {
    locale: "fr-CF",
    parentLocale: "fr"
  }, {
    locale: "fr-CG",
    parentLocale: "fr"
  }, {
    locale: "fr-CH",
    parentLocale: "fr"
  }, {
    locale: "fr-CI",
    parentLocale: "fr"
  }, {
    locale: "fr-CM",
    parentLocale: "fr"
  }, {
    locale: "fr-DJ",
    parentLocale: "fr"
  }, {
    locale: "fr-DZ",
    parentLocale: "fr"
  }, {
    locale: "fr-GA",
    parentLocale: "fr"
  }, {
    locale: "fr-GF",
    parentLocale: "fr"
  }, {
    locale: "fr-GN",
    parentLocale: "fr"
  }, {
    locale: "fr-GP",
    parentLocale: "fr"
  }, {
    locale: "fr-GQ",
    parentLocale: "fr"
  }, {
    locale: "fr-HT",
    parentLocale: "fr",
    fields: {
      year: {
        displayName: "année",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "dans {0} an",
            other: "dans {0} ans"
          },
          past: {
            one: "il y a {0} an",
            other: "il y a {0} ans"
          }
        }
      },
      "year-short": {
        displayName: "an",
        relative: {
          0: "cette année",
          1: "l’année prochaine",
          "-1": "l’année dernière"
        },
        relativeTime: {
          future: {
            one: "dans {0} a",
            other: "dans {0} a"
          },
          past: {
            one: "il y a {0} a",
            other: "il y a {0} a"
          }
        }
      },
      month: {
        displayName: "mois",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} mois",
            other: "dans {0} mois"
          },
          past: {
            one: "il y a {0} mois",
            other: "il y a {0} mois"
          }
        }
      },
      "month-short": {
        displayName: "m.",
        relative: {
          0: "ce mois-ci",
          1: "le mois prochain",
          "-1": "le mois dernier"
        },
        relativeTime: {
          future: {
            one: "dans {0} m.",
            other: "dans {0} m."
          },
          past: {
            one: "il y a {0} m.",
            other: "il y a {0} m."
          }
        }
      },
      day: {
        displayName: "jour",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} jour",
            other: "dans {0} jours"
          },
          past: {
            one: "il y a {0} jour",
            other: "il y a {0} jours"
          }
        }
      },
      "day-short": {
        displayName: "jr.",
        relative: {
          0: "aujourd’hui",
          1: "demain",
          2: "après-demain",
          "-2": "avant-hier",
          "-1": "hier"
        },
        relativeTime: {
          future: {
            one: "dans {0} j",
            other: "dans {0} j"
          },
          past: {
            one: "il y a {0} j",
            other: "il y a {0} j"
          }
        }
      },
      hour: {
        displayName: "heure",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} heure",
            other: "dans {0} heures"
          },
          past: {
            one: "il y a {0} heure",
            other: "il y a {0} heures"
          }
        }
      },
      "hour-short": {
        displayName: "hr",
        relative: {
          0: "cette heure-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} h",
            other: "dans {0} h"
          },
          past: {
            one: "il y a {0} h",
            other: "il y a {0} h"
          }
        }
      },
      minute: {
        displayName: "minute",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} minute",
            other: "dans {0} minutes"
          },
          past: {
            one: "il y a {0} minute",
            other: "il y a {0} minutes"
          }
        }
      },
      "minute-short": {
        displayName: "min.",
        relative: {
          0: "cette minute-ci"
        },
        relativeTime: {
          future: {
            one: "dans {0} min",
            other: "dans {0} min"
          },
          past: {
            one: "il y a {0} min",
            other: "il y a {0} min"
          }
        }
      },
      second: {
        displayName: "seconde",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} seconde",
            other: "dans {0} secondes"
          },
          past: {
            one: "il y a {0} seconde",
            other: "il y a {0} secondes"
          }
        }
      },
      "second-short": {
        displayName: "s",
        relative: {
          0: "maintenant"
        },
        relativeTime: {
          future: {
            one: "dans {0} s",
            other: "dans {0} s"
          },
          past: {
            one: "il y a {0} s",
            other: "il y a {0} s"
          }
        }
      }
    }
  }, {
    locale: "fr-KM",
    parentLocale: "fr"
  }, {
    locale: "fr-LU",
    parentLocale: "fr"
  }, {
    locale: "fr-MA",
    parentLocale: "fr"
  }, {
    locale: "fr-MC",
    parentLocale: "fr"
  }, {
    locale: "fr-MF",
    parentLocale: "fr"
  }, {
    locale: "fr-MG",
    parentLocale: "fr"
  }, {
    locale: "fr-ML",
    parentLocale: "fr"
  }, {
    locale: "fr-MQ",
    parentLocale: "fr"
  }, {
    locale: "fr-MR",
    parentLocale: "fr"
  }, {
    locale: "fr-MU",
    parentLocale: "fr"
  }, {
    locale: "fr-NC",
    parentLocale: "fr"
  }, {
    locale: "fr-NE",
    parentLocale: "fr"
  }, {
    locale: "fr-PF",
    parentLocale: "fr"
  }, {
    locale: "fr-PM",
    parentLocale: "fr"
  }, {
    locale: "fr-RE",
    parentLocale: "fr"
  }, {
    locale: "fr-RW",
    parentLocale: "fr"
  }, {
    locale: "fr-SC",
    parentLocale: "fr"
  }, {
    locale: "fr-SN",
    parentLocale: "fr"
  }, {
    locale: "fr-SY",
    parentLocale: "fr"
  }, {
    locale: "fr-TD",
    parentLocale: "fr"
  }, {
    locale: "fr-TG",
    parentLocale: "fr"
  }, {
    locale: "fr-TN",
    parentLocale: "fr"
  }, {
    locale: "fr-VU",
    parentLocale: "fr"
  }, {
    locale: "fr-WF",
    parentLocale: "fr"
  }, {
    locale: "fr-YT",
    parentLocale: "fr"
  }];
});

/***/ }),

/***/ "./src/locale-data/zh.js":
/*!*******************************!*\
  !*** ./src/locale-data/zh.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

var __WEBPACK_AMD_DEFINE_FACTORY__, __WEBPACK_AMD_DEFINE_RESULT__;function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

!function (e, t) {
  "object" == ( false ? undefined : _typeof(exports)) && "undefined" != typeof module ? module.exports = t() :  true ? !(__WEBPACK_AMD_DEFINE_FACTORY__ = (t),
				__WEBPACK_AMD_DEFINE_RESULT__ = (typeof __WEBPACK_AMD_DEFINE_FACTORY__ === 'function' ?
				(__WEBPACK_AMD_DEFINE_FACTORY__.call(exports, __webpack_require__, exports, module)) :
				__WEBPACK_AMD_DEFINE_FACTORY__),
				__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)) : (undefined);
}(this, function () {
  "use strict";

  return [{
    locale: "zh",
    pluralRuleFunction: function pluralRuleFunction(e, t) {
      return "other";
    },
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      hour: {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      "hour-short": {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      minute: {
        displayName: "分钟",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      "minute-short": {
        displayName: "分",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒钟后"
          },
          past: {
            other: "{0}秒钟前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hans",
    parentLocale: "zh"
  }, {
    locale: "zh-Hans-HK",
    parentLocale: "zh-Hans",
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      hour: {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      "hour-short": {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      minute: {
        displayName: "分钟",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      "minute-short": {
        displayName: "分",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hans-MO",
    parentLocale: "zh-Hans",
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      hour: {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      "hour-short": {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      minute: {
        displayName: "分钟",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      "minute-short": {
        displayName: "分",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hans-SG",
    parentLocale: "zh-Hans",
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0}年后"
          },
          past: {
            other: "{0}年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下个月",
          "-1": "上个月"
        },
        relativeTime: {
          future: {
            other: "{0}个月后"
          },
          past: {
            other: "{0}个月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "后天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0}天后"
          },
          past: {
            other: "{0}天前"
          }
        }
      },
      hour: {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      "hour-short": {
        displayName: "小时",
        relative: {
          0: "这一时间 / 此时"
        },
        relativeTime: {
          future: {
            other: "{0}小时后"
          },
          past: {
            other: "{0}小时前"
          }
        }
      },
      minute: {
        displayName: "分钟",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      "minute-short": {
        displayName: "分",
        relative: {
          0: "此刻"
        },
        relativeTime: {
          future: {
            other: "{0}分钟后"
          },
          past: {
            other: "{0}分钟前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "现在"
        },
        relativeTime: {
          future: {
            other: "{0}秒后"
          },
          past: {
            other: "{0}秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hant",
    pluralRuleFunction: function pluralRuleFunction(e, t) {
      return "other";
    },
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0} 年後"
          },
          past: {
            other: "{0} 年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "明年",
          "-1": "去年"
        },
        relativeTime: {
          future: {
            other: "{0} 年後"
          },
          past: {
            other: "{0} 年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下個月",
          "-1": "上個月"
        },
        relativeTime: {
          future: {
            other: "{0} 個月後"
          },
          past: {
            other: "{0} 個月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下個月",
          "-1": "上個月"
        },
        relativeTime: {
          future: {
            other: "{0} 個月後"
          },
          past: {
            other: "{0} 個月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "後天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0} 天後"
          },
          past: {
            other: "{0} 天前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今天",
          1: "明天",
          2: "後天",
          "-2": "前天",
          "-1": "昨天"
        },
        relativeTime: {
          future: {
            other: "{0} 天後"
          },
          past: {
            other: "{0} 天前"
          }
        }
      },
      hour: {
        displayName: "小時",
        relative: {
          0: "這一小時"
        },
        relativeTime: {
          future: {
            other: "{0} 小時後"
          },
          past: {
            other: "{0} 小時前"
          }
        }
      },
      "hour-short": {
        displayName: "小時",
        relative: {
          0: "這一小時"
        },
        relativeTime: {
          future: {
            other: "{0} 小時後"
          },
          past: {
            other: "{0} 小時前"
          }
        }
      },
      minute: {
        displayName: "分鐘",
        relative: {
          0: "這一分鐘"
        },
        relativeTime: {
          future: {
            other: "{0} 分鐘後"
          },
          past: {
            other: "{0} 分鐘前"
          }
        }
      },
      "minute-short": {
        displayName: "分鐘",
        relative: {
          0: "這一分鐘"
        },
        relativeTime: {
          future: {
            other: "{0} 分鐘後"
          },
          past: {
            other: "{0} 分鐘前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "現在"
        },
        relativeTime: {
          future: {
            other: "{0} 秒後"
          },
          past: {
            other: "{0} 秒前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "現在"
        },
        relativeTime: {
          future: {
            other: "{0} 秒後"
          },
          past: {
            other: "{0} 秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hant-HK",
    parentLocale: "zh-Hant",
    fields: {
      year: {
        displayName: "年",
        relative: {
          0: "今年",
          1: "下年",
          "-1": "上年"
        },
        relativeTime: {
          future: {
            other: "{0} 年後"
          },
          past: {
            other: "{0} 年前"
          }
        }
      },
      "year-short": {
        displayName: "年",
        relative: {
          0: "今年",
          1: "下年",
          "-1": "上年"
        },
        relativeTime: {
          future: {
            other: "{0} 年後"
          },
          past: {
            other: "{0} 年前"
          }
        }
      },
      month: {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下個月",
          "-1": "上個月"
        },
        relativeTime: {
          future: {
            other: "{0} 個月後"
          },
          past: {
            other: "{0} 個月前"
          }
        }
      },
      "month-short": {
        displayName: "月",
        relative: {
          0: "本月",
          1: "下個月",
          "-1": "上個月"
        },
        relativeTime: {
          future: {
            other: "{0} 個月後"
          },
          past: {
            other: "{0} 個月前"
          }
        }
      },
      day: {
        displayName: "日",
        relative: {
          0: "今日",
          1: "明日",
          2: "後日",
          "-2": "前日",
          "-1": "昨日"
        },
        relativeTime: {
          future: {
            other: "{0} 日後"
          },
          past: {
            other: "{0} 日前"
          }
        }
      },
      "day-short": {
        displayName: "日",
        relative: {
          0: "今日",
          1: "明日",
          2: "後日",
          "-2": "前日",
          "-1": "昨日"
        },
        relativeTime: {
          future: {
            other: "{0} 日後"
          },
          past: {
            other: "{0} 日前"
          }
        }
      },
      hour: {
        displayName: "小時",
        relative: {
          0: "這個小時"
        },
        relativeTime: {
          future: {
            other: "{0} 小時後"
          },
          past: {
            other: "{0} 小時前"
          }
        }
      },
      "hour-short": {
        displayName: "小時",
        relative: {
          0: "這個小時"
        },
        relativeTime: {
          future: {
            other: "{0} 小時後"
          },
          past: {
            other: "{0} 小時前"
          }
        }
      },
      minute: {
        displayName: "分鐘",
        relative: {
          0: "這分鐘"
        },
        relativeTime: {
          future: {
            other: "{0} 分鐘後"
          },
          past: {
            other: "{0} 分鐘前"
          }
        }
      },
      "minute-short": {
        displayName: "分鐘",
        relative: {
          0: "這分鐘"
        },
        relativeTime: {
          future: {
            other: "{0} 分鐘後"
          },
          past: {
            other: "{0} 分鐘前"
          }
        }
      },
      second: {
        displayName: "秒",
        relative: {
          0: "現在"
        },
        relativeTime: {
          future: {
            other: "{0} 秒後"
          },
          past: {
            other: "{0} 秒前"
          }
        }
      },
      "second-short": {
        displayName: "秒",
        relative: {
          0: "現在"
        },
        relativeTime: {
          future: {
            other: "{0} 秒後"
          },
          past: {
            other: "{0} 秒前"
          }
        }
      }
    }
  }, {
    locale: "zh-Hant-MO",
    parentLocale: "zh-Hant-HK"
  }];
});

/***/ }),

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
//# sourceMappingURL=l10n.js.map