public class TemperatureTracker {

    
    static int[] occurs = new int[111]; 
    static int maxOccurs = 0;
    static Integer mode;

  
    static int totNums = 0;
    static double totSum = 0.0;
    static Double mean;


    static Integer minTemp;
    static Integer maxTemp;

    public static void insert(int temp) {


        occurs[temp]++;
        if (occurs[temp] > maxOccurs) {
            mode = temp;
            maxOccurs = occurs[temp];
        }

        totNums++;
        totSum += temp;
        mean = totSum / totNums;
        if (maxTemp == null || temp > maxTemp) {
            maxTemp = temp;
        }
        if (minTemp == null || temp < minTemp) {
            minTemp = temp;
        }
    }


    public static Integer getMax() {
        return maxTemp;

    }


    public static Integer getMin() {
        return minTemp;

    }


    public static Double getMean() {
        return mean;

    }


    public static Integer getMode() {
        return mode;

    }


    public static void main(String[] args) {
    	


    	insert(50);
    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(80);

    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(80);

    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(30);
        
    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());



    }
}
