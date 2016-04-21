#! /usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import struct
import sys


def _calculte_mantissa(bin_number, exponent):
    val = 0 if exponent < -126 else 1
    bit_count = -1
    bit_length = 0
    while bit_length <= 22:
        val += int(bin_number[bit_length]) * 2**bit_count
        bit_count -= 1
        bit_length += 1
    return val


def _convert_position(pos):
    bin_pos = format(int(pos, 16), "0>32b")
    sign = (-1)**int(bin_pos[0], 2)
    _exponent = int(bin_pos[1:9], 2) - 127
    mantissa = _calculte_mantissa(bin_pos[9:], _exponent)
    exponent = _exponent if _exponent > -127 else -126
    position = sign * 2**exponent * mantissa
    return "Bin: %s - Sign: %s - Exponent: %s (%s) - Mantissa: %s - Posititon: %s" % (bin_pos, sign, exponent, _exponent, mantissa, position)


if __name__ == "__main__":
    argvs = sys.argv
    print _convert_position(argvs[1])
    sys.exit()

