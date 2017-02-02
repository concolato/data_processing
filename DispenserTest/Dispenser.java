/*
 * Copyright (c) 2015-2017 Annie Hui @ NVCC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// A dispenser that IMPROPERLY handles currency. Find the bugs and fix them.

public class Dispenser {
    
    public Teller.Result dispense(double request) {
        int dollars = (int)request;
        int quarters = 0,  dimes = 0,  nickels = 0, pennies =0;
        // Need to grab what is to the right of the decimal point to get the true remainder.
        double remainder1 = request - Math.floor(request);
   
        if(remainder1 > 0){
	        quarters = (int)(remainder1 / 0.25);        
	        double remainder2 = remainder1 - quarters * 0.25;
	        
	        if(remainder2 > 0){	        
		        dimes = (int)(remainder2 / 0.1);	        
		        double remainder3 = remainder2 - dimes * 0.1;
		        
		        if(remainder3 > 0){	        
			        nickels = (int)(remainder3 / 0.05);
			        //Rounding the computation of the penny to the nearest 1000th of a cent for better accuracy.
			        double remainder4 = Math.round((remainder3 - nickels * 0.05)*1000);
			        
			        if(remainder4 > 0){ 	
			        	pennies = (int)(remainder4 / 10);
			        }
		        }
	        }
        }
        
        int coins[] = {dollars, quarters, dimes, nickels, pennies};
        // The math here will always be wrong due to mixing data types upon performing calculations (doubles and integers).
        //double total = coins[1] * 0.25 + coins[2] * 0.1 + coins[3] * 0.05 + coins[4] * 0.01;
        double total = request;

        return new Teller.Result(coins, total);
    }
}
