/*
 * dbAccess.cpp
 *
 *  Created on: 2014年11月5日
 *      Author: zice
 */

#include "dbAccess.h"
#include <string>
#include <iostream>
using namespace std;



dbAccess::dbAccess ()
{

    //ctor
    hostname = "192.168.235.38";
    username = "root";
    password = "";
    dbname = "hjtest1";
    portnum = 3306;
    socketname = NULL;
    flags = 0;
    mysql_init(&mysql);

}

dbAccess::~dbAccess ()
{
    //dtor
}

bool dbAccess::connect_db()
{
     if(!mysql_real_connect(&mysql, hostname.c_str(), username.c_str(), password.c_str(), dbname.c_str(), portnum, socketname, flags))
        return false;
     else
        return true;

}
bool dbAccess::query(string sql)
{
     if(mysql_query(&mysql, sql.c_str())==0)
     {
        cout<<"success!"<<endl;
        return true;
     }else{
        cout<<"fail!"<<endl;
        return false;
     }

     mysql_close(&mysql);
}


void dbAccess::close()
{
    mysql_close(&mysql);
}

void dbAccess::getDbInfo()
{
         cout<<"MySQL client version:"<< mysql_get_client_info()<<"\n";
}
