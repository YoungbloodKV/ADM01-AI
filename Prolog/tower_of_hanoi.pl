% Base case:
move(1, Source, _, Destination) :-
    format('Move top disk from ~w to ~w~n', [Source, Destination]).

% Recursive case:
move(N, Source, Auxiliary, Destination) :-
    N > 1,
    M is N - 1,
    move(M, Source, Destination, Auxiliary),
    move(1, Source, Auxiliary, Destination),
    move(M, Auxiliary, Source, Destination).

% Run using: ?- move(NumberOfDisks, source, auxiliary, destination).
