#include <stdio.h>
#include <string.h>
#include <string>
#include <list>

int
main(int argc, char *argv[])
{
    std::list<std::string> strlist;
    std::list<std::string>::iterator iter;

    strlist.push_back("A:000");
    strlist.push_back("A:001");
    strlist.push_back("A:002");
    strlist.push_back("A:003");
    strlist.push_back("A:004");
    strlist.push_back("A:005");
    strlist.push_back("A:006");

    for (iter = strlist.begin(); iter != strlist.end(); ++iter)
        printf("%u: %s\n", __LINE__, iter->c_str());
    iter = strlist.begin();
    while (iter != strlist.end())
        if (!strcmp(iter->c_str(), "A:002")) iter = strlist.erase(iter);
        else if (!strcmp(iter->c_str(), "A:003")) iter = strlist.erase(iter);
        else ++iter;
    for (iter = strlist.begin(); iter != strlist.end(); ++iter)
        printf("%u: %s\n", __LINE__, iter->c_str());
    return 0;
}
