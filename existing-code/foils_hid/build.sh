#!/bin/bash

rm -f *.o
rm -f mouse remote

gcc -fPIC -g -Wall -c term_input.c
gcc -fPIC -g -Wall -c mapping.c

gcc -fPIC -g -Wall -c mouse.c
gcc -fPIC -g -Wall -c remote.c

gcc -Wall -g -pipe -fexceptions -Wl,-z,relro -o mouse mouse.o /usr/lib64/libfoils_hid.a -lrudp -lela -lm
gcc -Wall -g -pipe -fexceptions -Wl,-z,relro -o remote remote.o term_input.o mapping.o /usr/lib64/libfoils_hid.a -lrudp -lela -lm

