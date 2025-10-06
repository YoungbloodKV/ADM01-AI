/* PLANETS DB (Prolog)
   Author: Yash  (Reg No: 19255)
   Usage: consult('planets_db.pl').
*/

% planet(Name, Type, MassInEarths, RadiusKm, DistanceAU, Moons, HasRings, Star).

planet(mercury, terrestrial, 0.055, 2439, 0.39, 0, no, sun).
planet(venus,   terrestrial, 0.815, 6052, 0.72, 0, no, sun).
planet(earth,   terrestrial, 1.000, 6371, 1.00, 1, no, sun).
planet(mars,    terrestrial, 0.107, 3389, 1.52, 2, no, sun).

planet(jupiter, gas_giant, 317.8, 69911, 5.20, 95, yes, sun).
planet(saturn,  gas_giant, 95.16, 58232, 9.58, 83, yes, sun).
planet(uranus,  ice_giant, 14.54, 25362, 19.2,  27, yes, sun).
planet(neptune, ice_giant, 17.15, 24622, 30.1,  14, yes, sun).

% --- Derived predicates (rules) ---

% inner planets (approx: inside asteroid belt ~ < 2 AU)
inner_planet(P) :- planet(P, _, _, _, D, _, _, _), D < 2.0.
outer_planet(P) :- planet(P, _, _, _, D, _, _, _), D >= 2.0.

% broader categories
terrestrial(P) :- planet(P, terrestrial, _, _, _, _, _, _).
giant(P)       :- planet(P, T, _, _, _, _, _, _), (T = gas_giant ; T = ice_giant).

% has moons / ringed giant
has_moons(P)    :- planet(P, _, _, _, _, M, _, _), M > 0.
ringed_giant(P) :- planet(P, T, _, _, _, _, yes, _), (T = gas_giant ; T = ice_giant).

% compare masses
more_massive_than(A, B) :-
    planet(A, _, MA, _, _, _, _, _),
    planet(B, _, MB, _, _, _, _, _),
    MA > MB.

% sibling planets (share the same star, distinct)
sibling_planet(A, B) :-
    planet(A, _, _, _, _, _, _, Star),
    planet(B, _, _, _, _, _, _, Star),
    A \= B.

% Simple habitable zone (very rough, for Sun ~ 0.95–1.67 AU)
in_habitable_zone(P) :-
    planet(P, _, _, _, D, _, _, sun),
    D >= 0.95, D =< 1.67.

% Potentially habitable: terrestrial + in HZ + mass within [0.1, 5] Earths
potentially_habitable(P) :-
    terrestrial(P),
    in_habitable_zone(P),
    planet(P, _, M, _, _, _, _, _),
    M >= 0.1, M =< 5.

% Nice labels for display (optional)
info(P) :-
    planet(P, T, M, R, D, Moons, Rings, Star),
    format('~w: type=~w, mass(E)=~w, radius(km)=~w, dist(AU)=~w, moons=~w, rings=~w, star=~w~n',
           [P,T,M,R,D,Moons,Rings,Star]).
