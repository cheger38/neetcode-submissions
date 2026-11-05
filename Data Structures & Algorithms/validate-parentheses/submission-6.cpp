class Solution {
public:
    bool isValid(string s) {
        auto isOpen = [](char c) {
            if ( c == '(' || c == '{' || c == '[' ) {
                return true;
            }

            return false;
        };

        auto matches = [](char open, char close) {
            if (
                (open == '(' && close == ')') ||
                (open == '[' && close == ']') ||
                (open == '{' && close == '}')
            ) {
                return true;
            }

            return false;
        };

        stack<char> st;

        for (char c : s) {
            if (isOpen(c)) {
                st.push(c);
                continue;
            }

            if (st.empty()) {
                return false;
            }

            if (matches(st.top(), c)) {
                st.pop();
            } else {
                return false;
            }
        }

        return st.empty();
    }
};
