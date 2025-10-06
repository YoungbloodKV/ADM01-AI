male(ram).
male(raju).
male(amit).
male(raj).
male(karthik).

female(sita).
female(lakshmi).
female(priya).
female(anu).

% Parent relationships
parent(ram, raju).
parent(ram, lakshmi).
parent(sita, raju).
parent(sita, lakshmi).

parent(raju, amit).
parent(priya, amit).

parent(lakshmi, raj).
parent(karthik, raj).

parent(amit, anu).

% --- Rules ---

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    male(X),
    grandparent(X, Y).

grandmother(X, Y) :-
    female(X),
    grandparent(X, Y).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).