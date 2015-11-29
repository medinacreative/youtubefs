### Required software ###
  * python 2.5
  * fuse (Filesystem in UserSpace) kernel module
  * fuse client library (libfuse2)
  * python-fuse

### Configuring fuse ###
Once fuse is installed please perform the following steps
  * sudo adduser **username** fuse
  * sudo chgrp fuse /dev/fuse

where the **username** is your Unix username. Make sure you log out of your shell and log in again after executing these steps.

### Running YoutubeFS on Linux ###

  * Download the latest tar file
  * Extract the tar file
  * Mount the Youtube filesystem using the following command
    * **./youtubefs.py**

&lt;username&gt;

 

&lt;mountpoint&gt;



where the **username** is your youtube username and **mountpoint** is the full path of the directory where the Youtube videos will be located. Also make sure you are connected to the internet while mounting the file system.
