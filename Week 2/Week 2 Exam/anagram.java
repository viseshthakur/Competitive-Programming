import java.util.*;
import java.util.Arrays;
public class anagram{
	public static void isAnagram(String input1, String input2)	{
		String str1 = input1.replaceAll("\\s", "");
		String str2 = input2.replaceAll("\\s", "");

		boolean flag = true;
		if(str1.length() != str2.length()){
			flag = false;
		}
		else{
			char[] str1array = str1.toLowerCase().toCharArray();
			char[] str2array = str2.toLowerCase().toCharArray();
			Arrays.sort(str1array);
			Arrays.sort(str2array);
			flag = Arrays.equals(str1array, str2array);
		}
		if(flag){
			System.out.println(input1+" and "+input2+" true");
		}
		else{
			System.out.println(input1+" and "+input2+" false");
		}
	}
public static void main(String[] args){
	isAnagram("anagram", "nagaram");
	isAnagram("Keep", "Peek");
	isAnagram("Mother In Law", "Hitler Woman");
	isAnagram("School Master","The Classroom ");
	isAnagram("School MASTER", "The ClassROOM");
	isAnagram("DORMITORY", "Dirty Room");
	isAnagram("ASTRONOMERS", "NO MORE STARS");
	isAnagram("Toss", "Shot");
	isAnagram("joy", "enjoy");
	isAnagram("Debit Card","Bad Credit");
	isAnagram("Dormitory","Dirty Room");
	isAnagram("SiLeNt CAT", "LisTen AcT");
	}
}
