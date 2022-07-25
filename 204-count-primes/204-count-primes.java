class Solution {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        int count = 0;
            
        for(int i = 2; i < n; i++){
            if(primes[i] == false){
                count++;
                for(int mult = 2; i*mult < n; mult++){
                    primes[i*mult] = true;
                }
            }
        }
        
        return count;
    }
}