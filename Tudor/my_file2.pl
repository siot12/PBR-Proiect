iterate_months(Days,Final) :-
    iterate_months(Days, january,Final).

iterate_months(Days, _, Final) :-
    Days =< 31,
    Final is Days.

iterate_months(Days, Month, Final) :-
    days_in_month(Month, DaysInMonth),
    Days >= DaysInMonth,
    NewDays is Days - DaysInMonth,
    write(Month), write(': '), write(DaysInMonth), nl,
    next_month(Month, NextMonth),
    iterate_months(NewDays, NextMonth, Final).

next_month(january, february).
next_month(february, march).
next_month(march, april).
next_month(april, may).
next_month(may, june).
next_month(june, july).
next_month(july, august).
next_month(august, september).
next_month(september, october).
next_month(october, november).
next_month(november, december).
next_month(december, january).

days_in_month(january, 31).
days_in_month(february, 28).
days_in_month(march, 31).
days_in_month(april, 30).
days_in_month(may, 31).
days_in_month(june, 30).
days_in_month(july, 31).
days_in_month(august, 31).
days_in_month(september, 30).
days_in_month(october, 31).
days_in_month(november, 30).
days_in_month(december, 31).

epoch_to_date(Epoch, date(FinalYear,FinalMonth,Final)) :-
    Seconds is Epoch,
    Year is Seconds div 31556926,
    FinalYear is 1970 + Year,
    Months is Seconds div 2629743,
    FinalMonth is Months-((Year * 31556926) div 2629743)+1 ,
    Days is Seconds div 86400,
    SemiFinalDays is Days - ((Year * 31556926) div 86400),
    iterate_months(SemiFinalDays,Final).