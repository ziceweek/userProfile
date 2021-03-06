#ifndef PREPROCESS_H
#define PREPROCESS_H
#include "../nlpir/include/NLPIR.h"
#include <string>
#include <vector>
#include <set>
#include "common.h"
using namespace std;

class preprocess
{
    public:
        preprocess();
        string segmentation(const string sentence);
        string removeStopwords(string str,string seperators);
        bool isStopWord(string word);
        void loadUserDict(string path);
        void loadStopWords(string path);

        virtual ~preprocess();




    protected:
    private:
        string _stopword_dir;
        set<string> _stopWords;
        vector<string> _userDict;


};

#endif // PREPROCESS_H
