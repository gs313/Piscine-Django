#!/bin/bash
LINK=$(curl -s -I $1 | grep -i location | cut -d' ' -f2 )
echo $LINK
