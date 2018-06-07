#!/bin/bash

counter=2

while [ $counter -le 20 ]
    do
        echo $counter
        ((counter++))
        ((counter++))
    done

echo 'All done'
