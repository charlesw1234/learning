#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int
main(void)
{
    int status;
    unsigned idx;
    pid_t subpid;
    for (idx = 0; idx < 3; ++idx)
        if ((subpid = fork()) == 0) {
            int x = 9 / idx;
            exit(0);
        }
    for (idx = 0; idx < 5; ++idx) {
        subpid = waitpid(-1, &status, WNOHANG);
        printf("subpid = %d, status = %d\n", (int)subpid, status);
        sleep(1);
    }
    return 0;
}
