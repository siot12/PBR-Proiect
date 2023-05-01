zile_pe_luna([31,28,31,30,31,30,31,31,30,31,30,31]).

zile_in_luna(Luna, An, Zile) :-
    (Luna = 2, mod(An, 4) = 0, (mod(An, 100) = 0 ; mod(An, 400) = 0) ->
        Zile is 29
    ;
        zile_pe_luna(ZilePeLuna),
        nth1(Luna, ZilePeLuna, Zile)
    ).

adauga_zile_la_data(Data, N, Rezultat) :-
    atom_chars(Data, [Z1, Z2,'-', L1, L2,'-',Y1, Y2, Y3, Y4]),
    number_chars(An, [Y1, Y2, Y3, Y4]),
    number_chars(Luna, [L1, L2]),
    number_chars(Zi, [Z1, Z2]),
    date_time_value(year, Data1, An),
    date_time_value(month, Data1, Luna),
    date_time_value(day, Data1, Zi),
    adauga_zile_la_data_helper(Zi, Luna, An, N, Rezultat).

adauga_zile_la_data_helper(Zi, Luna, An, N, Rezultat) :-
    zile_in_luna(Luna, An, ZileInLuna),
    ZiUrmatoare is Zi + N - 1, % Deduct 1 from N because we've already counted the current day
    (ZiUrmatoare >= ZileInLuna ->
        NewLuna is Luna + 1,
        (NewLuna > 12 ->
            NewAn is An + 1,
            NewLuna1 is NewLuna - 12
        ;
            NewAn = An,
            NewLuna1 is NewLuna
        ),
        adauga_zile_la_data_helper(ZiUrmatoare - ZileInLuna + 1, NewLuna1, NewAn, 1, Rezultat)
    ;
        Rezultat = [ZiUrmatoare, Luna, An]
    ).
