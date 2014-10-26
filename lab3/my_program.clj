(defn product [list1]
    (apply * list1)
)

(defn my-count [l]
    (if (empty? l)
        0
        (+ 1 (my-count (rest l)))
    )
)

(defn col-sum[l]
    (map + (first l) (last l))
)

(defn row-sum[l]
    (list (reduce + (first l)) (reduce + (last l)))
)

(defn append-row[l1 l2]
    (if (empty? l1)
        (cons l2 l1)
        (cons (first l1) (append-row (rest l1) l2)))
)


(defn get-counts[lis]
    (map count lis)
)

(defn my-map [func lst]
    (if (empty? lst)
        ()
        (cons (func (first lst)) (my-map func (rest lst)))
    )
)

(defn my-filter [func lst]
    (cond
        (empty? lst)
        ()
        (func (first lst))
        (cons (first lst)(my-filter func (rest lst)))
        :else (my-filter func (rest lst))
    )
)

(defn is-sorted? [l]
    (cond
        (empty? (rest l)) true
        (< (first l) (first (rest l)))
        (is-sorted? (rest l))
        :else false
    )
)

(defn member? [a ls]
    (cond
        (empty? ls) false
        (= a(first ls)) true
        :else (recur a (rest ls))))

(defn union [set1 set2]
    (cond
        (empty? set1) set2
        (member? (first set1) set2) (recur(rest set1) set2)
        :else (recur(rest set1) (cons(first set1) set2))))

(defn my-last [l]
    (if (= (rest l) ())
        (first l)
        (my-last (rest l))
    )
)

(defn append [l x]
    (if (empty? l)
        (cons x l)
        (cons (first l) (append (rest l) x)))
)

(defn transpose [l]
    (apply map (cons list l))
)

(defn arg-max [fnn l]
    (cond (empty? l) nil :else
    (reduce (fn [x y]
        (cond
            (> (fnn x) (fnn y)) x
            :else y))
    l))
)   

(defn my-tr-count 
    ([x] (my-tr-count x 0))
    ([x acc]
        (if (empty? x)
            acc
            (recur (rest x) (+ 1 acc)))))

(defn my-tr-reverse 
    ([x] (my-tr-reverse x ()))
    ([x acc]
        (if (empty? x)
            acc
            (recur (rest x) (cons (first x) acc)))))

(defn item? [i l]
    (cond
        (empty? l) false
        (= i (first l)) true
        :else (item? i (rest l))))
 
 
(defn my-tr-intersection
    ([l1 l2] (my-tr-intersection l1 l2 ()))
    ([l1 l2 common]
        (cond
            (empty? l1) common
            (item? (first l1) l2)
                (recur (rest l1) l2 (cons (first l1) common))
            :else (recur (rest l1) l2 common))))

(defn conjoin [& preds] (apply every-pred preds))

(defn compose-two [func1 func2]
    :else (fn [arg] (func2 (func1 arg))))

(defn compose [& funcs]
    (cond
        (empty? funcs) (fn [arg] (identity arg))
        (= (count funcs) 1) (fn [arg] ((first funcs) arg))
        :else (reduce compose-two funcs)
))

(defn one-by-n [item lis]
    (if (empty? lis)
        '()
        (cons (flatten (list item (first lis))) (one-by-n item (rest lis)))))
 
(defn n-by-n [lis1 lis2]
    (cond (empty? lis1) '()
        :else (concat (one-by-n (first lis1) lis2) (n-by-n (rest lis1) lis2))
))

(defn cartesian-product [& sets]
    (if (= (count sets) 1) (one-by-n '() (first sets))
        (reduce n-by-n sets)
))

