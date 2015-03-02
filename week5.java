 public static final BigInteger two_BigInt = new BigInteger("2");
 public static final BigInteger twenty_BigInt = new BigInteger("20");
 
 public static final String p_String =
   "134078079299425970995740249982058461274793658205923933" +
   "777235614437217640300735469768018742981669034276900318" +
   "58186486050853753882811946569946433649006084171";
 
 public static final String g_String =
   "117178298803662070095161175963353670885580849999989522" +
   "055999794590639294997365837466705721764714603129285948" +
   "29675428279466566527115212748467589894601965568";
 
 public static final String h_String =
   "032394751040504504435652643787280657886490975209524495" +
   "278347924529719819761432925580738569379585531805328789" +
   "28001494706097394108577585732452307673444020333";
 
 public static final BigInteger p_BigInt = new BigInteger(p_String);
 public static final BigInteger g_BigInt = new BigInteger(g_String);
 public static final BigInteger h_BigInt = new BigInteger(h_String);
 
 public static final BigInteger g_inverse_BigInt = g_BigInt.modInverse(p_BigInt);
 
 public static final BigInteger B = two_BigInt.modPow(twenty_BigInt, p_BigInt);
 
 public static final BigInteger GtoB = g_BigInt.modPow(Dlog.B, p_BigInt);
 
 public Map<BigInteger, BigInteger> x0_hashMap = new HashMap<BigInteger, BigInteger>();
 
 public void createHashMap_x0(){
  BigInteger tempResult = Dlog.h_BigInt;
  for (BigInteger i = BigInteger.ONE; i.compareTo(B) != 1; i = i.add(BigInteger.ONE)){
   tempResult = tempResult.multiply(g_inverse_BigInt).mod(p_BigInt);
   this.x0_hashMap.put(tempResult, i);
   System.out.println("Saving hashmap " + i);
  }
 }
 
 public void checkHashCollision(){
  BigInteger temp2 = BigInteger.ONE;
  for (BigInteger i = BigInteger.ONE; i.compareTo(B) != 1; i = i.add(BigInteger.ONE)){
   temp2 = temp2.multiply(GtoB).mod(p_BigInt);
   
   if (this.x0_hashMap.containsKey(temp2)){
    System.out.println("Find Collision!");
    System.out.println("x0 = " + i);
    System.out.println("x1 = " + this.x0_hashMap.get(temp2));
    BigInteger result = i.multiply(B).add(this.x0_hashMap.get(temp2)).mod(p_BigInt);
    System.out.println(" x = " + result.toString());
    break;
   }else{
    System.out.println("Checking hashmap " + i + " no!");
   }
  }
 }
 
 public static void main(String[] args){
  Dlog dlog = new Dlog();
  dlog.createHashMap_x0();
  dlog.checkHashCollision();
  BigInteger _h = g_BigInt.modPow(new BigInteger("375374217830"), p_BigInt);
  System.out.println(_h);
 }
