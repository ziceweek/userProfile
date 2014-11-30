#include "common.h"
#include <string>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include "preprocess.h"
using namespace std;
common::common()
{
    //ctor

}

common::~common()
{
    //dtor
}



bool common::read(string dir,vector<string> &pack)
{
            ifstream file;

            file.open(dir.c_str(),fstream::in|ios::binary);

            if(!file){
                cout<<"error occur when read the file:"<<dir<<endl;
                return false;
            }

            string oneline;

            while(getline(file,oneline)){
                pack.push_back(oneline);

            }

            file.close();
            return true;

}

void common::split(vector<string> &result,string str,string seperators)
{
            int n = str.length();
            int start, stop;

            start = str.find_first_not_of(seperators);
            while (start >= 0 && start < n) {
            stop = str.find_first_of(seperators, start);
            if (stop < 0 || stop > n) {
                stop = n;
            }

            result.push_back(str.substr(start, stop - start));
            start = str.find_first_not_of(seperators, stop + 1);
            }

}


string& common::trim(string &str)
{
    if(str.empty())
        return str;
    str.erase(0,str.find_first_not_of(" "));
    str.erase(str.find_last_not_of(" "));
    return str;
}




