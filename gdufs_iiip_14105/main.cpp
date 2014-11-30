#include <iostream>
#include <databaseAccess.h>
#include "preprocess.h"
#include "NLPIR.h"
#include <string>
#include <stdio.h>
#include <fstream>
#include "GibbsLDA/model.h"
#include "common.h"
using namespace std;

 /*get weibo text string from database*/
void read_data_from_db(vector<string> &doc_pack)
{
    databaseAccess dba;
    dba.connect_db();
    dba.query("select text from weibo where uid = '1693867981'");
    //dba.query("select content from snippet where keyword ='柯震东吸毒' ");
    dba.getResult(&doc_pack);
    dba.close();
}
    /*get context from txt or dat file*/
void read_data_form_file(string infile,vector<string> &dp)
{

      ifstream file;
      file.open(infile.c_str(),fstream::in|ios::binary);
      if(!file){
          cout<<"error occur when read the file:"<<infile<<endl;
      }
      string one_doc;
      while(getline(file,one_doc)){
          dp.push_back(one_doc);
      }
      file.close();

}

int main()
{
    vector<string> doc_pack;
    /*get weibo text string from database*/
 //   read_data_from_db(doc_pack);
//    databaseAccess dba;
//    dba.connect_db();
//    dba.query("select text from weibo where uid = '1693867981'");
//    //dba.query("select content from snippet where keyword ='柯震东吸毒' ");
//    dba.getResult(&doc_pack);
//    dba.close();
    /*get context from txt or dat file*/
    read_data_form_file("/home/zice/wanglianxi/微博论文分析UTF8.TXT",doc_pack);
    int doc_pack_size = doc_pack.size();
    cout<<"the size of doc_pack:"<<doc_pack_size<<endl;


    //segmentation on the weibo text vector
    preprocess prep;
    for(vector<string>::iterator doc_pack_itr = doc_pack.begin();doc_pack_itr!=doc_pack.end();doc_pack_itr++)
    {
        *doc_pack_itr = prep.removeStopwords(prep.segmentation(*doc_pack_itr)," ");
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



//int main()
//{
//    preprocess prep;
//
//    string str = prep.segmentation("以是影科响力分析国内财经,网站的和讯微博那为例,使用计量学的方法,对用户的特性进行统计和分析,并使用可视化的软件Pajek进行可视化的分析。研究表明,微博用户的特性,关注者数、被关注者数和博文数均具有统计特性,地域差异明显;另外,两种类型的用户群体之和占用户总体的近90%,具有很强的代表性,为深入研究微博用户行为提供参考。");
//    string s = prep.removeStopwords(str," ");
//    cout<<s<<endl;
//    string w = "、";
//    cout<<w.size();
//}

