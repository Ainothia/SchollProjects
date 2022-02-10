using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{ 
    class Dijkstra       
    {

        static int V;
        int minDistance(int[] dist, bool[] marked)// Verilen uzaklık ve işaret dizilerine göre en kısa uzaklığı bulur.
        {
            int min = int.MaxValue, min_index = -1; //mininum değeri sonsuz olarak belirterek daha sonrası için kolaylık sağlanır.

            for (int v = 0; v < V; v++)
                if (marked[v] == false && dist[v] <= min)//Eğer işaretlenmemişse ve minimum değerden küçükse index ve min değerleri bu değerler olarak atanır.
                {
                    min = dist[v];
                    min_index = v;
                }

            return min_index;//en küçük değerin indexini döndürür
        }

        void printSolution(int[] dist)// Uzaklık dizisini bastırır
        {
            Console.Write("Vertex     Distance "
                          + "from Source\n");
            for (int i = 0; i < V; i++)
                Console.Write(i + " \t\t " + dist[i] + "\n");
        }

        public void dijkstra(int[,] graph, int src) // En kısa yol algoritmasının uygulanma metodu
        {
            V = graph.GetLength(0);
            int[] dist = new int[V]; // Verilen kaynaktan diğerlerine en kısa uzaklıkları tutan uzaklık dizisi

            bool[] marked = new bool[V]; //En kısa yolu bulunan düğümlerin işaretlendiği dizi

            for (int i = 0; i < V; i++) // Daha sonra karşılaştırmada kolaylık olması için uzaklığın sonsuz işaretlerin ise false olarak atanması yapılmıştır.
            {
                dist[i] = int.MaxValue;
                marked[i] = false;
            }

            dist[src] = 0; //Kendine olan uzaklığı 0 olarak verilir.

            for (int count = 0; count < V - 1; count++) //Bütün düğümlere olan en kısa uzaklıkları bulmak için döngü
            {

                int u = minDistance(dist, marked);// minimum uzaklığı bulan method.İlk döngüde u her zaman kaynağa eşittir.

                marked[u] = true; //en kısa uzaklığı bulunan düğüm işaretlenir.

                for (int v = 0; v < V; v++)

                    if (!marked[v] && graph[u, v] != 0 &&
                         dist[u] != int.MaxValue && dist[u] + graph[u, v] < dist[v]) //Uzaklık dizisi gerekli kontrollerden sonra güncellenir
                        dist[v] = dist[u] + graph[u, v];
            }

            printSolution(dist);//Uzaklık dizisinin en son hali bastırılır.
        }
    }
}
