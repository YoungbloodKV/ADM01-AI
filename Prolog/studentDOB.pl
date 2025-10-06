person(yash,        14, 6, 2002).
person(arjun,       25, 1, 2001).
person(kavya,       3,  11, 2003).
person(sneha,       19, 6, 2002).
person(ravi,        14, 6, 2002).
person(abhishek,    22, 12, 2001).

% --- Rules ---

% 1. Retrieve DOB by name
dob(Name, Day, Month, Year) :-
    person(Name, Day, Month, Year).

% 2. Find all people born in a particular month
born_in_month(Month, Name) :-
    person(Name, _, Month, _).

% 3. Find all people born in a particular year
born_in_year(Year, Name) :-
    person(Name, _, _, Year).

% 4. Check if two people share the same birth year
same_birth_year(Name1, Name2) :-
    person(Name1, _, _, Year),
    person(Name2, _, _, Year),
    Name1 \= Name2.