# from string import maketrans
fin = open("#21.1.5file", "r")
fout = open("#21.1.5file_out", "w")
a = fin.readline()
intab_upper = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
outtab_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
intab_lower = "zabcdefghijklmnopqrstuvwxy"
outtab_lower = "abcdefghijklmnopqrstuvwxyz"
upper_replacement = a.maketrans(intab_upper, outtab_upper)
lower_replacement = a.maketrans(intab_lower, outtab_lower)
a1 = a.translate(upper_replacement)
a_final = a1.translate(lower_replacement)
fout.write(a_final)
fin.close()
fout.close()
