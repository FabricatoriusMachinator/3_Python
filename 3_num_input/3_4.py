import time

bar_length = 20
current_numb = 1
total_numb = 100
##bar_calc = int(bar_length/(total_numb / current_numb))


while current_numb < total_numb:
    bar_calc = int(bar_length/(total_numb / current_numb))
    time.sleep(1)
    print("|" + "="*bar_calc + " " * (bar_length - bar_calc) + "|", end = "\r" )
    current_numb += 10