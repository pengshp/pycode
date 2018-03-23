#!/usr/bin/env python3
#

from fabric.api import local,settings, abort
from fabric.contrib.console import confirm



def test():
    with settings(warn_only=True):
        result = local('sl', capture=True)
    if result.failed and not confirm("Tests failed,continue anyway?"):
    	abort("Aborting at user request.")

    local('ls')
