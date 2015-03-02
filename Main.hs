{-# LANGUAGE UnicodeSyntax #-}
module Main where

import Control.Applicative ((<$>))
import Control.Monad (foldM, join)
import qualified Data.Bits as Bits
import Data.List (genericReplicate, inits)
import Data.Monoid ((<>))
import Data.Word (Word8)
import Text.Printf (printf)

import Data.ByteString (ByteString)
import qualified Data.ByteString as B
import qualified Network.Curl as C


randomByteString ∷ ByteString
randomByteString = B.replicate 16 57


main ∷ IO ()
main =
  do cipher ← B.readFile "ciphertext.dat"
     plainText ← decrypt cipher
     print plainText


decrypt ∷ ByteString → IO ByteString
decrypt cipher = B.concat . map (B.pack . B.zipWith Bits.xor randomByteString) <$> mapM decryptitionRound (ciphers cipher)
 where
  ciphers = map B.concat . drop 2 . inits . chunk 16



decryptitionRound ∷ ByteString → IO ByteString
decryptitionRound cipher = foldM (bruteforceByte cipher) (B.replicate 16 0) paddings
 where
  paddings = map (B.pack . reverse . take 16 . (<> repeat 0) . join genericReplicate) [1..16]


bruteforceByte ∷ ByteString → ByteString → ByteString → IO ByteString
bruteforceByte cipher acc padding = go 0
 where
  paddedCipher = cipher `xor` padding `xor` acc `xor` randomByteString
  go n =
    do let guess = pretty $ paddedCipher `xor` fromWord8 (B.length $ B.dropWhile (== 0) acc) n
       r ← C.withCurlDo $ C.curlGetResponse_
         ("http://crypto-class.appspot.com/po?er=" <> guess)
         [] ∷ IO (C.CurlResponse_ [(String, String)] ByteString)
       case C.respStatus r of
         403 → go (n + 1)
         _ → return (addByte n acc)


addByte ∷ Word8 → ByteString → ByteString
addByte n xs = B.replicate (16 - t - 1) 0 <> B.cons n ys
 where
  ys = B.dropWhile (== 0) xs
  t = B.length ys


xor ∷ ByteString → ByteString → ByteString
xor x y = B.concat as <> B.pack (B.zipWith Bits.xor c y) <> b
 where
  (as,c,b) = split $ chunk 16 x


fromWord8 ∷ Int → Word8 → ByteString
fromWord8 t n = B.pack $ replicate (16 - t - 1) 0 ++ n : replicate t 0


pretty ∷ ByteString → String
pretty = concatMap (printf "%02x") . B.unpack


chunk ∷ Int → ByteString → [ByteString]
chunk n bs
  | B.length bs <= n = [bs]
  | otherwise = B.take n bs : chunk n (B.drop n bs)


split ∷ [α] → ([α], α, α)
split = go []
 where
  go as [x,y] = (reverse as, x, y)
  go as (x:xs) = go (x:as) xs
  go _ _ = error "Main.split: [_]/empty list"
