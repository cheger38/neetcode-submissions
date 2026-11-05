class MinStack {
private:
    stack<int> st;
    stack<int> stMin;

public:
    MinStack() : st(), stMin() {}
    
    void push(int val) {
        st.push(val);
        if (stMin.empty()) {
            stMin.push(val);
        } else {
            stMin.push(min(stMin.top(), val));
        }
    }
    
    void pop() {
        st.pop();
        stMin.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return stMin.top();
    }
};
