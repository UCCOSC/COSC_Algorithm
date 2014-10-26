likes(bob, chocolate).
likes(rita, eat).
eats(Person, Thing) :- likes(Person, Thing).
eats(Person, Thing) :- hungry(Person), edible(Thing).

edge(a,b).
edge(b,c).
edge(d,b).
edge(d,e).
connected(Source, Destination) :- edge(Source, Destination).
connected(Source, Destination) :- edge(Source, Z),connected(Z, Destination).

goes_through(Path, Node) :- Path = [H|T],(H=Node;goes_through(T,Node)).
goes_through(Path, Node) :- Path = [Node].

connects([Source|X], Source, Destination):- X = [T|D] ,connects(X, T, Destination), edge(Source, T).
connects([T,D], Source, Destination) :- T = Source, D =  Destination, edge(Source, Destination).

crosses(Path1, Path2):- Path1 = [H|T], (goes_through(Path2, H); crosses(T, Path2)).
crosses(Path1, Path2):- Path1 = [H], goes_through(Path2, H).

person(john).
person(jane).
person(craig).
person(ann).
person(alice).
person(sean).

chats(john, jane).
chats(john, craig).
chats(ann, alice).

enjoys(jane, ice-creame).
enjoys(sean, reading).

friends(F1, F2) :- chats(F1, F2).
friends(F1, F2) :- chats(F2, F1).

connecteds(F1, F2) :- friends(F1, F2).
connecteds(F1, F2) :- friends(F1, F), friends(F, F2).

disconnected(P1,X) :- not(connecteds(P1,X)).





reflection(point(X,Y), point(Y,X)).


word(abalone,a,b,a,l,o,n,e). 
word(abandon,a,b,a,n,d,o,n). 
word(enhance,e,n,h,a,n,c,e). 
word(anagram,a,n,a,g,r,a,m). 
word(connect,c,o,n,n,e,c,t). 
word(elegant,e,l,e,g,a,n,t).

solution(V1,V2,V3,H1,H2,H3):-
    word(V1,_,X,_,_,_,_,_), word(H1,_,X,_,_,_,_,_),
    word(V1,_,_,_,Y,_,_,_), word(H2,_,Y,_,_,_,_,_),
    word(V1,_,_,_,_,_,Z,_), word(H3,_,Z,_,_,_,_,_),
    
    word(V2,_,A,_,_,_,_,_), word(H1,_,_,_,A,_,_,_),
    word(V2,_,_,_,B,_,_,_), word(H2,_,_,_,B,_,_,_),
    word(V2,_,_,_,_,_,C,_), word(H3,_,_,_,C,_,_,_),
    
    word(V3,_,D,_,_,_,_,_), word(H1,_,_,_,_,_,D,_),
    word(V3,_,_,_,E,_,_,_), word(H2,_,_,_,_,_,E,_),
    word(V3,_,_,_,_,_,F,_), word(H3,_,_,_,_,_,F,_).


mirror(leaf(X), leaf(X)).
mirror(tree(L, R), tree(A, B)) :- mirror(R, A), mirror(L, B).


/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.
/* age-related clauses */
young(AGE) :- AGE < 45.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
    Recommend = no_lenses, low_tear_rate(Tear_Rate);
    Recommend = hard_lenses, Astigmatic == yes, young(Age),
        normal_tear_rate(Tear_Rate);
    Recommend = soft_lenses, Astigmatic == no, young(Age),
        normal_tear_rate(Tear_Rate).


directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).
contains(Outer, Inner) :- 
    directlyIn(Inner, Outer);
    directlyIn(Inner, X), contains(X, Inner).
