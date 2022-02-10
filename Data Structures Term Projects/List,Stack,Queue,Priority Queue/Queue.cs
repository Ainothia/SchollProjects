using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje2
{
    class Queue
    {
        private int maxSize;
        private Müşteri[] queArray;
        private int front;
        private int rear;
        private int nItems;
        //--------------------------------------------------------------
        public Queue(int s) // constructor
        {
            maxSize = s;
            queArray = new Müşteri[maxSize];
            front = 0;
            rear = -1;
            nItems = 0;
        }
        //--------------------------------------------------------------
        public void insert(Müşteri j) // put item at rear of queue
        {
            if (rear == maxSize - 1) // deal with wraparound
                rear = -1;
            queArray[++rear] = j; // increment rear and insert
            nItems++; // one more item
        }
        //--------------------------------------------------------------
        public Müşteri remove() // take item from front of queue
        {
            if (isEmpty())
            {
                Console.WriteLine("Queue is empty.");
                return new Müşteri("Null", 0);
            }
            Müşteri temp = queArray[front++]; // get value and incr front
            if (front == maxSize) // deal with wraparound
                front = 0;
            nItems--; // one less item
            return temp;
        }
        //--------------------------------------------------------------
        public Müşteri peekFront() // peek at front of queue
        {
        return queArray[front];
        }
        //--------------------------------------------------------------
        public bool isEmpty() // true if queue is empty
        {
            bool a = (nItems == 0);
            return a;
        }
        //--------------------------------------------------------------
        public bool isFull() // true if queue is full
        {
            return (nItems == maxSize);
        }
        //--------------------------------------------------------------
        public int size() // number of items in queue
        {
            return nItems;
        }
        //--------------------------------------------------------------
    }
}
