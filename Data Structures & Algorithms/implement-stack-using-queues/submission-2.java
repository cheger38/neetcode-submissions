class MyStack {

    int size;
    Queue<Integer> queue;

    public MyStack() {
        queue = new LinkedList<>();
        size = 0;
    }
    
    public void push(int x) {
        if (queue.isEmpty()) {
            queue.offer(x);
        } else {
            Queue<Integer> temp = new LinkedList<>();
            temp.offer(x);
            for (int y: queue) {
                temp.offer(y);
            }
            queue = temp;
        }

        size++;
    
    }
    
    public int pop() {
        size--;
        return queue.poll();
    }
    
    public int top() {
        return queue.peek();
    }
    
    public boolean empty() {
        return size == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */