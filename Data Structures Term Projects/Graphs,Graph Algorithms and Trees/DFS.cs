using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class DFT 
    {
        private int V; // Düğüm sayısı


        private List<int>[] adj; //Komşuluk listesini tutan dizi

        public DFT(int v)//Constructor Metot
        {
            V = v;
            adj = new List<int>[v];
            for (int i = 0; i < v; ++i)
                adj[i] = new List<int>();
        }

        public void AddEdge(int v, int w)//Graph'a kenar ekleme metodu
        {
            adj[v].Add(w);
        }

        void DFSUtil(int v, bool[] visited)//DFS fonskiyonun gerçekleştirimi
        {

            visited[v] = true;//Mevcut düğüm işaretlenir ve bastırılır.
            Console.Write(v + " ");


            List<int> vList = adj[v]; // Düğümün komşularını bir liste olarak tutar.
            foreach (var n in vList)
            {
                if (!visited[n]) //İşaretlenmiş bir düğüm bulunana dek recursive olarak işlem devam eder.
                    DFSUtil(n, visited);
            }
        }

        public void DFS(int v)//Depth First Search(Traversal) fonskiyonu
        {

            bool[] visited = new bool[V]; //Ziyaret edilen düğümleri işaretlemek için dizi


            DFSUtil(v, visited);//Gerçekleştirim metodu.
        }
    }
}
