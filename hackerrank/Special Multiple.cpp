string solve(int n) {
    queue<string> q;
    q.push("9");

    while (!q.empty()) {
        string s = q.front();
        q.pop();

        long long num = stoll(s);

        if (num % n == 0) {
            return s;  
        }

        q.push(s + "0");
        q.push(s + "9");
    }

    return ""; 
}
