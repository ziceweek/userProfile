#include "../include/databaseAccess.h"
#include <string>
#include <iostream>
using namespace std;

databaseAccess::databaseAccess()
{

    //ctor
    hostname = "127.0.0.1";
    username = "root";
    password = "";
    dbname = "test";
    portnum = 3306;
    socketname = NULL;
    flags = 0;
    mysql_init(&mysql);

}

databaseAccess::~databaseAccess()
{
    //dtor
}

bool databaseAccess::connect_db()
{
     if(!mysql_real_connect(&mysql, hostname.c_str(), username.c_str(), password.c_str(), dbname.c_str(), portnum, socketname, flags))
        return false;
     else
        return true;

}
bool databaseAccess::query(string sql)
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
void databaseAccess::getResult()
{
    MYSQL_RES *result;
    MYSQL_ROW row;
    result = mysql_store_result(&mysql);
    if(result==NULL)
        cout<<"error!"<<endl;
    else{
        unsigned int i;
        while((row = mysql_fetch_row(result))!=NULL)
        {
            for( i=0;i<mysql_num_fields(result);i++)
            {
                if(row[i]==NULL)
                    cout<<" "<<"\t";
                else{
                    cout<<row[i]<<"\t";
                }
                cout<<endl;
            }
        }
    }
    mysql_free_result(result);
}
void databaseAccess::close()
{
    mysql_close(&mysql);
}

void databaseAccess::getDbInfo()
{
         cout<<"MySQL client version:"<< mysql_get_client_info()<<"\n";
}
