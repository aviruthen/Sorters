#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ELMS 100000
#define MAX_VALUE 100


int* gen_list_uniform_ints() {
    int* lst = malloc(ELMS * sizeof(int));
    srand(time(NULL));
    for (int i = 0; i < ELMS; i++) {
        lst[i] = rand() % (MAX_VALUE + 1);
    }
    return lst;
}

// int* sort_list_power3(int* lst) {
//     int min = lst[0];
//     int max = lst[0];
//     for (int i = 0; i < ELMS; i++) {
//         if (lst[i] < min) {
//             min = lst[i];
//         } else if (lst[i] > max) {
//             max = lst[i];
//         }
//     }

//     int* hmap = (int*)malloc(ELMS * sizeof(int));
//     for (int i = 0; i < ELMS; i++) {
//         int x = (int)((lst[i] - min) / max * (ELMS - 1));
//         try {
//             hmap[x].append(lst[i]);
//             int j = hmap[x].size() - 1;
//             while (j > 0 && hmap[x][j - 1] > hmap[x][j]) {
//                 hmap[x][j], hmap[x][j - 1] = hmap[x][j - 1], hmap[x][j];
//                 j -= 1;
//             }
//         } catch {
//             hmap[x] = [lst[i]];
//         }
//     }
//     int* res = (int*)malloc(ELMS * sizeof(int));
//     for (int i = 0; i < ELMS; i++) {
//         try {
//             res += hmap[i];
//         } catch {
//             continue;
//         }
//     }
//     return res;
// }

void insertionSort(int* arr, int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
 
        // Move elements of arr[0..i-1],
        // that are greater than key, 
        // to one position ahead of their
        // current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int* power_sort(int* lst, int timer) {

    clock_t start, end;
    double cpu_time_used;

    if (timer == 1) {
        start = clock();
    }

    int max = lst[0];
    int min = lst[0];
    for (int i = 0; i < ELMS; i++) {
        if (lst[i] < min) {
            min = lst[i];
        } 
        else if (lst[i] > max) {
            max = lst[i];
        }
    }

    if (timer == 1) {
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Finding Min/Max took %f seconds\n", cpu_time_used);
        start = clock();
    }
    
    int* buckets = (int*) malloc(ELMS * sizeof(int));

    // Count the sizes of each bucket
    for (int i = 0; i < ELMS; i++) {
        buckets[((lst[i] - min) * (ELMS - 1)) / max] += 1;
    }

    if (timer == 1) {
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Calculating bucket sizes took %f seconds\n", cpu_time_used);
        start = clock();
    }

    // for(int loop = 0; loop < ELMS; loop++)
    //   printf("%d ", buckets[loop]);
    
    // Compute the indices of the buckets
    int prev_size = buckets[0];
    int size_temp = buckets[0];
    buckets[0] = 0;
    for(int i = 1; i < ELMS; i++) {
        size_temp = buckets[i];
        buckets[i] = buckets[i-1] + prev_size;
        prev_size = size_temp;
    }

    if (timer == 1) {
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Calculating bucket indices took %f seconds\n", cpu_time_used);
        start = clock();
    }


    int* res = (int*) malloc(ELMS * sizeof(int));
    for (int i = 0; i < ELMS; i++) {
        int x = ((lst[i] - min) * (ELMS - 1)) / max;
        res[buckets[x]] = lst[i];
        buckets[x] += 1;
    }
    if (timer == 1) {
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Creating sorted list took %f seconds\n", cpu_time_used);
        start = clock();
    }


    insertionSort(res, ELMS);
    if (timer == 1) {
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Insertion Sort took %f seconds\n", cpu_time_used);
    }
    

    // for(int loop = 0; loop < ELMS; loop++)
       // printf("%d ", res[loop]);

    return res;

}


struct buckets
{
int number;
int* element;
};
int comparevalues(const void* fvalue, const void* svalue)
{
int p = *((int*)fvalue), q = *((int*)svalue);
if (p == q)
{
return 0;
}
else if (p < q)
{
return -1;
}
else
{
return 1;
}
}
void crtbucketsortingElement(int* sortarry, int arylength)
{
struct buckets crtbuckets[3];
int m, j, k;
for (m = 0; m < 3; m++)
{
crtbuckets[m].number = 0;
crtbuckets[m].element = (int*)malloc(sizeof(int) * arylength);
}
for (m = 0; m < arylength; m++)
{
if (sortarry[m] < 0)
{
crtbuckets[0].element[crtbuckets[0].number++] = sortarry[m];
}
else if (sortarry[m] > 10)
{
crtbuckets[2].element[crtbuckets[2].number++] = sortarry[m];
}
else
{
crtbuckets[1].element[crtbuckets[1].number++] = sortarry[m];
}
}
for (k = 0, m = 0; m < 3; m++)
{
qsort(crtbuckets[m].element, crtbuckets[m].number, sizeof(int), &comparevalues);
for (j = 0; j < crtbuckets[m].number; j++)
{
sortarry[k + j] = crtbuckets[m].element[j];
}
k = k+ crtbuckets[m].number;
free(crtbuckets[m].element);
}
}

int cmpfunc (const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}

int twoArrEqual(int* arr1, int* arr2) 
{ 
  
    // Linearly compare elements 
    for (int i = 0; i < ELMS; i++) 
        if (arr1[i] != arr2[i]) {
            return 0;
        }
  
    // If all elements were same. 
    return 1;
}

int main(int argc, char *argv[]) {
    int* lst = gen_list_uniform_ints();

    int* lst_two = (int*) malloc(ELMS * sizeof(int));

    for (int i = 0; i < ELMS; i++) {
        lst_two[i] = lst[i];
    }

    // lst = sort_list_power3();

    // for(int loop = 0; loop < ELMS; loop++)
        // printf("%d ", lst[loop]);

    clock_t start, end;
    double cpu_time_used;
    double cpu_time_used_two;
    start = clock();
    lst = power_sort(lst, 0);
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Power Time: %f", cpu_time_used);

    start = clock();
    //qsort(lst_two, ELMS, sizeof(int), cmpfunc);
    crtbucketsortingElement(lst_two, ELMS);
    end = clock();
    cpu_time_used_two = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nQSort Time: %f", cpu_time_used_two);

    printf("\nMy Algorithm is %f times faster than qsort", cpu_time_used_two / cpu_time_used);




    // for(int loop = 0; loop < ELMS; loop++)
        // printf("%d ", lst_two[loop]);

    if (twoArrEqual(lst, lst_two) == 1) {
         printf("\nSorted Lists are Equal!");
    }


}

