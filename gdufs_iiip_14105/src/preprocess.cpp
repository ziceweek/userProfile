#include "preprocess.h"
#include <iostream>
using namespace std;
preprocess::preprocess()
{
    //ctor
     if(NLPIR_Init(0,UTF8_CODE))//这个地方要记得制定编码
    {
        cout<<"init nlpir success!";
    }else{
        cout<<"fail to init nlpir!";
    }

}

preprocess::~preprocess()
{
    //dtor
}

void getData()
{

}

string preprocess::segmentation(const string sentence)
{
    const char *nRstLen =ICTCLAS_ParagraphProcess(sentence.c_str(),0);
    string ss(nRstLen);
    return ss;
}
