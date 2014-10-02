eats(bob, Thing) :-
    hungry(bob),
    edible(Thing).
 
eats(alice, Thing) :-
    hungry(alice),
    edible(Thing),
    not(fast_food(Thing)).
 
 

second([_,Sec|_], X) :-
    X = Sec.
 
 

swap12([X, Y|Tail], [Y, X|Tail]).
 
 

listtran([], []).
listtran([Ger|Gtail], [Eng|Etail]) :-
    tran(Ger, Eng),
    listtran(Gtail, Etail).
 
 

twice([], []).
twice([H|T1], [H,H|T2]) :-
    twice(T1, T2).
 
 

addone([], []).
addone([L1|T1], [L2|T2]) :- L2 is L1 + 1,
                            addone(T1, T2).
 
 

trim_ends([_,_], []).
trim_ends([H1,H2|T], [L|LT]) :-
    append([H1],T,X), H2 = L, trim_ends(X, LT).
 
 

swap_ends([X,Y], [Y,X]).
swap_ends([H1,X1|T1], [H2,X2|T2]) :-
    X1 = X2, append([H1], T1, Reduced1), append([H2], T2, Reduced2),
        swap_ends(Reduced1, Reduced2).
 
 

element(List, Index, Val, Incr) :-
    Index = Incr, List = [H|_], Val = H.
 
element(List, Index, Val, Incr) :-
    List = [_|T], Incr2 is Incr + 1, element(T, Index, Val, Incr2).
 
element(List, Index, Val) :-
    element(List, Index, Val, 0).
    
    
remove(A,[],[]).
remove(A,[H|T],Result) :- H=A, remove(A,T,Result).
remove(A,[H|T],[H|Result]) :- remove(A,T,Result).
