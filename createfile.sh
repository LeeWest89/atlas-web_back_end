#!/usr/bin/env bash                                                 

#Create files easy                                                  

for f in $@                                                         

do                                                                  

        echo "#include" >> $f                                       

        chmod u+x $f                                                

done