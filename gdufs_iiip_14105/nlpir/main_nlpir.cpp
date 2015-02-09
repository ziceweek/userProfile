#include "NLPIR.h"
#include <string>
#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
int main_nlpir()
{
    fstream outputf;
    outputf.open("txtUTF8.txt",fstream::out);
    //if(NLPIR_Init(0,UTF8_CODE))//这个地方要记得制定编码
if(NLPIR_Init(0))
    {
        cout<<"init nlpir success!";
    }else{
        cout<<"fail to init nlpir!";
        return -1;
    }

    string sentence = "这是自己输入的汉字！";
    //char *s = sentence.c_str();
    const char *nRstLen =ICTCLAS_ParagraphProcess(sentence.c_str(),0);
    string ss(nRstLen);
    printf("%s\n", nRstLen);
    outputf<<ss<<endl;
    return 0;
}
