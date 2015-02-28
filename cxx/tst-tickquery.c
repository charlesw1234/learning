#include <stdio.h>
#include <curl/curl.h>
#include <curl/easy.h>

static const char *url = "http://www.ptrader.cn:8080/quote/tickquery/";

static size_t
_reader(void *ptr, size_t sz, size_t nmemb, void *fp)
{
    return fread(ptr, sz, nmemb, fp);
}

static size_t
_writer(void *ptr, size_t sz, size_t nmemb, void *fp)
{
    return fwrite(ptr, sz, nmemb, fp);
}

int
main(void)
{
    CURL *curl;
    struct curl_slist *headers = NULL;

    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1);
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_POST, 1);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_READFUNCTION, _reader);
    curl_easy_setopt(curl, CURLOPT_READDATA, stdin);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, 46);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, _writer);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, stdout);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return 0;
}
