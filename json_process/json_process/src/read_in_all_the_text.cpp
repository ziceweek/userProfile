/*
 * main.cpp
 *
 *  Created on: 2014年9月24日
 *      Author: zice
 */
#include<map>
#include<string>
#include<vector>
#include<set>
#include<utility>
#include<iostream>
#include<fstream>
#include<sstream>
#include<sys/types.h>
#include<dirent.h>
using namespace std;


map<string,int> dict;//全部词及序号
set<string> stopwords;
string *words;

void read_stopword(string dir){
  string infile(dir);
        ifstream file;
        file.open(infile.c_str(),fstream::in);
        if(!file){
            cout<<"error occur when try to open the "<<dir<<endl;
            return;
        }
        string s;
        while(file>>s){
            stopwords.insert(s);
        }
        file.close();

}
//读取一个文档，返回一个map表示
void read_one_file(string dir,map<string,int> *words){
      string infile(dir);
      ifstream file;
      file.open(infile.c_str(),fstream::in);
      if(!file){
          cout<<"error occur when read the file of stop word:"<<dir<<endl;
          return;
      }
      string s;
      int t = 0;
      while(getline(file,s)){
          string::size_type st = s.find(" ");
          istringstream stream(s.substr(st+1,s.size()-1));
          stream>>t;
          if(!stopwords.count(s.substr(0,st))){
              (*words).insert(make_pair(s.substr(0,st),t));
              dict.insert(make_pair(s.substr(0,st),dict.size()));//得到所有词的词典

              //cout<<s.substr(0,st)<<":"<<temp<<endl;
          }


      }
      file.close();

      return ;
    }
void save_dict(string p){
  ofstream dict_file;
  int s = dict.size();
  words = new string[s];
  dict_file.open(p.c_str(),fstream::app);
  map<string,int>::iterator itr_dict = dict.begin();
  cout<<itr_dict->first<<endl;
  while(itr_dict!=dict.end()){
      words[itr_dict->second] = itr_dict->first;
      itr_dict++;
  }
  for(int i = 0;i<s;i++){
      dict_file<<words[i]<<endl;
  }
  dict_file.close();
}

int main(){

  vector< map<string,int> > all_doc;//全部文档
  vector<string> filename_under_folder;

  //读入停用词
  read_stopword("/home/zice/Luan_workspace/SogouC2/stopword.txt");

  //读取文件夹下所有文件名
  string path = "/home/zice/Luan_workspace/SogouC2/tf2/tf-new_5000";
  DIR *dirp;
  struct dirent *dp;
  dirp = opendir(path.c_str());
  while((dp=readdir(dirp))!=NULL){
      if(dp->d_name[0]=='.')
	continue;
      string s(dp->d_name);
      filename_under_folder.push_back(s);

  }
  closedir(dirp);

  //读入5000个文档
  for(vector<string>::size_type ix = 0;ix!=filename_under_folder.size();++ix){
      cout<<filename_under_folder[ix]<<endl;

      map<string,int> temp;
      read_one_file(path+"/"+filename_under_folder[ix],&temp);
      map<string,int>::iterator test_temp = temp.begin();
      while(test_temp!=temp.end()){
	  cout<<test_temp->first<<" ";
	  test_temp++;
      }
      all_doc.push_back(temp);
  }

  cout<<"全部文档的个数是："<<all_doc.size()<<endl;
  cout<<"所有词的个数："<<dict.size()<<endl;
  save_dict("/home/zice/Luan_workspace/SogouC2/tf2/dict.txt");

  vector< map<string,int> >::iterator all_doc_itr = all_doc.begin();
  ofstream output_file;
  output_file.open("/home/zice/Luan_workspace/SogouC2/tf2/result.txt",ofstream::app);
  while(all_doc_itr!=all_doc.end()){

      output_file<<all_doc_itr->size()<<" ";
      map<string,int>::iterator one_doc_itr = all_doc_itr->begin();
      while(one_doc_itr!=(*all_doc_itr).end()){
      	  int num = dict[one_doc_itr->first];
      	  output_file<<num<<":"<<one_doc_itr->second<<" ";
      	  one_doc_itr++;
       }
            output_file<<"\n";
            all_doc_itr++;
      //cout<<one_doc_itr->second;

      all_doc_itr++;
  }
  cout<<"over?"<<endl;
  output_file.close();

  return 0;
}





