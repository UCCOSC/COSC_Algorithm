(defn my-tr-count 
    ([x] (my-tr-count x 0))
    ([x a]
        (if (empty? x)
            a
            (recur (rest x) (+ 1 a))
        )
    )

