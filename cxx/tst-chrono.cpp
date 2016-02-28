#include <unistd.h>
#include <typeinfo>
#include <chrono>
#include <iostream>

int
main(void)
{
    std::chrono::system_clock::time_point tpstart = std::chrono::system_clock::now();
    usleep(100 * 1000);
    std::chrono::system_clock::time_point tpend = std::chrono::system_clock::now();
    std::chrono::duration<double> duration = tpend - tpstart;
    std::cout << typeid(duration).name() << std::endl;
    std::cout << duration.count() << std::endl;
    printf("%f\n", duration.count());
    return 0;
}
