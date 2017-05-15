#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Copyright (C) 2017 Harold Coenen
#
# Permission is hereby granted, without written agreement and without
# license or royalty fees, to use, copy, modify, and distribute this
# software and its documentation for any purpose, provided that the
# above copyright notice and the following two paragraphs appear in
# all copies of this software.
#
# IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
# ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN
# IF THE COPYRIGHT HOLDER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
#
# THE COPYRIGHT HOLDER SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE PROVIDED HEREUNDER IS
# ON AN "AS IS" BASIS, AND THE COPYRIGHT HOLDER HAS NO OBLIGATION TO
# PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:         executor.py
# Version:      0.1.0
# Created:      2017.05.15
# Copyright:    OldskoolOrion (Harold Coenen)
# License:      MIT
#-------------------------------------------------------------------------------

# import modules
import sys, os
from datetime import date

# THIS FILE IS A SILLY PLACEHOLDER FOR WHAT IS GOING TO BE THE ACTUAL SCRIPT !!!!!!
# CODE BELOW IS NOT TO BE TAKEN SERIOUS AND DOES NOTHING BUT MAKING ME REMEMBER THE
# STRICT MANDATORY ARGUMENTS USED BY THE DELUGE EXECUTE PLUGIN !!!!!!!!!!!!!!!!!!!!

if not len(sys.argv) == 3:
    exitCode = 5
    print("** ERROR args total: Calling this launcher, you MUST specify THREE arguments, to make it work:")
    print("                     -- 1) torrentID")
    print("                     -- 2) torrentName")
    print("                     -- 3) torrentPath")
    print("** Number args rcvd: "+str(len(sys.argv)))
    if not len(sys.argv) == 0:
        print("** args list rcvd  : "+str(sys.argv))
    else:
        print("** args list rcvd  : NONE")
    print("** ERROR exit      : Exiting launcher with ExitCode = 5 (ERR_ARGS_NR_NOT_THREE)")
    exit(exitCode)
else:
    exitCode    = 0
    torrentID   = sys.argv[1]
    torrentName = sys.argv[2]
    torrentPath = sys.argv[3]
    print(">> args list rcvd  : "+str(sys.argv))
    print(">> split args to   : torrentID, torrentName, torrentPath")
    print("                     -- 1) torrentID   : "+str(torrentID))
    print("                     -- 2) torrentName : "+str(torrentName))
    print("                     -- 3) torrentPath : "+str(torrentPath))
    print("\n-- START PRE-POSTPROCESSING\n")

exit(exitCode)

