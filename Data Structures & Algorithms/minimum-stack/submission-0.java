class MinStack {
    Stack<Integer> stack;
    Stack<Integer> mins;

    public MinStack() {
        stack = new Stack<>();
        mins = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);

        if (mins.size() == 0) {
            mins.push(val);
        } else {
            mins.push(Math.min(val, mins.peek()));
        }

    }
    
    public void pop() {
        mins.pop();
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}
