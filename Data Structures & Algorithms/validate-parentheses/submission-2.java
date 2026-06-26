class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char bracket = s.charAt(i);
            if (bracket == '(' || bracket == '[' || bracket == '{') {
                stack.push(bracket);
            } else {
                
                if (stack.size() == 0) return false;

                if (bracket == ')' && stack.peek() == '(') {
                    stack.pop();
                } else if (bracket == ']' && stack.peek() == '[') {
                    stack.pop();
                } else if (bracket == '}' && stack.peek() == '{') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }

        return stack.size() == 0;
    }
}
