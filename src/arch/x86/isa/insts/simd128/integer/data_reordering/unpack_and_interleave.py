# Copyright (c) 2007 The Hewlett-Packard Development Company
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# The software must be used only for Non-Commercial Use which means any
# use which is NOT directed to receiving any direct monetary
# compensation for, or commercial advantage from such use.  Illustrative
# examples of non-commercial use are academic research, personal study,
# teaching, education and corporate research & development.
# Illustrative examples of commercial use are distributing products for
# commercial advantage and providing services using the software for
# commercial advantage.
#
# If you wish to use this software or functionality therein that may be
# covered by patents for commercial use, please contact:
#     Director of Intellectual Property Licensing
#     Office of Strategy and Technology
#     Hewlett-Packard Company
#     1501 Page Mill Road
#     Palo Alto, California  94304
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.  Redistributions
# in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.  Neither the name of
# the COPYRIGHT HOLDER(s), HEWLETT-PACKARD COMPANY, nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.  No right of
# sublicense is granted herewith.  Derivatives of the software and
# output created using the software may be prepared, but only for
# Non-Commercial Uses.  Derivatives of the software may be shared with
# others provided: (i) the others agree to abide by the list of
# conditions herein which includes the Non-Commercial Use restrictions;
# and (ii) such Derivatives of the software include the above copyright
# notice to acknowledge the contribution from this software where
# applicable, this list of conditions and the disclaimer below.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Gabe Black

microcode = '''
def macroop PUNPCKLBW_XMM_XMM {
    unpack xmmh, xmml, xmmlm, sel=1, size=1
    unpack xmml, xmml, xmmlm, sel=0, size=1
};

def macroop PUNPCKLBW_XMM_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=1
    unpack xmml, xmml, ufp1, sel=0, size=1
};

def macroop PUNPCKLBW_XMM_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=1
    unpack xmml, xmml, ufp1, sel=0, size=1
};

def macroop PUNPCKLWD_XMM_XMM {
    unpack xmmh, xmml, xmmlm, sel=1, size=2
    unpack xmml, xmml, xmmlm, sel=0, size=2
};

def macroop PUNPCKLWD_XMM_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=2
    unpack xmml, xmml, ufp1, sel=0, size=2
};

def macroop PUNPCKLWD_XMM_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=2
    unpack xmml, xmml, ufp1, sel=0, size=2
};

def macroop PUNPCKLDQ_XMM_XMM {
    unpack xmmh, xmml, xmmlm, sel=1, size=4
    unpack xmml, xmml, xmmlm, sel=0, size=4
};

def macroop PUNPCKLDQ_XMM_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=4
    unpack xmml, xmml, ufp1, sel=0, size=4
};

def macroop PUNPCKLDQ_XMM_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    unpack xmmh, xmml, ufp1, sel=1, size=4
    unpack xmml, xmml, ufp1, sel=0, size=4
};

def macroop PUNPCKHBW_XMM_XMM {
    unpack xmml, xmmh, xmmhm, sel=0, size=1
    unpack xmmh, xmmh, xmmhm, sel=1, size=1
};

def macroop PUNPCKHBW_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=1
    unpack xmmh, xmmh, ufp1, sel=1, size=1
};

def macroop PUNPCKHBW_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=1
    unpack xmmh, xmmh, ufp1, sel=1, size=1
};

def macroop PUNPCKHWD_XMM_XMM {
    unpack xmml, xmmh, xmmhm, sel=0, size=2
    unpack xmmh, xmmh, xmmhm, sel=1, size=2
};

def macroop PUNPCKHWD_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=2
    unpack xmmh, xmmh, ufp1, sel=1, size=2
};

def macroop PUNPCKHWD_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=2
    unpack xmmh, xmmh, ufp1, sel=1, size=2
};

def macroop PUNPCKHDQ_XMM_XMM {
    unpack xmml, xmmh, xmmhm, sel=0, size=4
    unpack xmmh, xmmh, xmmhm, sel=1, size=4
};

def macroop PUNPCKHDQ_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=4
    unpack xmmh, xmmh, ufp1, sel=1, size=4
};

def macroop PUNPCKHDQ_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    unpack xmml, xmmh, ufp1, sel=0, size=4
    unpack xmmh, xmmh, ufp1, sel=1, size=4
};

def macroop PUNPCKHQDQ_XMM_XMM {
    movfp xmml, xmmh
    movfp xmmh, xmmhm
};

def macroop PUNPCKHQDQ_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldfp ufp1, seg, [1, t0, t1], 8, dataSize=8
    movfp xmml, xmmh
    movfp xmmh, ufp1
};

def macroop PUNPCKHQDQ_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldfp ufp1, seg, riprel, 8, dataSize=8
    movfp xmml, xmmh
    movfp xmmh, ufp1
};

def macroop PUNPCKLQDQ_XMM_XMM {
    movfp xmmh, xmmlm
};

def macroop PUNPCKLQDQ_XMM_M {
    ldfp xmmh, seg, sib, disp, dataSize=8
};

def macroop PUNPCKLQDQ_XMM_P {
    rdip t7
    ldfp xmmh, seg, riprel, disp, dataSize=8
};
'''
