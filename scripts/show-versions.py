#!/usr/bin/env python3
#
# Copyright (c) 2018-2024, Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#
# Show installed versions of doc building tools (per requirements.txt)

import os.path
import sys
import pkg_resources
import subprocess

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Check all requirements listed in requirements.txt and print out version # installed (if any)
reqfile = os.path.join(sys.path[0], "requirements.txt")
print ("doc build tool versions found on your system per " + reqfile + "...\n")

rf = open(reqfile, "r")

for reqs in pkg_resources.parse_requirements(rf):
    try:
        ver = pkg_resources.get_distribution(reqs.project_name).version
        print ("  " + reqs.project_name.ljust(25," ") + " version: " + ver)
        if not reqs.__contains__(ver):
            print (color.RED + color.BOLD + "   >>> Warning: Expected version " +
                    reqs.__str__() + " Python module from scripts/requirements.text." + color.END)
    except:
        print (color.RED + color.BOLD + reqs.project_name + " is missing." + color.END +
                " (Hint: install all dependencies with " + color.YELLOW +
                "\"pip3 install --user -r scripts/requirements.txt\"" + color.END + ")")

rf.close()

# Print out the version of relevent packages not installed via pip
# print ("  " + "doxygen".ljust(25," ") + " version: " + subprocess.check_output(["doxygen", "-v"]).decode("utf-8"))