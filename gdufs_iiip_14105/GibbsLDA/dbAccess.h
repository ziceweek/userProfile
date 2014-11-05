/*
 * dbAccess.h
 *
 *  Created on: 2014年11月5日
 *      Author: zice
 */

#ifndef DBACCESS_H_
#define DBACCESS_H_

#include <string>
#include <sys/socket.h>
#include "mysql.h"
using namespace std;

class dbAccess
{
public:
  dbAccess ();
  void getDbInfo();
  bool connect_db();
  bool query(string);
  void close();

private:
    string hostname;
    string username;
    string password;
    string dbname;
    int portnum;
    char *socketname;
    int flags;
    MYSQL mysql;

   virtual
  ~dbAccess ();

};



/*
use this class like:

#include "include/databaseAccess.h"
in any function:
    databaseAccess dba;
    dba.connect_db();
    dba.query("insert into t1 (id, name) values (123, 'untouch');");
    dba.close();

*/





#endif /* DBACCESS_H_ */
