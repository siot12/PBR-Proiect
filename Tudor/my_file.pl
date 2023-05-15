% Functie care ne ajuta sa aflam daca un an este bisect sau nu
leap_year(Year) :-
    0 is mod(Year, 4),
    (mod(Year, 100) \= 0 ; mod(Year, 400) =:= 0).

$ Functie care ne ajuta sa aflam numarul de zile dintr-o luna a unui an dat
days_in_month(Year, Month, Days) :-
    nth0(Month, [31,28,31,30,31,30,31,31,30,31,30,31], DaysList),
    (Month =:= 1, leap_year(Year) -> Days is 29 ; Days is DaysList).

% Functie care ne ajuta sa aflam timestamp-ul unui an dat
date_to_epoch(date(Year, Month, Day), Epoch) :-
    % Calculam numarul de secunde dintre epoch-ul Unix si data data
    days_in_month(Year, Month, DaysInMonth),
    EpochSeconds is ((Year - 1970) * 31556926) +  % Number of seconds in a year
                  (DaysInMonth * 86400 * (Month - 1)) +  % Number of seconds in previous months
                  ((Day - 1) * 86400),           % Number of seconds in the current day

    % Returnam timestamp-ul
    Epoch is EpochSeconds.