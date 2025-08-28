int nonDivisibleSubset(int k, vector<int> s) {
    vector<int> remainder_count(k, 0);
  
    for (int num : s) {
        remainder_count[num % k]++;
    }

    int result = min(1, remainder_count[0]);

    for (int i = 1; i <= k / 2; i++) {
        if (i == k - i) {  
            result += 1;
        } else {
            result += max(remainder_count[i], remainder_count[k - i]);
        }
    }

    return result;
}
