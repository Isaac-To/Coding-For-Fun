#include <iostream>

using namespace std;
class node {
    private:
        node *downPointer;
        node *upPointer;
        int value;
        int length;
    public:
        node(int newValue) {
            downPointer = NULL;
            value = newValue;
        }
        int getItem(int index) {
            if (index == 0) {
                return value;
            } else {
                index--;
                downPointer->getItem(index);
            }
        }
        void append(int newValue) {
            length++;
            if (downPointer == NULL) {
                downPointer = new node(newValue);
                downPointer -> upPointer = this;
            } else {
                downPointer->append(newValue);
            }
        }
        void cleanUp() {
            if (downPointer == NULL) {
                upPointer -> cleanUp();
                delete(this);
            } else {
                downPointer -> cleanUp();
            }
        }
};

int main() {
    node test = node(1);
    test.append(2);
    test.append(3);
    test.append(4);
    test.append(5);
    test.append(6);
    cout << test.getItem(0) << endl;
    cout << test.getItem(1) << endl;
}