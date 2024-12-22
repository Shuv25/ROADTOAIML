// 4 Find the ouccrance of repeated words in a sentance
#include <bits/stdc++.h>

using namespace std;

map<string, int> findRepeatedWords(const string &sentence)
{
    map<string, int> wordCount;
    string word = "";

    for (char c : sentence)
    {
        if (c == ' ' || c == '\0')
        {
            if (!word.empty())
            {
                wordCount[word]++;
                word.clear();
            }
        }
        else
        {
            word += c;
        }
    }

    return wordCount;
}

int main()
{
    string s = "hi there sourav from hi there from ";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    map<string, int> repeatedWords = findRepeatedWords(s);

    for (auto entry : repeatedWords)
    {
        if (entry.second > 1)
        {
            cout << entry.first << ": " << entry.second << endl;
        }
    }

    return 0;
}
