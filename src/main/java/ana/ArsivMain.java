package ana;

import dataAccessLayer.Baglanti;

public class ArsivMain{
    public static void main (String[] args) {
        System.out.println("Naber");
        int a=2;
        int b=3;
        int c=4;
        a*=a;
        b+=b;
        c++;
        a=b+c;
        System.out.println("hayde");
        System.out.println(a);
        Baglanti baglanti=new Baglanti();
        baglanti.ac();
        baglanti.kapat();
    }
}
