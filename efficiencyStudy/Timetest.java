import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;


public class timetest {
    double coefficients[];  // coefficients of a polynomial
    int numberOfTerms;
    double Xmin = -270.0;   // default value
    double Xmax = 0.0;  // default value


    public timetest(double min, double max) {
        numberOfTerms = 14;
        coefficients = new double[numberOfTerms];
        coefficients[0] = 0.000000000000E+00;
        coefficients[1] = 0.586655087080E-01;
        coefficients[2] = 0.454109771240E-04;
        coefficients[3] = -0.779980486860E-06;
        coefficients[4] = -0.258001608430E-07;
        coefficients[5] = -0.594525830570E-09;
        coefficients[6] = -0.932140586670E-11;
        coefficients[7] = -0.102876055340E-12;
        coefficients[8] = -0.803701236210E-15;
        coefficients[9] = -0.439794973910E-17;
        coefficients[10] = -0.164147763550E-19;
        coefficients[11] = -0.396736195160E-22;
        coefficients[12] = -0.558273287210E-25;
        coefficients[13] = -0.346578420130E-28;
  
        if (min<max) {
            Xmin = min;
            Xmax = max;
        }
    }

    public double compute(double x) {
        double y = 0.0;

        // Do sum in reverse order
        for (int index=coefficients.length-1; index>=0; index--) {
            y = coefficients[index] + y * x;
        }
        return y;
    }



    public void checkTime(int samplePoints, String logFilename) throws IOException {
        BufferedWriter buf = null;
        boolean saveLog = (logFilename!=null);

        System.out.print("Time test of pure computation in Java  " + (saveLog ? " with log" : " without log") + "\n");

        long startTime = System.currentTimeMillis();

        if (saveLog) {
            try {
                File file = new File(logFilename);
                //BufferedWriter for performance, false to set overwrite to file flag
                buf = new BufferedWriter(new FileWriter(file, false));
            } catch (IOException e) {
                saveLog = false;
                if (buf!=null) buf.close();
            }
        }


        double delta = (Xmax-Xmin) / (samplePoints-1);
        for (int point=0; point<samplePoints; point++) {
            double X = Xmin + point*delta;
            double Y = compute(X);

            if (saveLog) { 
                buf.append(String.format("%f %f\n", X, Y));
            }
        }

        if (saveLog) buf.close();

        long endTime = System.currentTimeMillis();
        long timeUse = endTime - startTime;

        System.out.print("time for " + samplePoints + " computations is " + timeUse + " msec\n");

    }
    
    public double method1(double x) {
         double y = 0.0;
         
         for (int index=0; index<coefficients.length; index++) {
             y += coefficients[index] * Math.pow(x, index);
         }
         
         return y;
    }
    public double method2(double x) {
         double y = 0.0;
         
         // Do sum in reverse order
         for (int index=coefficients.length-1; index>=0; index--) {
             y = coefficients[index] + y * x;
         }
         
         return y;
    }

    public static void main(String[] args) throws IOException {
        timetest test = new timetest(-270.0, 0.0);

        /*
        test.checkTime(1000, null);
        test.checkTime(100000, null);
        test.checkTime(10000000, null);
    
        test.checkTime(1000, "jlog-1000.txt");
        test.checkTime(100000, "jlog-100000.txt");
        test.checkTime(10000000, "jlog-10000000.txt");
        */
        
        //Method 1 and 2 Tests
        double method1Num = 0.0;
        double testNum1 = 1.0;
        double testNum2 = 2.0;
        double testNum3 = 3.0;
        double testNum4 = 4.0;
        double testNum5 = 5.0;
        double testNum6 = 6.0;
        
        long startTime = System.currentTimeMillis();
        method1Num = test.method1(testNum1);
        long endTime = System.currentTimeMillis();
        long timeUse = endTime - startTime;       
        System.out.print("Result of Method 1: "+ method1Num+" in "+ timeUse+"\n");
        
        method1Num = test.method1(testNum2);
        System.out.print("Result of Method 1: "+ method1Num+"\n");
        method1Num = test.method1(testNum3);
        System.out.print("Result of Method 1: "+ method1Num+"\n");
        method1Num = test.method1(testNum4);
        System.out.print("Result of Method 1: "+ method1Num+"\n");
        method1Num = test.method1(testNum5);
        System.out.print("Result of Method 1: "+ method1Num+"\n");
        method1Num = test.method1(testNum6);
        System.out.print("Result of Method 1: "+ method1Num+"\n \n");
        
        long startTime2 = System.currentTimeMillis();
        method1Num = test.method2(testNum1);
        long endTime2 = System.currentTimeMillis();
        long timeUse2 = endTime2 - startTime2;
        System.out.print("Result of Method 2: "+ method1Num+" in "+ timeUse2+"\n");
        
        method1Num = test.method2(testNum2);
        System.out.print("Result of Method 2: "+ method1Num+"\n");
        method1Num = test.method2(testNum3);
        System.out.print("Result of Method 2: "+ method1Num+"\n");
        method1Num = test.method2(testNum4);
        System.out.print("Result of Method 2: "+ method1Num+"\n");
        method1Num = test.method2(testNum5);
        System.out.print("Result of Method 2: "+ method1Num+"\n");
        method1Num = test.method2(testNum6);
        System.out.print("Result of Method 2: "+ method1Num+"\n \n");           
    }   
}