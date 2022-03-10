import argparse
import csv
import random
import spacy
from spacy.tokens import Doc
from redaction import *
import datetime

begin_time = datetime.datetime.now()

Doc.set_extension("cy_text", default=set()) # TO ADD CY TEXT TO EN DOC

nlp_en = spacy.load("en_core_web_lg", disable=["parser"])
nlp_cy = spacy.load("/home/gruffudd/spacy23/model_tagio_lemateiddio_spacy")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help='Input file. Must be a tab-delimited .csv '
                                    'file featuring a column named "source" '
                                    'featuring English text and a column named '
                                    '"target" featuring the corresponding Welsh '
                                    'text.')
    parser.add_argument("output_file", help='The required name of the anonymized output '
                                      'two-column .csv file that will be produced')

    args = parser.parse_args()


    anonymized_bitexts = []
    with open(args.input_file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            bitext = {}

            bitext["en"] = (row["source"].strip())
            bitext["cy"] = (row["target"].strip())

            en_doc = nlp_en(bitext["en"])
            en_sensitive_ents = get_sensitive_ents(en_doc)
            redacted_en = redact_en(en_doc, bitext["en"], en_sensitive_ents)

            cy_doc = nlp_cy(bitext["cy"])
            redacted_cy = redact_cy(cy_doc, bitext["cy"], en_sensitive_ents) # using EN ents for the time being)

            if redacted_en \
            and redacted_cy \
            and len(redacted_en) > 1 \
            and len(redacted_cy) > 1:
                anonymized_bitext = redacted_en + "\t" + redacted_cy + "\n"

            if "X" not in anonymized_bitext:
                anonymized_bitexts.append(anonymized_bitext)

            # if i == 100:
            #     break

    random.shuffle(anonymized_bitexts)

    with open(args.output_file, mode="w") as outfile:
        for anonymized_bitext in anonymized_bitexts:
            outfile.write((anonymized_bitext))

    print ('File "' + args.output_file + '" written!')
    print ("Time taken:", datetime.datetime.now() - begin_time)
