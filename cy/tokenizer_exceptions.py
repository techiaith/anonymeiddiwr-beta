# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA


TOKENIZER_EXCEPTIONS = {

    "a.y.y.b": [
        {ORTH: "a.", LEMMA: "ac"},
        {ORTH: "y.", LEMMA: "yn"},
        {ORTH: "y.", LEMMA: "y"},
        {ORTH: "b", LEMMA: "blaen"} 
    ],

    "a.y.b": [
        {ORTH: "a.", LEMMA: "ac"},
        {ORTH: "y.", LEMMA: "yn y"},
        {ORTH: "b", LEMMA: "blaen"}
    ],

    "h.y.": [
        {ORTH: "h.", LEMMA: "hynny"},
        {ORTH: "y.", LEMMA: "yw"}
    ],

    "e.e.": [
        {ORTH: "e.", LEMMA: "er"},
        {ORTH: "e.", LEMMA: "enghraifft"}
    ],

    "A.C.": [
        {ORTH: "A.", LEMMA: "Aelod"},
        {ORTH: "C.", LEMMA: "Cynulliad"}
    ],

    "A.S.": [
        {ORTH: "A.", LEMMA: "Aelod"},
        {ORTH: "S.", LEMMA: "Seneddol"}
    ],

    "A.S.E.": [
        {ORTH:"A.", LEMMA: "Aelod"},
        {ORTH:"S.", LEMMA: "Seneddol"},
        {ORTH:"E.", LEMMA: "Ewropeaidd"} 
    ]

}

