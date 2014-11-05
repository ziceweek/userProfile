#include <iostream>
#include <databaseAccess.h>
using namespace std;

int main()
{
    databaseAccess dba;
    dba.connect_db();
    dba.query("select * from hjtest1.weibo LIMIT 0,10;");
    dba.getResult();
    dba.close();
}
