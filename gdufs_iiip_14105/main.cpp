#include <iostream>
#include <databaseAccess.h>
#include "preprocess.h"
#include "NLPIR.h"
#include <string>
#include <stdio.h>
#include <fstream>
#include "GibbsLDA/model.h"
using namespace std;

int main()
{
    vector<string> doc_pack;
    /*get weibo text string from database*/
    databaseAccess dba;
    dba.connect_db();
    dba.query("select text from weibo where uid = '1693867981'");
    dba.getResult(&doc_pack);
    dba.close();
    int doc_pack_size = doc_pack.size();
    cout<<"the size of doc_pack:"<<doc_pack_size<<endl;


    //segmentation on the weibo text vector
    preprocess prep;
    for(vector<string>::iterator doc_pack_itr = doc_pack.begin();doc_pack_itr!=doc_pack.end();doc_pack_itr++)
    {
        *doc_pack_itr = prep.segmentation(*doc_pack_itr);
    }

    model lda;

    //char **agrv={"MODEL_STATUS_EST","-dir","dfile","model"};
    if (lda.init(&doc_pack)) {
    cout<<"init error"<<endl;
	return 1;
    }

    if (lda.model_status == MODEL_STATUS_EST || lda.model_status == MODEL_STATUS_ESTC) {
	// parameter estimation
	lda.estimate();
    }









}
