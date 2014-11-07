#ifndef PREPROCESS_H
#define PREPROCESS_H
#include "../nlpir/include/NLPIR.h"
#include <string>
using namespace std;

class preprocess
{
    public:
        preprocess();
        string segmentation(const string sentence);
        virtual ~preprocess();
    protected:
    private:

};

#endif // PREPROCESS_H
