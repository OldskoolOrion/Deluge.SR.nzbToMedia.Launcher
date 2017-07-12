#!/usr/bin/env python

"""
----------------------------------------------------------------------------------------------------
  MIT License                                                                   Copyright (c) 2017
----------------------------------------------------------------------------------------------------

- Author :
    Harold Coenen (OldskoolOrion)
- E-mail :
    OldskoolOrion@gmail.com
- First shared at GitHub (2017.05.16) - v0.1.0 :
    https://github.com/OldskoolOrion/Deluge.SR.nzbToMedia.Launcher.git

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    1) The above copyright notice and this permission notice shall be included in all copies or
       substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Scriptname      : executor.py
Version         : 0.1.8
Last mod.       : 2017.07.12
Created         : 2017.05.16
License         : MIT
Copyright       : (c) 2017, Harold Coenen (OldskoolOrion)
E-mail          : OldskoolOrion@gmail.com
Scriptlocation  : https://github.com/OldskoolOrion/Deluge.SR.nzbToMedia.Launcher.git
"""

####################################################################################################
############
##
##  STEPS TO TAKE :
##  Run As (Dictated by Deluge) :
##      executor.py "d2d6a72b60cdb2cc5e80d3277d89d5df18c3ecbc" "Name.S01E01.720p.WEBRip.H264-GRP" \
##                  "D:\TorrentDL\u.series"
##  Check if PARAM 2 is file or directory :
##      D:\TorrentDL\u.series\Name.S01E01.720p.WEBRip.H264-GRP(.mkv) ??
##          -> note : Extremely basic but therefor easy to overlook check!
##             Initiating torrent downloads by scripts using magnet-links, sometimes prevents you
##             from noticing the movie/serie-episode download is not in a folder of it's own.
##             Usually this is standard practice. Is there just one single file not in a folder ?
##             This of course has consequences when trying to tidy/clean the release from as much
##             unnecessary extra files and even worse (malware/virus).
##             Imagine not checking : chdir to a file instead of folder - script will not halt, but
##             no directory change was made. Still in script directory the script starts cleaning.
##             You could lose all your scripts / other files, or at least spending time restoring
##             a backup. Prevent extra work.- automation is the goal : not extra work!
##  Clean Folder after handling possible exception, based on experience :
##      D:\TorrentDL\u.series\Name.S01E01.720p.WEBRip.H264-GRP
##          Filemasks which are being deleted for movies / serie-episodes :
##              - *.links    - *.nfo    - *.bat
##              - *.exe      - *.chm    - *.cmd
##              - *.nzb      - *.par    - *.vbs
##              - *.par2     - *.sfv    - *.ps1
##              - *.srr      - *.jpg    - *.js
##              - *.png      - *.bmp    - *.py
##              - *.ico      - *.txt    - *.[docx|xlsx|pptx]
##              - *.[1..99]  - *.OSX (and OSX typical files)
##              - RARBG.*    - *.(thumbs db)
##              - *.pdf      - Goedkoop*.rar
##              (and so on.. edit list for personal preference / need)
##          Comparable to what is often done with a batchfile function under Windows (example) :
##          >> FOR %%g IN ( *.nzb *.par2 *.par *.sfv *.srr *.jpg *.gif *.png *.txt *.nfo *.url \
##          >>              Q-for-You.* *.exe *.chm *._Contents *.plist *.wflow *.workflow RARBG.* \
##          >>              Goedkoop*.rar ) DO ( DEL "%%g" )
##  Check videocontainer's first audiostream :
##      If not produced as E-AC3 stream, then continue to the next step.
##      If it IS E-AC3 instead of the standard A-AC3 codec, then perform in the background :
##          - rename container to *.eac3.mkv
##          - using FFMpeg leave videostream & subtitlestreams untouched
##          - just reencode audiostream from E-AC3 into A-AC3 and recombine this stream, with the
##            untouched video & subtitles. This saves A LOT time compared to transcode or full
##            reencode (as nzbToMedia (see next step) performs.
##          - when starting the FFMpeg execution, also start a monitor on FFMpeg's ProcessID :
##            on end of ProcessID delete *.eac3.mkv. This ensures removal of correct input, when
##            multiple postprocessing threads run ( multiprocessing + nonblocking code ).
##          - After deleting the file continue to the next step
##  Continue postprocessing using nzbToMedia's scripts :
##      Calling nzbToMedia gives additional perk of FDH (failed download handling), when being
##      coupled to SickRage as main serie-episodes management centre. The proliferation of fakes,
##      incompletes, corrupt files, codec scams, propagation issues, upload glitches and
##      DMCA takedowns can break the automation process and requires user intervention.
##      Not what we want.. we want full automation, with no waiting time!
##      >> ISSUE : pyw TorrentToMedia.py "193593c6678281cc3fd2b4e23232747c4855820f" \
##                                       "Name.S01E01.720p.WEBRip.H264-GRP" "D:\TorrentDL\u.series"
##      End-of-Script!
##  IMPORTANT: path-notation under Windows sometimes changes :
##                 * usually pathnotation under Windows   :  "D:\etc"
##                 * occasionally pathnotation found like :  "\\?\D:\etc"
##             Make sure both forms are dealt with correctly! Easy string replace would do the
##             trick (from Windows batch script as example) :
##                 ' SET resultdir=%~3\%~2 ' and then ' SET resultdir=%resultdir:\\?\=% '
##
############
####################################################################################################

# import modules
import sys
import os
import time

# constants
EXECSCRIPT = "TorrentToMedia.py"
EXECPATH = "D:\\Feed.Me.Bytes\\d.downloading\\config\\"

if __name__ == "__main__":

    T1 = time.clock()
    PREPROCESSED = 0
    EXITCODE = 4 - len(sys.argv)

    if not EXITCODE == 0:
        print("** ERROR - 3 arguments expected. See below how to call this script:")
        print("\n            >> path.to/executor.py \"< torrent-id >\"  \"< release-name >\""\
              " \"< destination-path >\" ")
        print("\n\n** NOTE  : <releaseName> can be a either a video-file, or the directory-name"\
              " containing the content to process.")
        print("\nErrorcode: "+str(EXITCODE))
        exit(EXITCODE)
    else:
        ARGLIST = str(sys.argv)
        TORRENTID = sys.argv[1]
        RELEASE = sys.argv[2]
        DESTPATH = sys.argv[3]
        COMBINEDPATH = os.path.join(DESTPATH, RELEASE)

        if os.path.isdir(COMBINEDPATH):
            print("\nEntering directory : "+str(COMBINEDPATH))
            #change into directory and clean unwanted files
            PREPROCESSED = 1
        else:
            if os.path.isfile(COMBINEDPATH):
                print("\nRelease passed was not a directory but an existing single video-file: "
                      +str(COMBINEDPATH))
                # create directory & move file
                PREPROCESSED = 1
            else:
                EXITCODE = 0xFF

    if EXITCODE != 0:
        print("\n> ERROR detected")
        print("Errorcode          : "+str(EXITCODE))
    else:
        print("No Error : maybe do aditionall stuff before passing it up the chain")
        print("\nExiting with code : "+str(EXITCODE))

    T2 = time.clock()
    print("Starttime          : "+str(T1))
    print("Endtime            : "+str(T2))
    print("Total runtime (ms) : "+str((T2-T1)*1000))
    print("Exiting script...")

    exit(EXITCODE)
