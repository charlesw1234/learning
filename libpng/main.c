#include "png.h"

int main(void)
{
    png_structp read_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    png_infop read_info_ptr = png_create_info_struct(read_ptr);
    png_infop end_info_ptr = png_create_info_struct(read_ptr);
    png_destroy_read_struct(&read_ptr, &read_info_ptr, &end_info_ptr);
    return 0;
}
