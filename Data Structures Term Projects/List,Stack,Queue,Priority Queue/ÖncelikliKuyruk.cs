using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje2
{
    class ÖncelikliKuyruk
    {
        private List<Müşteri> queArray;
        private int front;
        private int rear;
        private int nItems;
        //--------------------------------------------------------------
        public ÖncelikliKuyruk() // constructor
        {
            queArray = new List<Müşteri>();
            front = 0;
            rear = -1;
            nItems = 0;
        }
        //--------------------------------------------------------------
        public void insert(Müşteri j) // put item at rear of queue
        {
            queArray.Add(j);
            rear++; // increment rear and insert
            nItems++; // one more item
        }
        //--------------------------------------------------------------
        public Müşteri dpq() // take item from queue in descending order
        {
            int max = 0;
            if (isEmpty())
            {
                Console.WriteLine("Queue is empty.");
                return new Müşteri("Null", 0);
            }
            Müşteri maxitem = queArray[0];
            for(int i = 0; i < queArray.Count; i++)
            {
                if (max < queArray[i].getÜrünSayısı())
                {
                    max = queArray[i].getÜrünSayısı();
                    maxitem = queArray[i];
                }
            }
            nItems--;
            queArray.Remove(maxitem);
            return maxitem;
        }
        public Müşteri apq() // take item from queue in ascending order
        {
            int min = queArray[0].getÜrünSayısı();
            if (isEmpty())
            {
                Console.WriteLine("Queue is empty.");
                return new Müşteri("Null", 0);
            }
            Müşteri minitem = queArray[0];
            for (int i = 0; i < queArray.Count; i++)
            {
                if (min > queArray[i].getÜrünSayısı())
                {
                    min = queArray[i].getÜrünSayısı();
                    minitem = queArray[i];
                }
            }
            nItems--;
            queArray.Remove(minitem);
            return minitem;
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

        public int size() // number of items in queue
        {
            return nItems;
        }
        //--------------------------------------------------------------
    }
}
