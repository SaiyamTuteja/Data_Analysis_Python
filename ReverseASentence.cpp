#include <bits/stdc++.h>
using namespace std;
string reverseASentence(string &s)
{
    string ans = "";
    int i = 0;
    int n = s.length();
    reverse(s.begin(), s.end());
    for (int i = 0; i < n; i++)
    {
        string word = "";
        while (i < n && s[i] != ' ')
        {
            word += s[i];
            i++;
        }
        reverse(word.begin(), word.end());
        if (word.length() > 0)
        {

            ans += " " + word;
        }
    }

    return ans.substr(1);
}
int main()
{
    string s;
    cout << "Enter the sentence to reverse :";
    getline(cin, s);
    string ans = reverseASentence(s);
    cout << ans << " ";
}