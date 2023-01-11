#include <iostream>
#include <stack>


class MyQueue {
private:
    std::stack<int> input;
    std::stack<int> output;
public:
    MyQueue() {
        std::stack<int> input = std::stack<int>();
        std::stack<int> output = std::stack<int>();
    }
    
    void push(int x) {
        while (!output.empty()) {
            input.push(output.top());
            output.pop();
        }

        input.push(x);
    }
    
    int pop() {
        while (!input.empty()) {
            output.push(input.top());
            input.pop();
        }

        int result = output.top();
        output.pop();
        return result;
    }
    
    int peek() {
        while (!input.empty()) {
            output.push(input.top());
            input.pop();
        }

        return output.top();
    }
    
    bool empty() {
        return input.empty() && output.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */