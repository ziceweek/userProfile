#ifndef DATABASEACCESS_H
#define DATABASEACCESS_H
#include <string>
#include <sys/socket.h>
#include <mysql/mysql.h>
using namespace std;
class databaseAccess
{
    public:
        databaseAccess();
        void getDbInfo();
        bool connect_db();
        bool query(string);
        void  getResult();
        void close();
        virtual ~databaseAccess();



    private:
        string hostname;
        string username;
        string password;
        string dbname;
        int portnum;
        char *socketname;
        int flags;

        MYSQL mysql;


};

#endif // DATABASEACCESS_H


/*
use this class like:

#include "include/databaseAccess.h"
in any function:
    databaseAccess dba;
    dba.connect_db();
    dba.query("insert into t1 (id, name) values (123, 'untouch');");
    dba.close();

*/
