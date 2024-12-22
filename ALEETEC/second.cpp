// 2. Write a function “IsNumeric” to check whether the given string is numeric

#include <bits/stdc++.h>

using namespace std;

bool IsNumeric(string s)
{
    if (s.size() == 0)
    {
        return false;
    }
    for (char c : s)
    {
        if (!isdigit(c))
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string s = "567";

    bool res = IsNumeric(s);

    if (res == true)
    {
        cout << s << " is Numeric" << endl;
    }
    else
    {
        cout << s << " is not Numeric" << endl;
    }
}