using Proje3;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    public class MaxHeap
    {
        public Durak[] Heap;
        public int size;
        public int maxsize;

        // Constructor to initialize an 
        // empty max heap with given maximum 
        // capacity. 
        public MaxHeap(int maxsize)
        {
            this.maxsize = maxsize;
            this.size = 0;
            Heap = new Durak[this.maxsize + 1];
            Heap[0] = new Durak("Null",0,0,Int32.MaxValue) ;
        }

        // Returns position of parent 
        public int parent(int pos)
        {
            return pos / 2;
        }

        // Below two functions return left and 
        // right children. 
        public int leftChild(int pos)
        {
            return (2 * pos);
        }
        public int rightChild(int pos)
        {
            return (2 * pos) + 1;
        }
        public bool RightChildExist(int pos)  // Check if right child exist
        {
            if (rightChild(pos) < size)
                return true;
            return false;
        }

        // Returns true of given node is leaf 
        public bool isLeaf(int pos)
        {
            if (pos > (size / 2))
            {
                return true;
            }
            return false;
        }

        public void swap(int fpos, int spos)
        {
            Durak tmp;
            tmp = Heap[fpos];
            Heap[fpos] = Heap[spos];
            Heap[spos] = tmp;
        }

        // A recursive function to max heapify the given 
        // subtree. This function assumes that the left and 
        // right subtrees are already heapified, we only need 
        // to fix the root. 
        public void maxHeapify(int pos)
        {
            if (isLeaf(pos))
                return;

            if (Heap[pos].getNormalBisiklet() < Heap[leftChild(pos)].getNormalBisiklet() ||
                Heap[pos].getNormalBisiklet() < Heap[rightChild(pos)].getNormalBisiklet())
            {
                if (RightChildExist(pos))
                {
                    if (Heap[leftChild(pos)].getNormalBisiklet() > Heap[rightChild(pos)].getNormalBisiklet())
                    {
                        swap(pos, leftChild(pos));
                        maxHeapify(leftChild(pos));
                    }
                    else
                    {
                        swap(pos, rightChild(pos));
                        maxHeapify(rightChild(pos));
                    }
                }
                else
                {
                    swap(pos, leftChild(pos));
                    maxHeapify(leftChild(pos));
                }
            }
        }

        // Inserts a new element to max heap 
        public void insert(Durak element)
        {
            Heap[++size] = element;

            // Traverse up and fix violated property 
            int current = size;
            while (Heap[current].getNormalBisiklet() > Heap[parent(current)].getNormalBisiklet())
            {
                swap(current, parent(current));
                current = parent(current);
            }
        }

        public void print()
        {
            for (int i = 1; i <= size ; i++)
            {
                Console.Write(Heap[i] + " ");
            }
            Console.WriteLine();
        }

        // Remove an element from max heap 
        public Durak extractMax()
        {
            Durak popped = Heap[1];
            Heap[1] = Heap[size--];
            maxHeapify(1);
            return popped;
        }
    }
}