from __future__ import unicode_literals

from ...attrs import LIKE_NUM
#from ...attrs import IS_MUT

# Angen deall sut i drin rhifau aml-air
# Angen rhifau benywaidd
_num_words = ['sero', 'un', 'dau', 'tree', 'pedwar', 'pump', 'chwech', 'saith',
              'wyth', 'naw', 'deg', 'deuddeg',
              'pymtheg', 'deunaw', 'ugain',
              'deugain', 'trigain',
              'can', 'cant', 'mil', 'miliwn', 'biliwn', 'triliwn', 'cwadriliwn',
              'gajiliwn', 'basiliwn']


def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return (text, True)
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return (text, True)
    if text in _num_words:
        return (text, True)
    return (text, False)


LEX_ATTRS = {
    LIKE_NUM: like_num
}
