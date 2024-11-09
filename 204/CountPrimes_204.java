//204 Count Primes Given an integer n, return the number of prime numbers that are strictly less than n.
public class CountPrimes_204 {
    public static void main(String[] args) {
        System.out.println(sol(100));
    }

    private static int sol(int n){
        boolean[] isPrime = new boolean[n]; //default value is false
        int count = 0;
        for(int i=2; i<n; i++){
            if(isPrime[i] == false){
                count += 1;
                for(int j=i;  j<n ;j += i){
                    isPrime[j] = true;
                }
            }
        }
        return count;
    }
}

