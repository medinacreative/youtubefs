# Roadmap #

### v0.2 ###
  * YoutubeFS on Mac OSX using MacFUSE
  * Currently if the user changes his playlists, favorites or subscriptions the changes are not reflected dynamically by YoutubeFS, i.e. the user has to remount the filesystem to see the updates. Use a polling mechanism to update the videos dynamically using a polling threading.