#!/usr/bin/env python
# -*- coding: latin-1 -*-

# fpdf php helpers:

def substr(s, start, length = -1):
    if length < 0: length = len(s) - start
    return s[start:start + length]

def sprintf(fmt, *args): return fmt % args

def print_r(array):
    if not isinstance(array, dict):
        array = dict([(k, k) for k in array])
    for k, v in sorted(array.items(), key=lambda x: str(x[0])):
        print("[%s] => %s " % (k, v))

def UTF8ToUTF16BE(instr, setbom = True):
    "Converts UTF-8 strings to UTF16-BE."
    outstr = "".encode()
    if (setbom):
        outstr += "\xFE\xFF".encode("latin1")
    if not isinstance(instr, str):
        instr = instr.decode('UTF-8')
    return outstr + instr.encode('UTF-16BE')

def UTF8StringToArray(instr):
    "Converts UTF-8 strings to codepoints array"
    return [ord(c) for c in instr]

# ttfints php helpers:

def die(msg):
    raise RuntimeError(msg)

def str_repeat(s, count):
    return s * count

def str_pad(s, pad_length=0, pad_char= " ", pad_type= +1 ):
    # pad left
    if pad_type < 0:   return s.rjust(pad_length,  pad_char)
    # pad right
    elif pad_type > 0: return s.ljust(pad_length,  pad_char)
    # pad both
    else:              return s.center(pad_length, pad_char)

strlen = count = lambda s: len(s)
