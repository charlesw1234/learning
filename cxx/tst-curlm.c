#include <curl/curl.h>
#include <curl/multi.h>

int
main(void)
{
    int nhandles;
    CURLM *curlm; CURLMcode rcm;
    CURL *curl0, *curl1; CURLcode rc;

    curl0 = curl_easy_init();
    rc = curl_easy_setopt(curl0, CURLOPT_URL, "http://v.91jin.com/");
    if (rc != CURLE_OK) printf("%u: %s\n", __LINE__, curl_easy_strerror(rc));
    rc = curl_easy_setopt(curl0, CURLOPT_VERBOSE, 1);
    if (rc != CURLE_OK) printf("%u: %s\n", __LINE__, curl_easy_strerror(rc));

    curl1 = curl_easy_init();
    rc = curl_easy_setopt(curl1, CURLOPT_URL, "http://www.baidu.com/");
    if (rc != CURLE_OK) printf("%u: %s\n", __LINE__, curl_easy_strerror(rc));
    rc = curl_easy_setopt(curl1, CURLOPT_VERBOSE, 1);
    if (rc != CURLE_OK) printf("%u: %s\n", __LINE__, curl_easy_strerror(rc));

    curlm = curl_multi_init();
    rcm = curl_multi_add_handle(curlm, curl0);
    if (rcm != CURLM_OK) printf("%u: %s\n", __LINE__, curl_multi_strerror(rcm));
    rcm = curl_multi_add_handle(curlm, curl1);
    if (rcm != CURLM_OK) printf("%u: %s\n", __LINE__, curl_multi_strerror(rcm));

    for (;;) {
        rcm = curl_multi_perform(curlm, &nhandles);
        if (rcm != CURLM_OK) printf("%u: %s\n", __LINE__, curl_multi_strerror(rcm));
        if (nhandles == 0) break;
    }

    rcm = curl_multi_cleanup(curlm);
    if (rcm != CURLM_OK) printf("%u: %s\n", __LINE__, curl_multi_strerror(rcm));

    curl_easy_cleanup(curl1);
    curl_easy_cleanup(curl0);
    return 0;
}
