from pyswip import Prolog

prolog = Prolog
prolog.consult("my_file.pl")
rez = list(prolog.query("date_to_epoch(date(2023, 4, 11), Epoch)"))
print(rez)

prolog.consult("my_file2.pl")
rez = list(prolog.query("epoch_to_date(1488015561, Date)"))
print(rez)


