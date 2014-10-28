#ifndef PERSONALINFO_H
#define PERSONALINFO_H


class personalInfo
{
    public:
        personalInfo();
        virtual ~personalInfo();
        int get_id();
        int get_field_num();

    protected:
        int _id;
        int _field_num;
        bool set_id();


    private:


};

#endif // PERSONALINFO_H
