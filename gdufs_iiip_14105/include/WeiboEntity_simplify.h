#ifndef WEIBOENTITY_SIMPLIFY_H
#define WEIBOENTITY_SIMPLIFY_H


class WeiboEntity_simplify
{
    public:
        WeiboEntity_simplify();
        virtual ~WeiboEntity_simplify();
    protected:
    private:
        string uid;
        string nice_name;
        int follow_count;
        int follower_count;
        int weibo_count;
        string introdution;
        string[] label;
        int gender;
        string school;
        string company;
};

#endif // WEIBOENTITY_SIMPLIFY_H
