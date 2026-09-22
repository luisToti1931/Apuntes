#!/bin/bash
cat archivo2.txt archivo1.txt > nuevoarchivo.txt
cat archivo1.txt archivo2.txt > nuevoarchivo.txt
mv nuevoarchivo.txt archivo2.txt