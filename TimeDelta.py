#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
import calendar


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = t1[3:].strip() #retira o caractere selecionado
    t2 = t2[3:].strip()

    date_format = "%d %b %Y %H:%M:%S %z"
    #dia, mês, ano, horas, minutos, segundos, adicional
    t1 = datetime.strptime(t1, date_format)
    t2 = datetime.strptime(t2, date_format)

    result = t2 - t1
    result = str(abs(int(result.total_seconds())))

    return result


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
