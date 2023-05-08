% Determine if a year is a leap year
leap_year(Year) :-
    0 is mod(Year, 4),
    (mod(Year, 100) \= 0 ; mod(Year, 400) =:= 0).

% Get the number of days in a given month of a given year
days_in_month(Year, Month, Days) :-
    nth0(Month, [31,28,31,30,31,30,31,31,30,31,30,31], DaysList),
    (Month =:= 1, leap_year(Year) -> Days is 29 ; Days is DaysList).

% Convert a date to an epoch timestamp
date_to_epoch(date(Year, Month, Day), Epoch) :-
    % Calculate the number of seconds between the Unix epoch and the given date
    days_in_month(Year, Month, DaysInMonth),
    EpochSeconds is ((Year - 1970) * 31556926) +  % Number of seconds in a year
                  (DaysInMonth * 86400 * (Month - 1)) +  % Number of seconds in previous months
                  ((Day - 1) * 86400),           % Number of seconds in the current day

    % Return the epoch timestamp
    Epoch is EpochSeconds.

% Calculate the difference between two dates in days
date_difference(date(Year1, Month1, Day1), date(Year2, Month2, Day2), Difference) :-
    date_to_epoch(date(Year1, Month1, Day1), Epoch1),
    date_to_epoch(date(Year2, Month2, Day2), Epoch2),
    DifferenceSeconds is abs(Epoch2 - Epoch1),
    Difference is DifferenceSeconds // 86400.  % Convert seconds to days

