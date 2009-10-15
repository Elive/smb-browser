#!/usr/bin/env python

from distutils.core import setup

setup(name = "smb-browser",
	version = "1.06",
	description = "This program was designed to assist users in finding and mounting samba shared folders on a network while being easy yet functional",
	author = "David Braker",
	author_email = "linuxnit@elivecd.org",
	packages=["smb-browser"],
	data_files=[("/usr/share/pixmaps",["tree/usr/share/pixmaps/smb-browser.png"]),
		    ("/usr/share/applications/",["tree/usr/share/applications/smb-browser.desktop"]),
		    ("/usr/bin/",["tree/usr/bin/smb-browser"])]
	)