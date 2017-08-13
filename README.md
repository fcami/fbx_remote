# fbx_remote

### TODO

At this point the list is rather long:
* specfiles: remove the libtool .la files & add [-static subpackages](https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Packaging_Static_Libraries)
* detect the Player using the avahi-client C/C++ API: _hid._udp (like "avahi-browse -d local _hid._udp --resolve -t")
* handle multiple Players gracefully (do these have different names?)
* check that the control codes in remote.c are the right ones
* display a remote control and act on button events

### Licensing

Everything is GPLv3-licensed unless the subdirectory contains a different COPYING/LICENSE/LICENSE.TXT file.
In this case refer to the subdirectory's license file as noted above instead of the project's.


### existing-code/*

This code comes from Avahi and foils_hid tutorials.
Rudimentary build.sh scripts are provided for easy reuse purposes.


### specfiles/*

Rough Fedora specfiles to package dependencies.


