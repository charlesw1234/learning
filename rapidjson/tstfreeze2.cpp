#include "rapidjson/filereadstream.h"
#include "freezecmp.hpp"
#include "freezerender.hpp"

fjson::Document4_t *load(const char *fname)
{
    char buffer[4096];
    FILE *rfp = fopen(fname, "r");
    rapidjson::Document doc;
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    fclose(rfp);
    return new fjson::Document4_t(&doc);
}

fjson::Document4_t *loadstr(const char *docstr)
{
    rapidjson::Document doc;
    doc.Parse<0>(docstr);
    return new fjson::Document4_t(&doc);
}

int main(void)
{
    fjson::Document4_t *doc0 = load("config.json");
    fjson::Render4_t render(doc0, 0);
    char *doc0str = render.get();
    //printf("doc0str = %s\n", doc0str);
    fjson::Document4_t *doc1 = loadstr(doc0str);
    printf("cmp_f4f4 = %s\n", recur_cmp_ff(doc0, 0, doc1, 0) ? "true": "false");
    free(doc0str);
    delete doc1;
    delete doc0;
    return 0;
}
