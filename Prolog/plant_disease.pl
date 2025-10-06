% Facts: disease(Name, RecommendedFoods, AvoidFoods).

disease(diabetes,
        [vegetables, oats, brown_rice, fruits_in_moderation, nuts],
        [sugar, sweets, white_rice, white_bread]).

disease(hypertension,
        [fresh_fruits, green_vegetables, low_salt_foods, oats],
        [salt, pickles, fried_food, junk_food]).

disease(obesity,
        [fruits, green_salads, soups, whole_grains, lemon_water],
        [sweets, oil_foods, fast_food, aerated_drinks]).

disease(anemia,
        [green_leafy_vegetables, jaggery, beetroot, apple, pomegranate],
        [coffee, tea, junk_food]).

disease(heart_disease,
        [olive_oil, oats, fruits, vegetables, lean_meat],
        [fried_foods, butter, cheese, red_meat]).

% Rule: Suggest diet based on disease
diet_suggestion(Disease) :-
    disease(Disease, Recommended, Avoid),
    format('~nRecommended Diet for ~w:~n', [Disease]),
    write('  Eat: '), write(Recommended), nl,
    write('  Avoid: '), write(Avoid), nl.

% Interactive rule (optional)
run_diet_advice :-
    write('Enter your disease (in lowercase, e.g., diabetes.): '),
    read(Disease),
    (diet_suggestion(Disease) -> true;
     write('Sorry, no data available for that condition.'), nl).