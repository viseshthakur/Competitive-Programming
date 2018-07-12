import java.util.*;
class QueueHK{
	public static void main(String[] args) {
		int grid[][]= {{7,0}, {4,4}, {7,1}, {5,0}, {6,1}, {5,2}};
		int gi[][]=reconstructQueue(grid);
		for (int i = 0; i <gi.length; i++) {
			for (int j = 0; j <gi.length ; i++) {
			}
		}
	}
	
	public static int[][] reconstructQueue(int[][] people) {
		int[][] result = new int[people.length][];
		Arrays.sort(people, new Comparator<int[]>(){
			public int compare(int[] a1, int[] a2){
				if(a1[0]!=a2[0]){
					return a2[0]-a1[0];
				}
				else{
					return a1[1]-a2[1];
				}
			}
		});
	ArrayList<int[]> list = new ArrayList<int[]>();
	for(int i=0; i<people.length; i++){
		int[] arr = people[i];
		list.add(arr[1],arr);
	}
	for(int i=0; i<people.length; i++){
		result[i]=list.get(i);
	}
	return result;
	}
}