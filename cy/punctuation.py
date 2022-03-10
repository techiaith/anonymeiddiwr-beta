# coding: utf-8

from __future__ import unicode_literals
from ..punctuation import TOKENIZER_SUFFIXES

_cy_suffixes = (["'CH", "'ch", "'I", "'i", "'M", "'m", "'N", "'n",
	"'R", "'r", "'TH", "'th", "'U", "'u", "'W", "'w"])

TOKENIZER_SUFFIXES = TOKENIZER_SUFFIXES + _cy_suffixes

