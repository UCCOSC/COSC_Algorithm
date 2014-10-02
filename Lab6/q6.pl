remove(A,[],[]).
remove(A,[H|T],Result) :- H=A, remove(A,T,Result).
remove(A,[H|T],[H|Result]) :- remove(A,T,Result).
