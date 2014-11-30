#ifndef COMMON_H
#define COMMON_H
#include <string>
#include <vector>
using namespace std;
class common
{
    public:
        common();
        static bool read(string dir,vector<string> &pack);
        static void split(vector<string> &result,string str,string seperators);
        static void split_rmStopword(vector<string> &result,string str,string seperators);
        static string& trim(string &str);
        virtual ~common();

};

#endif // COMMON_H
