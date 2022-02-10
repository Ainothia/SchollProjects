using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje2
{
    class Stack
    {
        private int maxSize; // size of stack array
        private Müşteri[] stackArray;
        private int top; // top of stack
                         //--------------------------------------------------------------
        public Stack(int s) // constructor
        {
            maxSize = s; // set array size
            stackArray = new Müşteri[maxSize]; // create array
            top = -1; // no items yet
        }
        //--------------------------------------------------------------
        public void push(Müşteri j) // put item on top of stack
        {
            stackArray[++top] = j; // increment top, insert item
        }

        public Müşteri pop() // take item from top of stack
        {
            return stackArray[top--]; // access item, decrement top
        }
        //--------------------------------------------------------------
        public Müşteri peek() // peek at top of stack
        {
            return stackArray[top];
        }
        //--------------------------------------------------------------
        public bool isEmpty() // true if stack is empty
        {
            return (top == (-1));
        }
        //--------------------------------------------------------------
        public bool isFull() // true if stack is full
        {
            return (top == (maxSize - 1));
        }
        //--------------------------------------------------------------
    } // end class StackX
}
