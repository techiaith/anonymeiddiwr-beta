import re

def get_sensitive_ents(doc):
    sensitive_ents = {}
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC", "FAC", "PERSON", "ORG", "DATE"]:
            sensitive_ents[ent.text] = ent.label_
    return sensitive_ents

def redact_email_addresses(segment):
    segment_email_addresses = list(get_email_addresses(segment))
    for segment_email_address in segment_email_addresses:
        segment = segment.replace(segment_email_address, "XEMAILX")
    return segment

def redact_urls(segment):
    segment_urls = list(get_urls(segment))
    for segment_url in segment_urls:
        segment = segment.replace(segment_url, "XURLX")
    return segment

def redact_propns(doc, segment):
    propns = []
    for token in doc:
        if token.pos_ == "PROPN":
            propns.append(token.text)
    if propns:
        for propn in propns:
            segment = segment.replace(propn, "XPROPNX")
    return segment

def redact_nums(doc, segment):
    propns = []
    for token in doc:
        if token.pos_ == "NUM":
            propns.append(token.text)
    if propns:
        for propn in propns:
            segment = segment.replace(propn, "XNUMX")
    return segment

def get_email_addresses(segment):
    EMAIL_REG = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.search(EMAIL_REG, segment, re.IGNORECASE):
        search = re.search(EMAIL_REG, segment, re.IGNORECASE)
        yield search.group(1)

def get_urls(segment):
    URL_REG = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    URL_REG = r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
    if re.search(URL_REG, segment, re.IGNORECASE):
        search = re.search(URL_REG, segment, re.IGNORECASE)
        yield search.group(0)


def redact_ents(segment, sensitive_ents):
    for sensitive_ent in sensitive_ents:
        segment = segment.replace(sensitive_ent, "XXXX")
    return segment

def substitute_ents(segment, sensitive_ents):
    for sensitive_ent in sensitive_ents:
        segment = segment.replace(sensitive_ent, sensitive_ents[sensitive_ent])
    return segment

def redact_en(en_doc, en_segment, sensitive_ents):

    # REDACT EMAILS
    en_segment = redact_email_addresses(en_segment)

    # REDACT WEBSITE ADDRESSES
    en_segment = redact_urls(en_segment)

    # REDACT FILE NAMES ?

    # REDACT PHONE NUMBERS
    # see REDACT NUM POS TAGS

    # REDACT POSTCODES

    # REDACT DATES
    # (see ents DATE)
    # TODO: 06/03/17, 03/17 etc.

    # REDACT ENTS
    #en_segment = redact_ents(en_segment, sensitive_ents)
    en_segment = substitute_ents(en_segment, sensitive_ents)

    # REDACT PROPN POS TAGS
    en_segment = redact_propns(en_doc, en_segment)

    # REDACT NUM POS TAGS
    en_segment = redact_nums(en_doc, en_segment)

    return en_segment

def redact_cy(cy_doc, cy_segment, sensitive_ents):
    # REDACT EMAILS
    cy_segment = redact_email_addresses(cy_segment)

    # REDACT WEBSITE ADDRESSES
    cy_segment = redact_urls(cy_segment)

    # REDACT FILE NAMES ?

    # REDACT PHONE NUMBERS
    # see REDACT NUM POS TAGS

    # REDACT POSTCODES

    # REDACT DATES
    # (see ents DATE)
    # TODO: 06/03/17, 03/17 etc.

    # REDACT ENTS
    #en_segment = redact_ents(en_segment, sensitive_ents)
    cy_segment = substitute_ents(cy_segment, sensitive_ents)

    # REDACT PROPN POS TAGS
    cy_segment = redact_propns(cy_doc, cy_segment)

    # REDACT NUM POS TAGS
    cy_segment = redact_nums(cy_doc, cy_segment)

    return cy_segment

def redact_mono_cy(cy_doc, cy_segment):
    # REDACT EMAILS
    cy_segment = redact_email_addresses(cy_segment)

    # REDACT WEBSITE ADDRESSES
    cy_segment = redact_urls(cy_segment)

    # REDACT FILE NAMES ?

    # REDACT PHONE NUMBERS
    # see REDACT NUM POS TAGS

    # REDACT POSTCODES

    # REDACT DATES
    # (see ents DATE)
    # TODO: 06/03/17, 03/17 etc.

    # REDACT ENTS
    # TODO

    # REDACT PROPN POS TAGS
    cy_segment = redact_propns(cy_doc, cy_segment)

    # REDACT NUM POS TAGS
    cy_segment = redact_nums(cy_doc, cy_segment)

    return cy_segment
