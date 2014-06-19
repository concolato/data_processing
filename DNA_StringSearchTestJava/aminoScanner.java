
import java.io.*;
import java.util.Scanner;

/*
 * DNA Bio String Searching - The Genetica System
 * Algorithms Design and Analysis
 * Fall 2012
 * by: Claude Concolato
 * This program is designed to experiment with amino acid strings and string matching algorithms
 * for the purpose of observing performance to determine the best algorithm.
 */

class aminoScanner {
	private static  String txt;	
	private static String pat;	
	private static int on = 1;	
	private static int off = 0;	
	private int[] right;     // the bad-character skip array for BM
	private static int threshold;	
	private static int threshold2;
	private int R;	
	
	public static void main(String[] args){
	
		int onOffSwitch = on; //input from user to be converted to int		
		boolean Switch = true;	
		System.out.print("**** Welcome to Genetica Prototype 0.1 ****\n");		
		
		while(onOffSwitch == on){ // Continuously run the program	
			String path ="dna.txt";
			
			// Gather input	
			Scanner scanner = new Scanner(System.in);       
		    System.out.print("Please Enter Gene Pattern To Search: ");
		    String geneChain = scanner.nextLine();
		
		    System.out.print("Enter Gene Sequence: ");
		    String geneSq = scanner.nextLine();
		
		    while(geneChain.length() == 0 || geneSq.length() == 0){	
			    System.out.print("ERROR - Please enter required data for both gene pattern and sequence. \n");
		
			    System.out.print("Please Enter Gene Pattern To Search: \n");	
			    geneChain = scanner.nextLine();
			
			    System.out.print("Enter Gene Sequence: \n");	
			    geneSq = scanner.nextLine();
		    }
		
			try{  		
				aminoScanner aminoObject = new aminoScanner();
			    pat = geneSq;	        	        
			    File f = new File(path);
			    String text = "";
			
			    if(f.exists()){			
				    txt = geneChain;
				    FileWriter fstream = new FileWriter(path);
				
				    BufferedWriter insert = new BufferedWriter(fstream);	
				    insert.write(txt);
				
				    insert.close();	   
				
				    FileInputStream fis = new FileInputStream(path);
				
				    // Here BufferedInputStream is added for fast reading.	
					BufferedInputStream bis = new BufferedInputStream(fis);		
					BufferedReader data = new BufferedReader(new InputStreamReader(bis));		
					StringBuffer FileContents = new StringBuffer();		
					String line = null;             
			
				    // Read file line by line from file	
					while( (line = data.readLine()) != null){	
						FileContents.append(line);
				    }	                
			
			        // Finally convert StringBuffer object to String!
			        text = FileContents.toString();
			
			        // Dispose all the resources after using them.
					fis.close();		
					bis.close();		
					data.close();
			
				}else{
			        System.out.println("Input file not found. Switching to Memory For Text Searching.");
			        text = geneChain;
			    }     
		
				if(text != ""){			
					threshold = 100;					
					threshold2 = 12;
									
					//determine optimal searching					
					long startTimer = System.nanoTime();					
					if(text.length() < threshold){			
						BF(pat, text); // speed
					
					}else if(text.length() >= threshold  &&  pat.length() >= threshold2){			
						aminoObject.BandM(pat, text); //speed
					
					}else{		
						KMP(pat, text);	//frequency	
					}
					long endTimer = System.nanoTime();						
					final double million = 100000000.0;	
					
					double time = (endTimer - startTimer) / million;	
					
					System.out.println("Length of text threshold is "+threshold+" Characters");
					System.out.println("Length of pattern threshold is "+threshold2+" Characters");
					
					System.out.println("Length of text is "+text.length()+" Characters");
					System.out.println("Length of pattern is "+pat.length()+" Characters");
								
					System.out.println("*Processing time = "+time+" seconds. \n Press 1 for Yes and 0 for No to continue.\n");			
					onOffSwitch = scanner.nextInt();			
									
					/*
					Switch = validateInt(onOffSwitch);			
					System.out.println(onOffSwitch + Switch);
					
					while(Switch == false){		
						System.out.println("You need to enter 1 or 0 to continue.");			
						onOffSwitch = scanner.nextLine();			
						Switch = validateInt(onOffSwitch);
							
						if(Switch == true){
									
						}			
					} */
								
					if(onOffSwitch == off){			
						System.out.println("Shutting down Genetica...\nSalutations.");		
					}
					
				}else{			
					System.out.println("Text is empty.");			
				}        					
			}catch(IOException e){			
				System.err.println("Error 1: "+ e.getMessage());		
			}	
		}//end while		
	} // end main
		
	public static boolean validateInt(String input){		
		try{	
			int x = Integer.parseInt(input);		
			return true;
		
		}catch(NumberFormatException NFe){		
			return false;	
		}	
	} 

    //Brute Force O(N)
    public static void BF(String pat, String txt) {
        int M = pat.length();
        int N = txt.length();
        int i, j;
        int location = 0;
        System.out.println("Using Brute Force Algorithm.\r");

        for (i = 0, j = 0; i < N && j < M; i++) {
            if (txt.charAt(i) == pat.charAt(j))
            j++;
            else { i -= j; j = 0;  }
        }     

        if (j == M){ 
	        location = 1 + i - M;
	        System.out.println("Found at location "+location+" of String: "+txt);

        }else{ 
        	System.out.println("Not found.");
        }
    } 

    //Boyer and Moore O(N/M) in average case and O(N) in worst case.  
    public int BandM(String pat, String txt) {
        int M = pat.length();
        int N = txt.length();
        int location = 0;
        int skip;       
        this.R = 256; // represents total number of characters - alphabet. can be changed to 4 for amino acids.

        System.out.println("Using Boyer and Moore Algorithm.\n");       
        right = new int[R];
        
        for (int c = 0; c < R; c++)
            right[c] = -1;

        for (int j = 0; j < pat.length(); j++)
            right[pat.charAt(j)] = j;      

        for (int i = 0; i <= N - M; i += skip) {
            skip = 0;

            for (int j2 = M-1; j2 >= 0; j2--) {
                if (pat.charAt(j2) != txt.charAt(i+j2)) {                
                    skip = Math.max(1, j2 - right[txt.charAt(i+j2)]);
                    break;
                }               
            }           

            if (skip == 0){
            	location = i + 1;
                System.out.println("Found at charecter number "+location+".\n");// found
                return i;
            }           
        } 
     
        System.out.println("Not found.");
        return N;
    }
 
    //Knuth, Morris and Pratt O(MN)
    public static void KMP(String pat, String txt) {
        int M = pat.length();
        int N = txt.length();
        int location = 0;
        System.out.println("Using KMP Algorithm.\r");     

        for (int i = 0; i <= N - M; i++) {
            int j;
            for (j = 0; j < M; j++) {
                if (txt.charAt(i+j) != pat.charAt(j))
                    break;
            }
            
            if (j == M){               
                location = i + 1;
                System.out.println("Found at location "+location+" of String: "+txt+"\n");// found at offset i              
            }
        }     

        if(location == 0){
        	System.out.println("Not found.\r");
        }
    } 
    
} //end class
