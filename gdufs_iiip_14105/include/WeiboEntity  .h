#ifndef WEIBOENTITY_H
#define WEIBOENTITY_H
#include <string>
using namespace std;
//all the info from user
class WeiboEntity
{
    public:
        WeiboEntity  ();
        virtual ~WeiboEntity  ();
    protected:
    private:
        string real_name;
        string nice_name;
        string location;
        int sex;
        int sexual_orientatio;
        string birthday;
        string uid;
        string intro;
        int age;
        int sign_in_time;

        //job
        string organization_name;
        string apartment;
        string place;

        //education
        string school_type;
        string school_name;
        string department;

        string tag;

        string follower[];
        string follow[];
        string weibo[];


};

#endif // WEIBOENTITY  _H
