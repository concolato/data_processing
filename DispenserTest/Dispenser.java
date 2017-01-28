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
        //These remainders seem to only add to the problem.
        //double remainder1 = request - dollars;
        int quarters = (int)(request / 0.25);
        //double remainder2 = remainder1 - quarters * 0.25;
        int dimes = (int)(request / 0.1);
        //double remainder3 = request - dimes * 0.1;
        int nickels = (int)(request / 0.05);
        //double remainder4 = request - nickels * 0.05;
        int pennies = (int)(request / 0.01);
        
        int coins[] = {dollars, quarters, dimes, nickels, pennies};
        // The math here will always be wrong due to mixing data types upon performing calculations (doubles and integers).
        //double total = coins[1] * 0.25 + coins[2] * 0.1 + coins[3] * 0.05 + coins[4] * 0.01;
        System.out.println();
        double total = request;

        return new Teller.Result(coins, total);
    }

}
