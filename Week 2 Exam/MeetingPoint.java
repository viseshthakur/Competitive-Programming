import java.util.*;
import java.util.Collections;
class MeetingPoint{ 

	public static int minDistanceFOrMeeting(int[][] matrix) {
	int var1=matrix.length;
	int var2=matrix[0].length;
	ArrayList<Integer> columns = new ArrayList<Integer>();
	ArrayList<Integer> rows = new ArrayList<Integer>();
	for(int i=0; i<var1; i++){
		for(int j=0; j<var2; j++){
			if(matrix[i][j]==1){
				columns.add(j);
				rows.add(i);
			}
		}
	}
	int point=0;
	for(Integer i: rows){
		point += Math.abs(i - rows.get(rows.size()/2));
		}
	Collections.sort(columns);
	for(Integer i: columns){
		point+= Math.abs(i-columns.get(columns.size()/2));
		}
	return point;
	}

	public static void main(String[] args) {
		int matrix [][] = {{1, 0, 0, 0, 1}, 
				{0, 0, 0, 0, 0},
				{0, 0, 1, 0, 0}};
		System.out.println(minDistanceFOrMeeting(matrix));
		int matri [][] = {{1, 0, 1, 0, 1},
				{0, 1, 0, 0, 0}, 
				{0, 1, 1, 0, 0}};
		System.out.println(minDistanceFOrMeeting(matri)); 
		int matr [][] = {{1,1},
				{1,1}};
		System.out.println(minDistanceFOrMeeting(matr)); 
		int mat [][] = {{ 0, 0},
				{ 0, 0}};
		System.out.println(minDistanceFOrMeeting(mat)); 
		int ma [][] = {{1, 0},
				{0, 0}};
		System.out.println(minDistanceFOrMeeting(ma)); 
	}
}