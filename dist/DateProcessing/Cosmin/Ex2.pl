%distance_between_dates(date(2023,10, 10), date(2089,1, 1), Days).

% to check if year is leap
is_leap_year(Year) :-
    0 is Year mod 4,
    (0 \= Year mod 100; 0 is Year mod 400).

% foreach month => days 

% month with 31 days
days_in_month(1, _, 31).
days_in_month(3, _, 31).
days_in_month(5, _, 31).
days_in_month(7, _, 31).
days_in_month(8, _, 31).
days_in_month(10, _, 31).
days_in_month(12, _, 31).

% for february, if leaf => 29 days 
days_in_month(2, Year, 29) :- is_leap_year(Year).

% for february, if not leaf => 28 days 
days_in_month(2, _, 28).

% month with 30 days
days_in_month(4, _, 30).
days_in_month(6, _, 30).
days_in_month(9, _, 30).
days_in_month(11, _, 30).

% get distance between dates in days
distance_between_dates(Date1, Date2, Days) :-
    % so it doesn't matter the order of dates
    Date1 @< Date2 -> 
        calculate_distance(Date1, Date2, Days)
    ;   
        calculate_distance(Date2, Date1, Days).

calculate_distance(Date, Date, 0).
% count distance in days
calculate_distance(date(Year1, Month1, Day1), date(Year2, Month2, Day2), Distance) :-
    days_in_month(Month1, Year1, Days),
    NextDay is Day1 + 1,
    (NextDay =< Days ->
        % if new day is in current month
        NewDate = date(Year1, Month1, NextDay),
        calculate_distance(NewDate, date(Year2, Month2, Day2), TempDistance),
        Distance is TempDistance + 1
    ;
        % if new day is in next month
        NextMonth is Month1 + 1,
        (NextMonth =< 12 ->
            % if new month is in current year
            NewDate = date(Year1, NextMonth, 1),
            calculate_distance(NewDate, date(Year2, Month2, Day2), TempDistance),
            Distance is TempDistance + 1
        ;
            % if new month is in next year
            NextYear is Year1 + 1,
            NewDate = date(NextYear, 1, 1),
            calculate_distance(NewDate, date(Year2, Month2, Day2), TempDistance),
            Distance is TempDistance + 1
        )
    ).