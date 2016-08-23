#include "rapidjson/filereadstream.h"
#include "freezecmp.cpp"

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

int main(void)
{
    uint32_t pos;

    fjson::Document4_t *tstfull = load("tstfull.json");
    fjson::Document4_t *tstfull0a = load("tstfull0.json");
    fjson::Document4_t *tstfull1a = load("tstfull1.json");
    fjson::Document4_t *tstsub0a = load("tstsub0.json");
    fjson::Document4_t *tstsub1a = load("tstsub1.json");
    fjson::Document4_t *tstsub2a = load("tstsub2.json");

    pos = tstfull->Locate(0, "list.0");
    fjson::Document4_t tstsub0b(tstfull, pos);
    tstfull->Remove(pos);
    pos = tstfull->Locate(0, "list.1");
    fjson::Document4_t tstsub1b(tstfull, pos);
    tstfull->Remove(pos);
    pos = tstfull->Locate(0, "list.2");
    fjson::Document4_t tstsub2b(tstfull, pos);
    tstfull->Remove(pos);
    printf("cmp_f4f4(sub0) = %s, cmp_f4f4(sub1) = %s, cmp_f4f4(sub2) = %s\n",
           recur_cmp_ff<fjson::Document4_t>(tstsub0a, 0, &tstsub0b, 0) ? "true": "false",
           recur_cmp_ff<fjson::Document4_t>(tstsub1a, 0, &tstsub1b, 0) ? "true": "false",
           recur_cmp_ff<fjson::Document4_t>(tstsub2a, 0, &tstsub2b, 0) ? "true": "false");

    fjson::Document4_t tstfull0b(tstfull, 0);
    pos = tstfull->SearchObject(0, "list");
    tstfull->Remove(pos);
    fjson::Document4_t tstfull1b(tstfull, 0);
    printf("cmp_f4f4(full0) = %s, cmp_f4f4(full1) = %s\n",
           recur_cmp_ff<fjson::Document4_t>(tstfull0a, 0, &tstfull0b, 0) ? "true": "false",
           recur_cmp_ff<fjson::Document4_t>(tstfull1a, 0, &tstfull1b, 0) ? "true": "false");

    delete tstsub0a; delete tstsub1a; delete tstsub2a;
    delete tstfull; delete tstfull0a; delete tstfull1a;
    return 0;
}
