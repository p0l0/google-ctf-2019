#!/bin/bash
sed `cat map | awk '{print "-e s/"$1"/"$3"/g"}'`<<<"`cat program`" > xprogram
sed `cat map | awk '{print "-e s/"$1"/"$3"/g"}'`<<<"`cat vm.py`" > xvm.py