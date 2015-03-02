public static ArrayList <String> ReadFile () {
  File file = new File (FileDir);
  try {
   ArrayList <String> result = new ArrayList <String> ();
   FileInputStream fis = new FileInputStream (file);
   BufferedReader br = new BufferedReader (new InputStreamReader (fis));
   String line;
   while ((line = br.readLine ())! = null) {
    result.add (line);
   }
   br.close ();
   fis.close ();
   result.remove (0);
   return result;
  } Catch (IOException e) {
   e.printStackTrace ();
   return null;
  }
 }


public static ArrayList <String[]> getFileWithError404 (ArrayList <String> data) {
  ArrayList <String[]> result = new ArrayList <String[]> ();
  for (int i = 0; i <data.size (); i + +) {
   String target = data.get (i);
   if (target.endsWith ("404")) {
    target = target.substring (43, 107);
    result.add (new String [] {target.substring (0,16), target.substring (16,32),
      target.substring (32,48), target.substring (48,64)});
   }
  }
  return result;
 }




