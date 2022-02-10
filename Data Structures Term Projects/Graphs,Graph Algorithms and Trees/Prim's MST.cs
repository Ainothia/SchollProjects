using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class Prim_s_MST 
    {
        static int V;
        static int minKey(int[] key, bool[] marked) // minumum key değerinin indexini döndüren metot.
        {

            int min = int.MaxValue, min_index = -1;

            for (int v = 0; v < V; v++)
                if (marked[v] == false && key[v] < min)//min değeri ile karşılaştırarak en küçük değer bulunur.
                {
                    min = key[v];
                    min_index = v;
                }

            return min_index;
        }

        static void printMST(int[] parent, int[,] graph) //En küçük kapsayan ağacı bastıran metot.
        {
            Console.WriteLine("Edge \tWeight");
            for (int i = 1; i < V; i++)
                Console.WriteLine(parent[i] + " - " + i + "\t" + graph[i, parent[i]]);
        }


        public static void primMST(int[,] graph) //En küçük kapsayan ağacı oluşturan metot.
        {
            V = graph.GetLength(0); 

            int[] parent = new int[V]; //Oluşturulan MST'yi depolayan dizi

            int[] key = new int[V]; // En küçük ağırlıkları tutan dizi


            bool[] marked = new bool[V];//İşaret dizisi.


            for (int i = 0; i < V; i++)//Karşılaştırma için minimum değer sonsuz olarak ve işaret false olarak atanır.
            {
                key[i] = int.MaxValue;
                marked[i] = false;
            }


            key[0] = 0;
            parent[0] = -1;

 
            for (int count = 0; count < V - 1; count++)
            {

                int u = minKey(key, marked); //MST'de bulunmayan en küçük ağırlık değerini tutar.

                marked[u] = true;//Bu düğümü işaretler

                for (int v = 0; v < V; v++)

                    if (graph[u, v] != 0 && marked[v] == false
                        && graph[u, v] < key[v])//Gerekli karşılaştırmaları yaparak MST'yi ve ağırlıkları tutan diziyi günceller
                    {
                        parent[v] = u;
                        key[v] = graph[u, v];
                    }
            }

            printMST(parent, graph);//Oluşturulan en küçük kapasayan ağacı bastırır.
        }
    }
}
