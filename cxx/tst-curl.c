#include <curl/curl.h>

static const char *client_id = "9b903900765539fe193d";
static const char *client_secret = "57d124aeaaf43abb28551e332745159a7c53a2f1";
static const char *grant_type = "password";
static const char *auth2_url = "http://www.ptrader.cn:8080/oauth2/access_token/";
static const char *username = "wangli01";
static const char *password = "abcdef";

int
main(void)
{
    CURL *curl;
    CURLcode res;
    char postfields[1024];

    snprintf(postfields, sizeof(postfields),
             "client_id=%s&client_secret=%s&grant_type=%s&username=%s&password=%s",
             client_id, client_secret, grant_type, username, password);
    curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, auth2_url);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postfields);
    curl_easy_setopt(curl, CURLOPT_POST, 1);
    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1);
    /*curl_easy_setopt(curl, CURLOPT_COOKIEFILE, "filepath");*/
    res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return 0;
}
