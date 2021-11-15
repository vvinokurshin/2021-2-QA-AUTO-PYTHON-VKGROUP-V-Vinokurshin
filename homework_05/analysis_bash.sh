#!/bin/bash

file=$1

if [ -f res_bash.txt ]
then
    rm res_bash.txt
fi

touch res_bash.txt

{   
    printf "Общее количество запросов:\n"
    wc $file | awk '{print $1}'

    printf "\nКоличество запросов каждого типа:\n"
    cat $file | awk 'length($6)<=10 {print substr($6,2)}' | sort | uniq -c | sort -n # HEAD НА ОДИН МЕНЬШЕ?

    printf "\nТоп 10 самых частых запросов:\n"
    cat $file | awk '{print $7}' | sort | uniq -c | sort -rn | head -10 

    printf "\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n"
    cat $file | awk 'int($9/100)==4 {print $1 " " $9 " " $10 " " $7}' | sort -rnk3 | head -5

    printf "\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n"
    cat $file | awk 'int($9/100)==5 {print $1}' | sort | uniq -c | sort -rn | head -5

} >> res_bash.txt
