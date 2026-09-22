#!/bin/bash
mkdir -p proyecto/{docs,src/modulos,config,logs/backup,test/resultados}
touch proyecto/docs/{manual.txt,guia.txt,referencias.txt}
touch proyecto/src/{script1.sh,script2.sh} proyecto/src/modulos/modulos1.py
touch proyecto/config/{app.cfg,db.cfg}
touch proyecto/logs/{access.log,error.log} proyecto/logs/backup/backup1.log
touch proyecto/test/{test1.txt, test2.txt} proyecto/test/resultados/resultados1.txt