#!/bin/python3
# -*- coding: utf-8 -*-
"""Global settings for omorfi.

Includes special symbols, definitions of alphabets and their subsets,
and alphabet pairs as well as internal keywords.
"""

# Author: Omorfi contributors <omorfi-devel@groups.google.com> 2015

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


# common symbols for all
VERSION_ID_EASTER_EGG = "OMORFI_VERSION_≥_15_©_GNU_GPL_V3"
WORD_BOUNDARY = "{WB}"
NEWWORD_BOUNDARY = "{wB}"
WEAK_BOUNDARY = "{XB}"
DERIV_BOUNDARY = "{DB}"
MORPH_BOUNDARY = "{MB}"
STUB_BOUNDARY = "{STUB}"
OPTIONAL_HYPHEN = "{hyph?}"
COMMON_MULTICHARS = {
    VERSION_ID_EASTER_EGG,
    WORD_BOUNDARY,
    NEWWORD_BOUNDARY,
    WEAK_BOUNDARY,
    DERIV_BOUNDARY,
    MORPH_BOUNDARY,
    STUB_BOUNDARY,
    OPTIONAL_HYPHEN
}
# some duplicates for symmetry:
FIN_LOWERCASE = "abcdefghijklmnopqrsštuvwxyzžåäö" + \
    "áàâãāăąçćĉċčđðďéèêëēĕęėěƒĝğġģȟħíìîïĩīĭįıĳĵķĸĺļľŀłñńņňŋ" + \
    "óòôōŏŕŗřśŝşſţťŧßþúùûüũūŭůųŵýŷÿűźżʒæøœőə"
FIN_UPPERCASE = "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖ" \
    "ÁÀÂÃĀĂĄÇĆĈĊČÐÐĎÉÈÊËĒĔĘĖĚƑĜĞĠĢȞĦÍÌÎÏĨĪĬĮİĲĴĶĸĹĻĽĿŁÑŃŅŇŊ" + \
    "ÓÒÔŌŎŔŖŘŚŜŞSŢŤŦßÞÚÙÛÜŨŪŬŮŲŴÝŶŸŰŹŻƷÆØŒŐƏ"
# asymmetric sets:
FIN_LOWER_VOWELS = "aeiouyåäö" + \
    "áàâãāăąéèêëēĕęėěíìîïĩīĭįıóòôōŏúùûüũūŭůųýŷÿűæøœőə"
FIN_UPPER_VOWELS = "AEIOUYÅÄÖ" \
    "ÁÀÂÃĀĂĄÉÈÊËĒĔĘĖĚÍÌÎÏĨĪĬĮİÓÒÔŌŎÚÙÛÜŨŪŬŮŲÝŶŰÆØŒŐƏ"
FIN_VOWELS = FIN_LOWER_VOWELS + FIN_UPPER_VOWELS
FIN_LOWER_CONSONANTS = "bcdfghjklmnpqrsštvwxzž" + \
    "çćĉċčđðďƒĝğġģȟħĵķĸĺļľŀłñńņňŉŋŕŗřśŝşſţťŧßþŵźżʒ"
FIN_UPPER_CONSONANTS = "BCDFGHJKLMNPQRSŠTVWXZŽ" \
    "ÇĆĈĊČÐĎĜĞĠĢȞĦĴĶĹĻĽĿŁÑŃŅŇŊŔŖŘŚŜŞŢŤŦÞŴŹŻƷ"
FIN_CONSONANTS = FIN_LOWER_CONSONANTS + FIN_UPPER_CONSONANTS
# the words containing symbols are likely weird / props etc.
FIN_SYMBOLS = "1234567890§!\"#¤%&/()=?½@£$‚{[]}<>*"
# punctuation characters one may optionally split without space after the word
FIN_PUNCT_TRAILING = "\"'.,?!)]}’”–:;»>"
# punctuations chopped of at the beginning of the word
FIN_PUNCT_LEADING = "\"'<([{’”-–»>"
# known variants and old orthographies 1:1
# (a conservative listing for sure)
FIN_ORTH_PAIRS = [("’", "'"), ("’", "´"), ("’", "′"), ("-", "‐"),
                  ("-", "‑"), ("-", "‑")]
# weights by rules
STUFF_WEIGHTS = {"Bc": "+1.0",
                 "Duus": "+16.0", "Dttaa": "+16.0",
                 "Dtattaa": "+16.0", "Dtatuttaa": "+32.0", "Dinen": "+1.0",
                 "Dja": "+2.0", "Du": "+16.0",
                 "Uarch": "+16.0",
                 "Udial": "+2.0", "Urare": "+4.0", "Unonstd": "+4.0",
                 "Xabe": "+0.1", "Xcom": "+1.0", "Xins": "+2.0",
                 "Qhan": "+1.0", "Qpa": "+1.0", "Qkin": "+1.0",
                 "Qkaan": "+1.0"
                 }
BOUNDARY_WEIGHTS = {WORD_BOUNDARY: "+0.1", MORPH_BOUNDARY: "+0.1",
                    NEWWORD_BOUNDARY: "+1.0", DERIV_BOUNDARY: "+2.0",
                    WEAK_BOUNDARY: "+0.1", STUB_BOUNDARY: "+0.1"}

# stuff is the tag format in database or lexical data, a lot of things
STUFFS = {
    "",
    "ABBREVIATION",
    "ACRONYM",
    "ADJECTIVE",
    "ADPOSITION",
    "ADVERB",
    "ADVERBIAL",
    "Bc",
    "B-",
    "B←",
    "B→",
    "CARDINAL",
    "Ccmp",
    "CLAUSE-BOUNDARY",
    "Cma",
    "Cmaisilla",
    "Cmaton",
    "Cnut",
    "COMPARATIVE",
    "COMP",
    "CONJUNCTION",
    "COORDINATING",
    "Cpos",
    "Csup",
    "Cva",
    "DASH",
    "DECIMAL",
    "DEMONSTRATIVE",
    "DIGIT",
    "Din",
    "Dinen",
    "Dja",
    "Dma",
    "Dmaisilla",
    "Dmaton",
    "Dminen",
    "Dmpi",
    "Dnut",
    "Ds",
    "Dsti",
    "Dtattaa",
    "Dtatuttaa",
    "Dtava",
    "Dttaa",
    "Dtu",
    "Du",
    "Duus",
    "Dva",
    "FINAL-BRACKET",
    "FINAL-QUOTE",
    "FTB3man",
    "Ia",
    "Ie",
    "Ima",
    "Iminen",
    "INDEFINITE",
    "INITIAL-BRACKET",
    "INITIAL-QUOTE",
    "INTERJECTION",
    "INTERROGATIVE",
    "LEMMA-START",
    "Ncon",
    "Nneg",
    "NOUN",
    "Npl",
    "N??",
    "Nsg",
    "NUMERAL",
    "O3",
    "Opl1",
    "Opl2",
    "ORDINAL",
    "Osg1",
    "Osg2",
    "PE4",
    "PERSONAL",
    "PL1",
    "PL2",
    "PL3",
    "Ppe4",
    "Ppl1",
    "Ppl2",
    "Ppl3",
    "PREPOSITION",
    "PRONOUN",
    "PROPER",
    "Psg1",
    "Psg2",
    "Psg3",
    "PUNCTUATION",
    "Qhan",
    "Qkaan",
    "Qka",
    "Qkin",
    "Qko",
    "Qpa",
    "Qs",
    "QUALIFIER",
    "QUANTOR",
    "RECIPROCAL",
    "REFLEXIVE",
    "RELATIVE",
    "ROMAN",
    ".sent",
    "SENTENCE-BOUNDARY",
    "SG1",
    "SG2",
    "SG3",
    "SPACE",
    "SUPERL",
    "Tcond",
    "Timp",
    "Topt",
    "Tpast",
    "Tpot",
    "Tpres",
    "Uarch",
    "Udial",
    "Unonstd",
    "UNSPECIFIED",
    "Urare",
    "Vact",
    "VERB",
    "Vpss",
    "Xabe",
    "Xabl",
    "Xacc",
    "Xade",
    "Xall",
    "Xcom",
    "Xela",
    "Xess",
    "Xgen",
    "Xill",
    "Xine",
    "Xins",
    "Xlat",
    "X???",
    "Xnom",
    "Xpar",
    "Xtra",
}
