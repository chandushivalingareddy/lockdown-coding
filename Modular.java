import java.io.*; 
class Modular 
{ 
    static int power(int x, int y, int p) 
    { 
         int res = 1;      
         x = x % p;  
         if (x == 0) return 0;     
         while (y > 0) 
        { 
            if((y & 1)==1) 
            res = (res * x) % p; 
            y = y >> 1;  
            x = (x * x) % p;  
        } 
        return res; 
    } 
public static void main(String args[]) 
  { 
        int x = 2; 
        int y = 5; 
        int p = 13; 
        System.out.println("Power is " + power(x, y, p)); 
  } 
} 
