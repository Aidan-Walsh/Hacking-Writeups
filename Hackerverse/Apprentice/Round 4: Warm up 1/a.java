import java.util.Scanner;

public class a {
   private static int[] b = new int[256];
   private static int[] c = new int[]{121, 37, 114, 122, 34, 99, 32, 127, 118};
   private static int d = 23;

   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.print(new String(new char[]{'P', 'a', 's', 's', 'w', 'o', 'r', 'd', ':', ' '}));
      String var2 = var1.nextLine();
      var1.close();
      if (i(var2)) {
         System.out.println(new String(new char[]{'A', 'c', 'c', 'e', 's', 's', ' ', 'g', 'r', 'a', 'n', 't', 'e', 'd', '.'}));
      } else {
         System.out.println(new String(new char[]{'A', 'c', 'c', 'e', 's', 's', ' ', 'd', 'e', 'n', 'i', 'e', 'd', '.'}));
      }

   }

   private static boolean i(String var0) {
      if (var0 != null && var0.length() == k()) {
         char[] var1 = var0.toCharArray();
         return m(var1) && n(var1) && o(var1);
      } else {
         return false;
      }
   }

   private static int k() {
      return c.length;
   }

   private static boolean m(char[] var0) {
      int var1 = 0;

      for(int var2 = 0; var2 < var0.length; ++var2) {
         var1 += var0[var2] * (var2 + 1) ^ b[var2 % 256];
      }

      return (var1 & '\uffff') == 3743;
   }

   private static boolean n(char[] var0) {
      int var1 = 0;

      for(int var2 = 0; var2 < var0.length; ++var2) {
         var1 ^= var0[var2] << var2 % 8;
      }

      return var1 == 13443;
   }

   private static boolean o(char[] var0) {
      int var1 = u();

      for(int var2 = 0; var2 < var0.length; ++var2) {
         int var3 = c[var2] ^ var1;
         if (var0[var2] != var3) {
            return false;
         }
      }

      return true;
   }

   private static int u() {
      byte var0 = 51;
      int var1 = var0 ^ 36;
      var1 += 8;
      var1 -= 14;
      return var1;
   }

   private static String y() {
      int[] var0 = new int[]{112, 97, 115, 115, 119, 111, 114, 100};
      StringBuilder var1 = new StringBuilder();
      int[] var2 = var0;
      int var3 = var0.length;

      for(int var4 = 0; var4 < var3; ++var4) {
         int var5 = var2[var4];
         var1.append((char)(var5 ^ 16));
      }

      return var1.toString();
   }

   private static boolean cc(String var0) {
      return var0.equals(new String(new char[]{'a', 'd', 'm', 'i', 'n', '1', '2', '3'}));
   }

   private static boolean ee(char[] var0) {
      long var1 = 1L;
      char[] var3 = var0;
      int var4 = var0.length;

      for(int var5 = 0; var5 < var4; ++var5) {
         char var6 = var3[var5];
         var1 = var1 * (long)var6 % 1000000007L;
      }

      return var1 == 123456789L;
   }

   static {
      for(int var0 = 0; var0 < 256; ++var0) {
         b[var0] = var0 * 1103515245 + 12345 & 255;
      }

   }
}
