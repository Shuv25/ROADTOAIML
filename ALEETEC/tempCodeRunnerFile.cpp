// 4. Write program to Merging of two sorted lists

#include <bits/stdc++.h>

using namespace std;

vector<int> mergeTwoLists(vector<int> arrone, vector<int> arrtwo)
{
    vector<int> merged;
    int i = 0, j = 0;
    int n = arrone.size();
    int m = arrtwo.size();

    while (i < n && j < m)
    {
        if (arrone[i] < arrtwo[j])
        {
            merged.push_back(arrone[i++]);
        }
        else
        {
            merged.push_back(arrtwo[j++]);
        }
    }

    while (i < n)
    {
        merged.push_back(arrone[i++]);
    }
    while (j < m)
    {
        merged.push_back(arrtwo[j++]);
    }

    return merged;
}

int main()
{
    vector<int> arrone = {3, 5, 7, 9};
    vector<int> arrtwo = {4, 6, 8, 10, 11};

    vector<int> merge = mergeTwoLists(arrone, arrtwo);

    for (auto num : merge)
    {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
