"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
import math

digits = 1
result = False

MaxNum = 1929394959697989990

digits = int(math.sqrt(MaxNum))


while result == False:
    calc = str(digits ** 2)
    if len(calc) < 18:
        digits -= 1
    else:
        try:
            if (calc[0] == "1") and (calc[2] == "2") and (calc[4] == "3") and (calc[6] == "4") and (calc[8] == "5") and (calc[10] == "6") and (calc[12] == "7") and (calc[14] == "8") and (calc[16] == "9") and (calc[18] == "0"):
                result = True
            else:
                digits -= 1
        except:
            digits -= 1
print(digits)
