using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class AVL
    {
        class Node // Düğüm verilerini tutan sınıf
        {
            public int data;
            public Node left;
            public Node right;
            public Node(int data)
            {
                this.data = data;
            }
        }
        Node root; //Ağaç kökü
        public void Add(int data) //Ağaca eleman ekleme metodu
        {
            Node newItem = new Node(data);
            if (root == null)  //Eğer kök boş ise yeni eleman kök olur
            {
                root = newItem;
            }
            else
            {
                root = RecursiveInsert(root, newItem);
            }
        }
        private Node RecursiveInsert(Node current, Node n) //Ekleme ve dengeleme işleminin gerçekleştiği metot
        {
            if (current == null) //şuan tutulan düğüm null ise eklenecek eleman şuan tutulan düğüme atanır
            {
                current = n;
                return current;
            }
            else if (n.data < current.data) //eklenecek eleman şuanki tutulan elemandan küçük ise sola eklenir
            {
                current.left = RecursiveInsert(current.left, n);
                current = balance_tree(current);//ağaç şuanki tutulan düğümden itibaren dengelenir
            }
            else if (n.data > current.data) //eklenecek eleman şuanki tutulan elemandan küçük ise sola eklenir
            {
                current.right = RecursiveInsert(current.right, n); //recursive olarak işlem devam eder
                current = balance_tree(current);//ağaç şuanki tutulan düğümden itibaren dengelenir
            }
            return current; 
        }
        private Node balance_tree(Node current)//Ağacı dengeleme işlemi asıl olarak burda gerçekleşir
        {
            int b_factor = balance_factor(current); // verilen düğümün sol ve sağ çocuklarının derinlik farkı alınır
            if (b_factor > 1)//eğer sol ve sağ çocuklarının derinlik farkı 1'den fazlaysa aşağıdaki işlemler yapılır
            {
                if (balance_factor(current.left) > 0)//eğer fazlalık çevrede ise sağa tek döndürme yapılır.
                {
                    current = RotateLL(current);
                }
                else // aksi halde önce sola sonra sağa çift döndürme yapılır.
                {
                    current = RotateLR(current);
                }
            }
            else if (b_factor < -1)//eğer sol ve sağ çocuklarının derinlik farkı -1'den az ise aşağıdaki işlemler yapılır
            {
                if (balance_factor(current.right) > 0)//eğer fazlalık içerde ise önce sağa sonra sola çift döndürme yapılır.
                {
                    current = RotateRL(current);
                }
                else // aksi halde sola tek döndürme yapılır.
                {
                    current = RotateRR(current);
                }
            }
            return current;
        }
        public void DisplayTree() //Ağacı bastırma işlemi
        {
            if (root == null)
            {
                Console.WriteLine("Tree is empty");
                return;
            }
            InOrderDisplayTree(root);// InOrder olarak ağacı bastırır
            Console.WriteLine();
        }
        private void InOrderDisplayTree(Node current)
        {
            if (current != null)
            {
                InOrderDisplayTree(current.left);
                Console.Write("({0}) ", current.data);
                InOrderDisplayTree(current.right);
            }
        }
        private int max(int l, int r)
        {
            return l > r ? l : r;
        }
        private int getHeight(Node current) // recursive dönerek verilen düğümden itibaren derinliği döndürür
        {
            int height = 0;
            if (current != null)
            {
                int l = getHeight(current.left);
                int r = getHeight(current.right);
                int m = max(l, r);
                height = m + 1;
            }
            return height;
        }
        private int balance_factor(Node current) //sol ve sağ çocuk derinlik farkını döndürür
        {
            int l = getHeight(current.left);
            int r = getHeight(current.right);
            int b_factor = l - r;
            return b_factor;
        }
        private Node RotateRR(Node parent) //Sola tek döndürme
        {
            Node pivot = parent.right;
            parent.right = pivot.left;
            pivot.left = parent;
            return pivot;
        }
        private Node RotateLL(Node parent)//sağa tek döndürme
        {
            Node pivot = parent.left;
            parent.left = pivot.right;
            pivot.right = parent;
            return pivot;
        }
        private Node RotateLR(Node parent)//sağa çift döndürme 
        {
            Node pivot = parent.left;
            parent.left = RotateRR(pivot);
            return RotateLL(parent);
        }
        private Node RotateRL(Node parent)//sola çift döndürme
        {
            Node pivot = parent.right;
            parent.right = RotateLL(pivot);
            return RotateRR(parent);
        }
    }
}
