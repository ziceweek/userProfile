#include "preprocess.h"
#include "common.h"
#include <iostream>
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
    loadUserDict("/home/zice/userProfile/gdufs_iiip_14105/dict/user_defined_keywords.txt");

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

void preprocess::removeStopwords(string words_splited_by_space)
{
        if(_stopWords.size()==0)
        {
            cout<<"stopwords lexicon is null"<<endl;
        }

}
