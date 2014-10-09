#include <json.h>
#include <iostream>
#include <string>
#include<utility>
#include<iostream>
#include<fstream>
#include<sstream>
#include<sys/types.h>
#include<dirent.h>
#include<stdio.h>

#include <typeinfo>
using namespace std;

void read_one_line(string dir,string &s){
      string infile(dir);
      ifstream file;
      file.open(infile.c_str(),fstream::in);
      if(!file){
          cout<<"error occur when read the file of stop word:"<<dir<<endl;
          return;
      }
      getline(file,s);
      file.close();
      return;
    }

void save_one_line(ofstream f,string content){
  f<<content<<endl;
}


int main(){

  vector<string> all_doc;//全部文档
  vector<string> filename_under_folder;

  //读取文件夹下所有文件名
  string path = "E:\\weibo数据";
  string re_path = "E:\\weibo_Data_proed";
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

  const char *json_document;
  string json_doc_string;
  for(vector<string>::size_type ix = 0;ix!=filename_under_folder.size();++ix){

    string infile(path+"\\"+filename_under_folder[ix]);
    string outfile(re_path+"\\"+filename_under_folder[ix]);
    ifstream file;
    ofstream ofile;
    file.open(infile.c_str(),fstream::in);
    ofile.open(outfile.c_str(),ofstream::out);
//    file.seekg(0,ios::end);
//    streampos ps = file.tellg();
//    file.seekg(0,ios::beg);
    cout<<"i:"<<ix<<endl;
    if(!file){
          cout<<"error occur when read the file "<<endl;
    }
    if(!ofile){
        cout<<"error when create output file"<<endl;
    }

     while(getline(file,json_doc_string)!=""){
        if(json_doc_string.size()==0)
            break;
        string temp_s = json_doc_string.substr(1,json_doc_string.size()-2);
        json_document = temp_s.c_str();

        Json::Reader reader;
        Json::Value json_object;
        if (!reader.parse(json_document, json_object))
            return 0;
        string temp = json_object["content"].asString();
        ofile<<temp<<endl;
     }

     file.close();
     ofile.close();

  }


  return 0;
}





