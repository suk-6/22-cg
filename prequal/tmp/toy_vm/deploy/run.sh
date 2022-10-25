#!/bin/bash
#
cd /home/toy_vm
exec 2>/dev/null
timeout 300 /home/toy_vm/toy_vm
