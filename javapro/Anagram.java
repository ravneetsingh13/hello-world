//WAP to check if two given strings are anagram or not
import java.util.Scanner;

//Driver Class
class Anagram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter String s:");
		String s = sc.nextLine();
		System.out.println("Enter String t:");
		String t = sc.nextLine();
		
		AnagramMain am = new AnagramMain();
		boolean op = am.findAnagram(s,t);
		System.out.println(op);
	}
}

//Business Class
class AnagramMain {
	public boolean findAnagram(String s, String t) {
		int n=s.length();
		int[] ch = new int[26];
		if(n!=t.length())
			return false;
		
		for(int i=0;i<n;i++) {
			ch[s.charAt(i)-'a']++;
			ch[t.charAt(i)-'a']--;
		}
		for(int i : ch)
			if(ch[i]!=0)
				return false;
		return true;
	}
}