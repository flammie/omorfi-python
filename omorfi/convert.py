#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formatter to de/format omor style analyses for omrfi."""

# (c) Omorfi contributors <omorfi-devel@groups.google.com> 2015–2018
# see AUTHORS file in top-level dir of this project, or
# <https://github.com/flammie/omorfi/wiki/AUTHORS>

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
#
# utils to format apertium style data from omorfi database values

import re
import sys

from .error_logging import fail_formatting_missing_for, just_fail
from .string_manglers import egrep2xerox, lexc_escape, regex_delete_surface


def get_lemmas_omor(s, hacks=None):
    """Get lemma(s) from analysed token."""
    re_lemma = re.compile(r"\[WORD_ID=([^]]*)\]")
    escanal = s.replace("[WORD_ID=]]",
                        "[WORD_ID=@RIGHTSQUAREBRACKET@]")
    lemmas = re_lemma.finditer(escanal)
    rv = []
    for lemma in lemmas:
        s = lemma.group(1)
        for i in range(32):
            hnsuf = "_" + str(i)
            if s.endswith(hnsuf):
                s = s[:-len(hnsuf)]
        if s == "@RIGHTSQUAREBRACKET@":
            s = "]"
        rv += [s]
    # legacy pron hack
    if len(rv) == 1 and rv[0] in ["me", "te", "he", "nämä", "ne"] and\
            get_upos_omor(s) == "PRON" and hacks:
        if rv[0] == "me":
            rv[0] = "minä"
        elif rv[0] == "te":
            rv[0] = "sinä"
        elif rv[0] == "he":
            rv[0] = "hän"
        elif rv[0] == "nämä":
            rv[0] = "tämä"
        elif rv[0] == "ne":
            rv[0] = "se"
    return rv


def get_last_feat_omor(s, feat):
    """Get last (effective) value for the given morphological feature.

    This function tries to determine the most likely morphosyntactic
    feature values from complex analyses, e.g. with compounds and
    derivations the most relevant ones for the whole token.
    """
    re_feat = re.compile(r"\[" + feat + r"=([^]]*)\]")
    feats = re_feat.finditer(s)
    rv = ""
    for f in feats:
        rv = f.group(1)
    return rv


def get_last_feats_omor(s):
    """Get last (effective) value for the given morphological feature.

    This function tries to determine the most likely morphosyntactic
    feature values from complex analyses, e.g. with compounds and
    derivations the most relevant ones for the whole token.
    """
    re_feats = re.compile(r"\[[A-Z_]*=[^]]*\]")
    rvs = []
    feats = re_feats.finditer(s)
    for feat in feats:
        if "WORD_ID=" in feat.group(0):
            # feats reset on word boundary
            rvs = []
        else:
            rvs.append(feat.group(0))
    return rvs


def get_upos_omor(s, deriv_munging=True):
    """Get Universal Part-of-Speech."""
    upos = get_last_feat_omor(s, "UPOS")
    if deriv_munging:
        drv = get_last_feat_omor(s, "DRV")
        if upos == "VERB" and drv == "MINEN":
            upos = "NOUN"
    return upos
