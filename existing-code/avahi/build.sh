#!/bin/bash

rm -f *.o
rm -f client-browse-services

gcc -fPIC -Wall -g -c client-browse-services.c

# TODO: use -lNAME
gcc /usr/lib64/libavahi-client.so /usr/lib64/libavahi-common.so client-browse-services.o -o client-browse-services

