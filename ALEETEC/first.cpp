// 1. Write a function to find out the 2nd highest number from an Array
#include <bits/stdc++.h>

using namespace std;

int findSecondMax(vector<int> arr)
{
    int maxEle = -1;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] > maxEle)
        {
            maxEle = arr[i];
        }
    }

    int secMaxEle = -1;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] > secMaxEle && arr[i] < maxEle)
        {
            secMaxEle = arr[i];
        }
    }

    return secMaxEle;
}

int main()
{
    vector<int> arr = {3, 6, 4, 8, 9, 7};

    int res = findSecondMax(arr);

    cout << "Second max element is :" << res << endl;
}