#!/usr/bin/env python

__author__      = "Vishal Patil"
__copyright__   = "Copyright 2007 - 2008, Vishal Patil"
__license__     = "MIT"

from fuse import Stat
from fuse import Direntry
from youtube.api.protocol import YoutubeVideo
from youtube.api.protocol import YoutubePlaylist
from youtube.api.protocol import YoutubeUser
from youtube.fs import YoutubeInodeCounter
import time
import os
import stat
import logging
import re

class YoutubeStat(Stat):
    def __init__(self):
        self.st_ino     = 0 
        self.st_mode    = 0
        self.st_dev     = 0 
        self.st_nlink   = 0
        self.st_size    = 0
        self.st_uid     = os.getuid() 
        self.st_gid     = os.getgid()
        self.st_atime   = 0
        self.st_mtime   = 0
        self.st_ctime   = 0

    def __str__(self):
        tuple = (self.st_mode, self.st_ino, self.st_dev, \
                self.st_nlink, self.st_uid, self.st_gid,\
                self.st_size, self.st_atime, self.st_mtime, \
                self.st_ctime)        
        return str(tuple) 

class YoutubeFSInode:

    def __init__(self,path,mode,id,ctime,mtime,stat=YoutubeStat()):
        self.path           =   str(path)
        if self.path == "/":
            self.direntry = "/"
        else:
            elements        = self.path.split('/')
            self.direntry   = elements[len(elements) - 1]
  
        self.stat           =   YoutubeStat()
        self.stat.st_mode   =   int(mode)
        self.stat.st_ino    =   YoutubeInodeCounter.next() 
        self.stat.st_ctime  =   ctime
        self.stat.st_mtime  =   mtime
        self.data           = ""
        self.id             = id
        self.children       = []

        logging.debug("\nYoutubeFSInode init\npath = %s" +
                    "\ndirentry = %s\nmode = %s\n" + \
                "id = %s\nctime = %s\nmtime = %s\n",self.path,\
                self.direntry,str(self.stat.st_mode),self.stat.st_ino,\
                str(self.stat.st_ctime),str(self.stat.st_mtime))

    def addChildInode(self,inode):
        self.stat.st_nlink = self.stat.st_nlink + 1
        self.children.append(inode)

    def setData(self,data):
        logging.debug("\nYoutubeFSInode setting data as %s",str(data))
        self.data = data 
        self.stat.st_size = len(self.data)

    def __str__(self):
        rstr = ("\nYoutubeFSInode\npath = %s\ndirentry = %s\n"+\
                "id = %s\nstat = %s\n") % \
                (self.direntry,self.path,self.id,str(self.stat))
        return rstr

"""
    A very basic inode cache, this data structure would be 
    modified later for speedy access as well as to decrease
    the memory footprint.
"""
class YoutubeFSInodeCache:
    cache = {}    

    def addInode(self,inode):
        logging.debug("YoutubeFSInodeCache addInode " + str(inode))
        self.cache[inode.path] = inode

    def getInode(self,path):
        logging.debug("YoutubeFSInodeCache getInode for " + path)
        if self.cache.has_key(path):
            return self.cache[path]
        return None 

    def printCache(self):
         for k,v in self.cache.iteritems():
            rstr = "%s,%s\n" % (k,v)       
            logging.info(rstr)

    def __str__(self):
        rstr = "YoutubeInodeCache: Printing cache\n"
        for k,v in self.cache.iteritems():
            rstr = rstr + ("%s\n" % k)       
        return rstr            
