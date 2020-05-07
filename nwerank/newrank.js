function i(e) {
                    for (var t, n, a = "", i = -1; ++i < e.length; )
                        t = e.charCodeAt(i),
                        n = i + 1 < e.length ? e.charCodeAt(i + 1) : 0,
                        55296 <= t && t <= 56319 && 56320 <= n && n <= 57343 && (t = 65536 + ((1023 & t) << 10) + (1023 & n),
                        i++),
                        t <= 127 ? a += String.fromCharCode(t) : t <= 2047 ? a += String.fromCharCode(192 | t >>> 6 & 31, 128 | 63 & t) : t <= 65535 ? a += String.fromCharCode(224 | t >>> 12 & 15, 128 | t >>> 6 & 63, 128 | 63 & t) : t <= 2097151 && (a += String.fromCharCode(240 | t >>> 18 & 7, 128 | t >>> 12 & 63, 128 | t >>> 6 & 63, 128 | 63 & t));
                    return a
                }
nonce = function() {
                     for (var e = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], t = 0; t < 500; t++)
                         for (var n = "", a = 0; a < 9; a++) {
                             var i = Math.floor(16 * Math.random());
                             n += e[i]
                         }
                     return n
                 }

//
//function r(e) {
//                     for (var t = "", n = 0; n < 32 * e.length; n += 8)
//                         t += String.fromCharCode(e[n >> 5] >>> n % 32 & 255);
//                     return t
//                 }


function xyz(e){
    function t(e) {
        return a(n(i(e)))
    }
    function n(e) {
        return r(c(o(e), 8 * e.length))
    }
    function a(e) {
        try {} catch (t) {
            f = 0
        }
        for (var n, a = f ? "0123456789ABCDEF" : "0123456789abcdef", i = "", o = 0; o < e.length; o++)
            n = e.charCodeAt(o),
            i += a.charAt(n >>> 4 & 15) + a.charAt(15 & n);
        return i
    }
    function i(e) {
        for (var t, n, a = "", i = -1; ++i < e.length; )
            t = e.charCodeAt(i),
            n = i + 1 < e.length ? e.charCodeAt(i + 1) : 0,
            55296 <= t && t <= 56319 && 56320 <= n && n <= 57343 && (t = 65536 + ((1023 & t) << 10) + (1023 & n),
            i++),
            t <= 127 ? a += String.fromCharCode(t) : t <= 2047 ? a += String.fromCharCode(192 | t >>> 6 & 31, 128 | 63 & t) : t <= 65535 ? a += String.fromCharCode(224 | t >>> 12 & 15, 128 | t >>> 6 & 63, 128 | 63 & t) : t <= 2097151 && (a += String.fromCharCode(240 | t >>> 18 & 7, 128 | t >>> 12 & 63, 128 | t >>> 6 & 63, 128 | 63 & t));
        return a
    }
    function o(e) {
        for (var t = Array(e.length >> 2), n = 0; n < t.length; n++)
            t[n] = 0;
        for (var n = 0; n < 8 * e.length; n += 8)
            t[n >> 5] |= (255 & e.charCodeAt(n / 8)) << n % 32;
        return t
    }
    function r(e) {
        for (var t = "", n = 0; n < 32 * e.length; n += 8)
            t += String.fromCharCode(e[n >> 5] >>> n % 32 & 255);
        return t
    }
    function c(e, t) {
        e[t >> 5] |= 128 << t % 32,
        e[(t + 64 >>> 9 << 4) + 14] = t;
        for (var n = 1732584193, a = -271733879, i = -1732584194, o = 271733878, r = 0; r < e.length; r += 16) {
            var c = n
              , s = a
              , h = i
              , f = o;
            n = l(n, a, i, o, e[r + 0], 7, -680876936),
            o = l(o, n, a, i, e[r + 1], 12, -389564586),
            i = l(i, o, n, a, e[r + 2], 17, 606105819),
            a = l(a, i, o, n, e[r + 3], 22, -1044525330),
            n = l(n, a, i, o, e[r + 4], 7, -176418897),
            o = l(o, n, a, i, e[r + 5], 12, 1200080426),
            i = l(i, o, n, a, e[r + 6], 17, -1473231341),
            a = l(a, i, o, n, e[r + 7], 22, -45705983),
            n = l(n, a, i, o, e[r + 8], 7, 1770035416),
            o = l(o, n, a, i, e[r + 9], 12, -1958414417),
            i = l(i, o, n, a, e[r + 10], 17, -42063),
            a = l(a, i, o, n, e[r + 11], 22, -1990404162),
            n = l(n, a, i, o, e[r + 12], 7, 1804603682),
            o = l(o, n, a, i, e[r + 13], 12, -40341101),
            i = l(i, o, n, a, e[r + 14], 17, -1502002290),
            a = l(a, i, o, n, e[r + 15], 22, 1236535329),
            n = u(n, a, i, o, e[r + 1], 5, -165796510),
            o = u(o, n, a, i, e[r + 6], 9, -1069501632),
            i = u(i, o, n, a, e[r + 11], 14, 643717713),
            a = u(a, i, o, n, e[r + 0], 20, -373897302),
            n = u(n, a, i, o, e[r + 5], 5, -701558691),
            o = u(o, n, a, i, e[r + 10], 9, 38016083),
            i = u(i, o, n, a, e[r + 15], 14, -660478335),
            a = u(a, i, o, n, e[r + 4], 20, -405537848),
            n = u(n, a, i, o, e[r + 9], 5, 568446438),
            o = u(o, n, a, i, e[r + 14], 9, -1019803690),
            i = u(i, o, n, a, e[r + 3], 14, -187363961),
            a = u(a, i, o, n, e[r + 8], 20, 1163531501),
            n = u(n, a, i, o, e[r + 13], 5, -1444681467),
            o = u(o, n, a, i, e[r + 2], 9, -51403784),
            i = u(i, o, n, a, e[r + 7], 14, 1735328473),
            a = u(a, i, o, n, e[r + 12], 20, -1926607734),
            n = d(n, a, i, o, e[r + 5], 4, -378558),
            o = d(o, n, a, i, e[r + 8], 11, -2022574463),
            i = d(i, o, n, a, e[r + 11], 16, 1839030562),
            a = d(a, i, o, n, e[r + 14], 23, -35309556),
            n = d(n, a, i, o, e[r + 1], 4, -1530992060),
            o = d(o, n, a, i, e[r + 4], 11, 1272893353),
            i = d(i, o, n, a, e[r + 7], 16, -155497632),
            a = d(a, i, o, n, e[r + 10], 23, -1094730640),
            n = d(n, a, i, o, e[r + 13], 4, 681279174),
            o = d(o, n, a, i, e[r + 0], 11, -358537222),
            i = d(i, o, n, a, e[r + 3], 16, -722521979),
            a = d(a, i, o, n, e[r + 6], 23, 76029189),
            n = d(n, a, i, o, e[r + 9], 4, -640364487),
            o = d(o, n, a, i, e[r + 12], 11, -421815835),
            i = d(i, o, n, a, e[r + 15], 16, 530742520),
            a = d(a, i, o, n, e[r + 2], 23, -995338651),
            n = m(n, a, i, o, e[r + 0], 6, -198630844),
            o = m(o, n, a, i, e[r + 7], 10, 1126891415),
            i = m(i, o, n, a, e[r + 14], 15, -1416354905),
            a = m(a, i, o, n, e[r + 5], 21, -57434055),
            n = m(n, a, i, o, e[r + 12], 6, 1700485571),
            o = m(o, n, a, i, e[r + 3], 10, -1894986606),
            i = m(i, o, n, a, e[r + 10], 15, -1051523),
            a = m(a, i, o, n, e[r + 1], 21, -2054922799),
            n = m(n, a, i, o, e[r + 8], 6, 1873313359),
            o = m(o, n, a, i, e[r + 15], 10, -30611744),
            i = m(i, o, n, a, e[r + 6], 15, -1560198380),
            a = m(a, i, o, n, e[r + 13], 21, 1309151649),
            n = m(n, a, i, o, e[r + 4], 6, -145523070),
            o = m(o, n, a, i, e[r + 11], 10, -1120210379),
            i = m(i, o, n, a, e[r + 2], 15, 718787259),
            a = m(a, i, o, n, e[r + 9], 21, -343485551),
            n = p(n, c),
            a = p(a, s),
            i = p(i, h),
            o = p(o, f)
        }
        return Array(n, a, i, o)
    }
    function s(e, t, n, a, i, o) {
        return p(h(p(p(t, e), p(a, o)), i), n)
    }
    function l(e, t, n, a, i, o, r) {
        return s(t & n | ~t & a, e, t, i, o, r)
    }
    function u(e, t, n, a, i, o, r) {
        return s(t & a | n & ~a, e, t, i, o, r)
    }
    function d(e, t, n, a, i, o, r) {
        return s(t ^ n ^ a, e, t, i, o, r)
    }
    function m(e, t, n, a, i, o, r) {
        return s(n ^ (t | ~a), e, t, i, o, r)
    }
    function p(e, t) {
        var n = (65535 & e) + (65535 & t)
          , a = (e >> 16) + (t >> 16) + (n >> 16);
        return a << 16 | 65535 & n
    }
    function h(e, t) {
        return e << t | e >>> 32 - t
    }
    var f = 0;
    return t(e)
}


h = function() {
        for (var a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], b = 0; b < 500; b++)
            for (var c = "", d = 0; d < 9; d++) {
                var e = Math.floor(16 * Math.random());
                c += a[e]
            }
        return c
    }


function bxyz(a) {
        function b(a) {
            return d(c(e(a)))
        }
        function c(a) {
            return g(h(f(a), 8 * a.length))
        }
        function d(a) {
            for (var b, c = p ? "0123456789ABCDEF" : "0123456789abcdef", d = "", e = 0; e < a.length; e++)
                b = a.charCodeAt(e),
                d += c.charAt(b >>> 4 & 15) + c.charAt(15 & b);
            return d
        }
        function e(a) {
            for (var b, c, d = "", e = -1; ++e < a.length; )
                b = a.charCodeAt(e),
                c = e + 1 < a.length ? a.charCodeAt(e + 1) : 0,
                55296 <= b && b <= 56319 && 56320 <= c && c <= 57343 && (b = 65536 + ((1023 & b) << 10) + (1023 & c),
                e++),
                b <= 127 ? d += String.fromCharCode(b) : b <= 2047 ? d += String.fromCharCode(192 | b >>> 6 & 31, 128 | 63 & b) : b <= 65535 ? d += String.fromCharCode(224 | b >>> 12 & 15, 128 | b >>> 6 & 63, 128 | 63 & b) : b <= 2097151 && (d += String.fromCharCode(240 | b >>> 18 & 7, 128 | b >>> 12 & 63, 128 | b >>> 6 & 63, 128 | 63 & b));
            return d
        }
        function f(a) {
            for (var b = Array(a.length >> 2), c = 0; c < b.length; c++)
                b[c] = 0;
            for (var c = 0; c < 8 * a.length; c += 8)
                b[c >> 5] |= (255 & a.charCodeAt(c / 8)) << c % 32;
            return b
        }
        function g(a) {
            for (var b = "", c = 0; c < 32 * a.length; c += 8)
                b += String.fromCharCode(a[c >> 5] >>> c % 32 & 255);
            return b
        }
        function h(a, b) {
            a[b >> 5] |= 128 << b % 32,
            a[14 + (b + 64 >>> 9 << 4)] = b;
            for (var c = 1732584193, d = -271733879, e = -1732584194, f = 271733878, g = 0; g < a.length; g += 16) {
                var h = c
                  , i = d
                  , o = e
                  , p = f;
                c = j(c, d, e, f, a[g + 0], 7, -680876936),
                f = j(f, c, d, e, a[g + 1], 12, -389564586),
                e = j(e, f, c, d, a[g + 2], 17, 606105819),
                d = j(d, e, f, c, a[g + 3], 22, -1044525330),
                c = j(c, d, e, f, a[g + 4], 7, -176418897),
                f = j(f, c, d, e, a[g + 5], 12, 1200080426),
                e = j(e, f, c, d, a[g + 6], 17, -1473231341),
                d = j(d, e, f, c, a[g + 7], 22, -45705983),
                c = j(c, d, e, f, a[g + 8], 7, 1770035416),
                f = j(f, c, d, e, a[g + 9], 12, -1958414417),
                e = j(e, f, c, d, a[g + 10], 17, -42063),
                d = j(d, e, f, c, a[g + 11], 22, -1990404162),
                c = j(c, d, e, f, a[g + 12], 7, 1804603682),
                f = j(f, c, d, e, a[g + 13], 12, -40341101),
                e = j(e, f, c, d, a[g + 14], 17, -1502002290),
                d = j(d, e, f, c, a[g + 15], 22, 1236535329),
                c = k(c, d, e, f, a[g + 1], 5, -165796510),
                f = k(f, c, d, e, a[g + 6], 9, -1069501632),
                e = k(e, f, c, d, a[g + 11], 14, 643717713),
                d = k(d, e, f, c, a[g + 0], 20, -373897302),
                c = k(c, d, e, f, a[g + 5], 5, -701558691),
                f = k(f, c, d, e, a[g + 10], 9, 38016083),
                e = k(e, f, c, d, a[g + 15], 14, -660478335),
                d = k(d, e, f, c, a[g + 4], 20, -405537848),
                c = k(c, d, e, f, a[g + 9], 5, 568446438),
                f = k(f, c, d, e, a[g + 14], 9, -1019803690),
                e = k(e, f, c, d, a[g + 3], 14, -187363961),
                d = k(d, e, f, c, a[g + 8], 20, 1163531501),
                c = k(c, d, e, f, a[g + 13], 5, -1444681467),
                f = k(f, c, d, e, a[g + 2], 9, -51403784),
                e = k(e, f, c, d, a[g + 7], 14, 1735328473),
                d = k(d, e, f, c, a[g + 12], 20, -1926607734),
                c = l(c, d, e, f, a[g + 5], 4, -378558),
                f = l(f, c, d, e, a[g + 8], 11, -2022574463),
                e = l(e, f, c, d, a[g + 11], 16, 1839030562),
                d = l(d, e, f, c, a[g + 14], 23, -35309556),
                c = l(c, d, e, f, a[g + 1], 4, -1530992060),
                f = l(f, c, d, e, a[g + 4], 11, 1272893353),
                e = l(e, f, c, d, a[g + 7], 16, -155497632),
                d = l(d, e, f, c, a[g + 10], 23, -1094730640),
                c = l(c, d, e, f, a[g + 13], 4, 681279174),
                f = l(f, c, d, e, a[g + 0], 11, -358537222),
                e = l(e, f, c, d, a[g + 3], 16, -722521979),
                d = l(d, e, f, c, a[g + 6], 23, 76029189),
                c = l(c, d, e, f, a[g + 9], 4, -640364487),
                f = l(f, c, d, e, a[g + 12], 11, -421815835),
                e = l(e, f, c, d, a[g + 15], 16, 530742520),
                d = l(d, e, f, c, a[g + 2], 23, -995338651),
                c = m(c, d, e, f, a[g + 0], 6, -198630844),
                f = m(f, c, d, e, a[g + 7], 10, 1126891415),
                e = m(e, f, c, d, a[g + 14], 15, -1416354905),
                d = m(d, e, f, c, a[g + 5], 21, -57434055),
                c = m(c, d, e, f, a[g + 12], 6, 1700485571),
                f = m(f, c, d, e, a[g + 3], 10, -1894986606),
                e = m(e, f, c, d, a[g + 10], 15, -1051523),
                d = m(d, e, f, c, a[g + 1], 21, -2054922799),
                c = m(c, d, e, f, a[g + 8], 6, 1873313359),
                f = m(f, c, d, e, a[g + 15], 10, -30611744),
                e = m(e, f, c, d, a[g + 6], 15, -1560198380),
                d = m(d, e, f, c, a[g + 13], 21, 1309151649),
                c = m(c, d, e, f, a[g + 4], 6, -145523070),
                f = m(f, c, d, e, a[g + 11], 10, -1120210379),
                e = m(e, f, c, d, a[g + 2], 15, 718787259),
                d = m(d, e, f, c, a[g + 9], 21, -343485551),
                c = n(c, h),
                d = n(d, i),
                e = n(e, o),
                f = n(f, p)
            }
            return Array(c, d, e, f)
        }
        function i(a, b, c, d, e, f) {
            return n(o(n(n(b, a), n(d, f)), e), c)
        }
        function j(a, b, c, d, e, f, g) {
            return i(b & c | ~b & d, a, b, e, f, g)
        }
        function k(a, b, c, d, e, f, g) {
            return i(b & d | c & ~d, a, b, e, f, g)
        }
        function l(a, b, c, d, e, f, g) {
            return i(b ^ c ^ d, a, b, e, f, g)
        }
        function m(a, b, c, d, e, f, g) {
            return i(c ^ (b | ~d), a, b, e, f, g)
        }
        function n(a, b) {
            var c = (65535 & a) + (65535 & b);
            return (a >> 16) + (b >> 16) + (c >> 16) << 16 | 65535 & c
        }
        function o(a, b) {
            return a << b | a >>> 32 - b
        }
        var p = 0;
        return b(a)

        }