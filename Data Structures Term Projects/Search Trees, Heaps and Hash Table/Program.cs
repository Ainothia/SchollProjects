using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] duraklar = { "İnciraltı, 28, 2, 10", "Sahilevleri, 8, 1, 11", "Doğal Yaşam Parkı, 17, 1, 6", "Bostanlı İskele, 7, 0, 5",
                "Bornova Stad,18,5,8","Bornova Metro,26,10,12","Alsancak Garı,17,3,12","Liman,20,0,15","Karataş,8,1,3"};

            List<string[]> matris = new List<string[]>();

            for (int i = 0; i < 9; i++)//splits strings by , and add them into matrix.
            {
                matris.Add(duraklar[i].Split(','));
            }
            Durak[] durak = new Durak[9];
            Durak[] durakheap = new Durak[9];
            for (int i = 0; i < durak.Length; i++)//create new Durak object from matrix.
            {
                durak[i] = new Durak(matris[i][0], Int32.Parse(matris[i][1]), Int32.Parse(matris[i][2]), Int32.Parse(matris[i][3]));
                durakheap[i] = new Durak(matris[i][0], Int32.Parse(matris[i][1]), Int32.Parse(matris[i][2]), Int32.Parse(matris[i][3]));
            }
            DurakAğacı tree = new DurakAğacı();
            //tree.insert(durak[0]);
            for (int i = 0; i < durak.Length; i++)//insert elements of array durak into tree.
            {
                tree.insert(durak[i]);
            }
            tree.inOrder(tree.getRoot());//display tree
            Console.WriteLine("Alışveriş Yapan Müşteri Sayısı(Alınan Bisiklet Sayısı): " + tree.toplamMusteri);
            Console.WriteLine("Ağacın Derinliği: " + tree.Height());
            Console.WriteLine("\n****************************\n");
            Console.WriteLine("Aramak İstediğiniz Müşterinin ID'sini Giriniz(1-20): ");
            int input = Convert.ToInt32(Console.ReadLine());
            while (input < 1 || input > 20)
            {
                Console.WriteLine("Geçerli Bir Müşteri ID'si giriniz(1-20): ");
                input = Convert.ToInt32(Console.ReadLine());
            }
            tree.IDSearch(tree.getRoot(), input);
            Console.WriteLine("\n****************************\n");
            Console.WriteLine("Bisiklet Kiralamak İstediğiniz Durağı Giriniz: ");
            string durakinput = Console.ReadLine();
            Console.WriteLine("ID'nizi giriniz(1-20): ");
            string IDinput = Console.ReadLine();
            tree.Rent(tree.getRoot(), durakinput, IDinput);
            tree.IDSearch(tree.getRoot(), Convert.ToInt32(IDinput));

            Hashtable hash = new Hashtable();

            for (int i = 0; i < matris.Count; i++)//Adds elements to hashtable
            {
                int[] values = { Convert.ToInt32(matris[i][1]), Convert.ToInt32(matris[i][2]), Convert.ToInt32(matris[i][3]) };
                hash.Add(matris[i][0], values);
            }
            foreach(int[] a in hash.Values)
            {
                if (a[0] > 5)
                {
                    a[0] -= 5;
                    a[2] += 5;
                }
            }
            Console.WriteLine("\n****************************\n");
            Console.WriteLine("Heap Yapısı: \n");
            MaxHeap heap = new MaxHeap(100);
            for (int i = 0; i < durakheap.Length; i++)
            {
                heap.insert(durakheap[i]);
            }
            heap.print();

            for (int i = 0; i < 3; i++)
                Console.WriteLine("Çekilen Durak: "+ heap.extractMax());
            Console.WriteLine("\n****************************\n");

            int[] SelectionArray = { 5, 3, 4, 8, 9, 6, 15, 2, 13 };
            Sort.selectionSort(SelectionArray);
            int[] QuickArray = { 5, 3, 4, 8, 9, 6, 15, 2, 13 };
            Sort.quickSort(QuickArray);
            

            Console.ReadKey();
        }
    }
}
