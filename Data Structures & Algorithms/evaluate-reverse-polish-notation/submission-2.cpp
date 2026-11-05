class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        auto isOp = [](string s) {
            return s == "+" || s == "-" || s == "*" || s == "/";
        };

        auto calc = [](string op, int x, int y) {
            if (op == "+") {
                return x + y;
            } else if (op == "-") {
                return x - y;
            } else if (op == "*") {
                return x * y;
            } else if (op == "/") {
                return x / y;
            }
        };

        stack<int> st;

        for (const auto& s : tokens) {
            int val;

            if (!isOp(s)) {
                st.push(stol(s));
            } else {
                int y = st.top();
                st.pop();
                int x = st.top();
                st.pop();

                st.push(calc(s, x, y));
            }

        }

        return st.top();

    }
};
