from sys import argv
script_name, name, time, stake, premium = argv
print ('имя скрипта: ',script_name)
print ('имя работника: ',name)
print ('выработка работника в часах: ',time)
print ('ставка в час: ',stake)
print ('премия: ',premium)
print ('заработная плата = (выработка *ставка )+премия = ', (int(time)*int(stake))+int(premium))