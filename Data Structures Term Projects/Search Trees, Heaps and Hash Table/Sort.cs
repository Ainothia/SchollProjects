using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class Sort
    {
        public static void selectionSort(int[] a)
        {
            for(int i = 0; i < a.Length - 1; i++)
            {
                int min = i;
                for(int j = i + 1; j < a.Length; j++)
                {
                    if (a[j] < a[min])//finds the smallest element.
                        min = j;
                }
                swap(i, min, a);//swap i with the smallest element.
            }
        }
        public static void swap(int fpos,int spos,int[] a)//swap the elements of given two index of array.
        {
            int temp = a[fpos];
            a[fpos] = a[spos];
            a[spos] = temp;
        }
        public static void quickSort(int[] a)
        {
            reQuickSort(a,0,a.Length-1);
        }
        
        public static void reQuickSort(int[]a,int left,int right)
        {
            if (right <= left)//if right pointer bigger than left pointer then array is sorted.
                return;
            else
            {
                int pivot = a[right];//pivot is assigned as the last element of the array.
                int repivot = partition(a, left, right, pivot);//array divedes into two groups and assignes a new pivot.
                reQuickSort(a, left, repivot - 1);//left and right groups sorts and it goes recursively
                reQuickSort(a, repivot + 1, right);
            }
        }
        public static int partition(int[] a,int left,int right,int pivot)
        {
            int leftPtr = left - 1;
            int rightPtr = right;
            while (true)
            {
                while (a[++leftPtr] < pivot)//increase leftPtr until it finds an element bigger than pivot
                    ;
                while (rightPtr > 0 && a[--rightPtr] > pivot)//decrease rightPtr until it finds an element smaller than pivot
                    ;
                if (leftPtr >= rightPtr)//stops if leftPtr equals or bigger than rightPtr.
                    break;
                else
                    swap(leftPtr, rightPtr, a);//Swaps the elements of index leftPtr and right Ptr
            }
            swap(leftPtr, right,a);
            return leftPtr;//returns leftPtr as new pivot.
        }
    }
}
