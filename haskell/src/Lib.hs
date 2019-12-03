module Lib where

part1a :: IO ()
part1a = print . sum . map (fuel . read) . lines =<< readFile "../1.txt"
  where
    fuel :: Int -> Int
    fuel = subtract 2 . (`div` 3)

part1b :: IO ()
part1b = print . sum . map (fuel . read) . lines =<< readFile "../1.txt"
  where
    fuel :: Int -> Int
    fuel x = if x < 9
             then 0
             else let r = (x `div` 3) - 2
                  in r + fuel r

someFunc :: IO ()
someFunc = part1b
