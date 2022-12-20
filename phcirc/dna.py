import os
import sys

__author__ = 'Rob Edwards'


def rc(dna):
    """
    Reverse complement a DNA sequence

    :param dna: The DNA sequence
    :type dna: str
    :return: The reverse complement of the DNA sequence
    :rtype: str
    """
    complements = str.maketrans('acgtrymkbdhvACGTRYMKBDHV', 'tgcayrkmvhdbTGCAYRKMVHDB')
    rcseq = dna.translate(complements)[::-1]
    return rcseq


