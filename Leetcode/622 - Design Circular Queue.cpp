class MyCircularQueue {
private:
    vector<int> queue;   
    int size;            
    int front;           
    int rear;            
    int count;           

public:

    MyCircularQueue(int k) {
        size = k;
        queue = vector<int>(k, 0);
        front = 0;
        rear = -1;
        count = 0;
    }
    
    bool enQueue(int value) {
        if (isFull()) return false;
        rear = (rear + 1) % size;
        queue[rear] = value;
        count++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % size;
        count--;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return queue[front];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return queue[rear];
    }
    
    bool isEmpty() {
        return count == 0;
    }
    
    bool isFull() {
        return count == size;
    }
};
