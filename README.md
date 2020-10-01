# Deluge.SR.nzbToMedia.Launcher

Event based MS Windows python-script, which:
- Hides own window,
- Logs every step of the way (script),
- de-crap-ifies,
- Flattens directory structure,
- Cleans tvseries-episode release,
- Checks for completeness,
- Decides if wanted quality-rules are met,
- Scans for audio-streams encoded with E-AC3-codec,
- Speeds transcoding/encoding up by converting just those audio-streams to AC3-codec, leaving video and subtitles untouched,
- Manages meta-data (partially) for my Mede8er MED500X2,
- Pre-post-processes by streamlining and preparing everything needed for post-processing,
- Launches nzbToMedia's TorrentToMedia including a working failed-download-concept for Torrent downloads,
- Optimizes the workflow of SickRage tvseries-collection-database and management thereof.

This scripted will be launched by Deluge's standard Execute-plugin, which is unable to manage anything more than just the path pointing towards the script-to-execute on Microsoft Windows, disregarding or even crashing on added extra arguments, which are needed to keep everything optimized and informing to post-processing actors, needed later in the chain of processing the Torrent.
...
Reading all this, might actually suggest that creating a better & improved and more flexible Execute plugin, would be a good thing.
Since I already have a working .cmd (but not being able to hide windows for it) version, and the logic to all parts are basically done,
I'll go for the Python version of that script first and then decide if I want to put effort into creating a better plugin.

STATUS : active - start
