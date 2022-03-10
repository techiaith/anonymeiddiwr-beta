# encoding: utf8
from __future__ import unicode_literals, print_function

# Gruff
#from spacy.lang.cy.lemmatization import lemmatize_doc
#from spacy.lang.cy.dictionary_pos_tagger import rule_based_pos_tag

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .tag_map import TAG_MAP
from .stop_words import STOP_WORDS
from .lemmatizer import LOOKUP
from .punctuation import TOKENIZER_SUFFIXES
from .norm_exceptions import NORM_EXCEPTIONS
from .lex_attrs import LEX_ATTRS

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups


#from ...lemmatizerlookup import Lemmatizer
#from ...lemmatizer import Lemmatizer

class WelshDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    # lex_attr_getters.update(LEX_ATTRS) # Angen vocab?
    lex_attr_getters[LANG] = lambda text: 'cy'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM],
     BASE_NORMS, NORM_EXCEPTIONS)

    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    tag_map = dict(TAG_MAP)
    stop_words = set(STOP_WORDS)

    suffixes = tuple(TOKENIZER_SUFFIXES)
    lemma_lookup = LOOKUP

#    @classmethod
#    def create_lemmatizer(cls, nlp=None):
#        return Lemmatizer(LOOKUP)

class Welsh(Language):
    lang = 'cy'
    Defaults = WelshDefaults


__all__ = ['Welsh']
