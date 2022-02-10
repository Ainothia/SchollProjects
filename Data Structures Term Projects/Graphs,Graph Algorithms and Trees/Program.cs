using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class Program
    {
        static void Main(string[] args)
        {
            AVL avl = new AVL();
            avl.Add(5);
            avl.Add(78);
            avl.Add(54);
            avl.Add(6);
            avl.Add(1);
            avl.Add(89);
            avl.DisplayTree();
            int[,] graph = new int[,] { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
                                      { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                                      { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
                                      { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                                      { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                                      { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                                      { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                                      { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                                      { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };
            Dijkstra t = new Dijkstra();
            t.dijkstra(graph, 0);
            int[,] graph1 = new int[,] { { 0, 2, 0, 6, 0 },
                                      { 2, 0, 3, 8, 5 },
                                      { 0, 3, 0, 0, 7 },
                                      { 6, 8, 0, 0, 9 },
                                      { 0, 5, 7, 9, 0 } };

            // Print the solution 
            Prim_s_MST.primMST(graph1);
            DFT g = new DFT(4);

            g.AddEdge(0, 1);
            g.AddEdge(0, 2);
            g.AddEdge(1, 2);
            g.AddEdge(2, 0);
            g.AddEdge(2, 3);
            g.AddEdge(3, 3);

            Console.WriteLine(
                "Following is Depth First Traversal "
                + "(starting from vertex 2)");

            g.DFS(2);
            Console.ReadKey();
        }
    }
}
