#include "preprocess.h"
#include "common.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
preprocess::preprocess()
{
    //ctor
     if(NLPIR_Init(0,UTF8_CODE))//这个地方要记得制定编码
     //if(NLPIR_Init(0))
    {
        cout<<"init nlpir success!";
    }else{
        cout<<"fail to init nlpir!";
    }
    // add user defined lexicon
    if(1)
    {
        loadUserDict("/home/zice/userProfile/gdufs_iiip_14105/dict/user_defined_keywords.txt");
    }
     loadStopWords("/home/zice/userProfile/gdufs_iiip_14105/dict/append_stopword.txt");

}

preprocess::~preprocess()
{
    //dtor
}


void preprocess::loadUserDict(string path)
{
    ICTCLAS_ImportUserDict(path.c_str());
}

string preprocess::segmentation(const string sentence)
{
    const char *nRstLen =ICTCLAS_ParagraphProcess(sentence.c_str(),0);
    string ss(nRstLen);
    return ss;
}
void preprocess::loadStopWords(string path)
{

            ifstream file;
            file.open(path.c_str(),fstream::in|ios::binary);

            if(!file){
                cout<<"error occur when read the file:"<<path<<endl;
                return;
            }
            string oneline;
            while(getline(file,oneline)){
                _stopWords.insert(common::trim(oneline));

            }
            cout<<_stopWords.size()<<endl;
            file.close();
}

string preprocess::removeStopwords(string str,string seperators)
{
        string re="";
        if(_stopWords.size()==0)
        {
            cout<<"stopwords lexicon is null"<<endl;
        }

        int n = str.length();
        int start, stop;



        start = str.find_first_not_of(seperators);
        while (start >= 0 && start < n) {
            stop = str.find_first_of(seperators, start);
            if (stop < 0 || stop > n) {
                stop = n;
            }

            string word  = str.substr(start, stop - start);

            if(!isStopWord(word)&&word.size()>3)
            {
                re.append(word+" ");
            }

            start = str.find_first_not_of(seperators, stop + 1);
        }

    return re;

}

bool preprocess::isStopWord(string word)
{
    if(_stopWords.size()==0)
    {
        cout<<"there is no stopword"<<endl;
        return false;
    }
    if(_stopWords.count(word))
    {
        return true;
    }else{
        return false;
    }

}
