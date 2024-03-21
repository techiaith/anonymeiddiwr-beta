import argparse
import csv
import random
import spacy
from spacy.tokens import Doc
from redaction import *
import datetime

begin_time = datetime.datetime.now()

# https://github.com/techiaith/spacy_cy_tag_lem_ner_lg
nlp_cy = spacy.load("/model_tagio_lemateiddio_spacy")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help='Input text file. Sentence per line Welsh-language text expexted.')
    parser.add_argument("output_file", help='The required name of the anonymized output '
                                      'text file that will be produced')

    args = parser.parse_args()


    anonymized_cy_texts = []
    with open(args.input_file, mode="r") as text_file:
        for i, line in enumerate(text_file):

            cy_text = (line.strip())

            cy_doc = nlp_cy(cy_text)
            redacted_cy = redact_mono_cy(cy_doc, cy_text)

            if redacted_cy \
            and len(redacted_cy) > 1:
                anonymized_cy_text = redacted_cy + "\n"


            anonymized_cy_texts.append(anonymized_cy_text)

            # if i == 100:
            #     break

    #random.shuffle(anonymized_cy_texts)

    with open(args.output_file, mode="w") as outfile:
        for anonymized_cy_text in anonymized_cy_texts:
            outfile.write((anonymized_cy_text))

    print ('File "' + args.output_file + '" written!')
    print ("Time taken:", datetime.datetime.now() - begin_time)
