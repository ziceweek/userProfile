#ifndef PREPROCESS_H
#define PREPROCESS_H
#include "../nlpir/include/NLPIR.h"
#include <string>
#include <vector>
using namespace std;

class preprocess
{
    public:
        preprocess();
        string segmentation(const string sentence);
        void removeStopwords(string path);
        void loadUserDict(string path);
        void loadStopWords(string path);
        virtual ~preprocess();




    protected:
    private:
        string _stopword_dir;
        vector<string> _stopWords;
        vector<string> _userDict;


};

#endif // PREPROCESS_H
