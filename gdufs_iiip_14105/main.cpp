#include <iostream>
#include <databaseAccess.h>
using namespace std;

int main()
{
    databaseAccess dba;
    dba.connect_db();
    dba.query("select * from t1;");
    dba.getResult();
    dba.close();


}
