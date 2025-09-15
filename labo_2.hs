{--
problema todoMenor (t1, t2: RxR): Bool {
    requiere: {True}
    asegura: {res = True <-> (a_1 <= b_1 y a_2 <= b_2)}
}
--}

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (a,b) (c,d)
    | (a <= c) && (b <= d) = True
    | otherwise = False

{--
problema posPrimerPar (t: ZxZxZ): Z {
    requiere: {True}
    asegura: {
        (res = 1 <-> t1 es par) y
        (res = 2 <-> t2 es par y t1 es impar) y
        (res = 3 <-> t3 es par y t1 y t2 son impares) y
        (res = 4 <-> t1,t2,t3 son impares)
    }
}
--}

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a,b,c)
    |mod a 2 == 0 = 1
    |mod b 2 == 0 = 2
    |mod c 2 == 0 = 3
    |otherwise = 4

{-- 
problema factorial: (n: Z): Z {
    requiere: {n >= 0}
    asegura: {factorial n = n*(n-1)*(n-2)...(n-(n-1))}
}
--}

factorial :: Int -> Int
factorial n
    |n == 0 = 1
    |n > 0 = n * factorial (n-1)

{-- 
problema fibonacci: (n: Z): Z {
    requiere: {n >= 0}
    asegura: {res = fib(n)}
}
--}

fibonacci :: Int -> Int
fibonacci n
    |n == 0 = 0
    |n == 1 = 1
    |n >= 2 = fibonacci (n-1) + fibonacci (n-2)

{-- 
problema parteEntera: (n: R): Z {
    requiere: {n >= 0}
    asegura: {res <= n < res + 1}
}
--}

parteEntera :: Float -> Int
parteEntera n
    |n < 1 && n >= 0 = 0
    |otherwise = 1 + parteEntera(n-1)

{-- 
problema iesimoDigito: (n: Z, i: Z): Z {
    requiere: {n >= 0 y 1 <= i <= cantDIgitos(n)}
    asegura: {res = (n div 10**(cantDigitos(n)-i)) mod 10}
}

problema cantDigitos: (n: Z): Z {
    requiere: {n >= 0}
    asegura: {
        n = 0 -> res = 1
        n /= 0 -> (n div 10**(res-1) > 0 y n div 10**res = 0)
    }
}
--}

cantDigitos :: Integer -> Integer
cantDigitos n
    |n < 10 = 1
    |otherwise = cantDigitos(div n 10) + 1

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i
    |cantDigitos n == i = mod n 10
    |otherwise = iesimoDigito (div n 10) i