#include <stdio.h>
#include "png.h"

static void
custom_transform_fn(png_structp read_ptr, png_row_infop row_info_ptr, png_bytep row_data_ptr)
{
    printf("ROW(width(%u), rowbytes(%u), color_type(%u), bit_depth(%u), channels(%u), pixel_depth(%u)\n",
           (unsigned)row_info_ptr->width,
           (unsigned)row_info_ptr->rowbytes,
           (unsigned)row_info_ptr->color_type,
           (unsigned)row_info_ptr->bit_depth,
           (unsigned)row_info_ptr->channels,
           (unsigned)row_info_ptr->pixel_depth);
}

#define ENUM2DESC(NAME) case NAME: desc = #NAME; break
int
main(int argc, char *argv[])
{
    const char *desc;
    const char *pngfname = argv[1];
    FILE *rfp = fopen(pngfname, "rb");
    png_structp read_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    png_infop read_info_ptr = png_create_info_struct(read_ptr);
    png_infop end_info_ptr = png_create_info_struct(read_ptr);
    png_set_read_user_transform_fn(read_ptr, custom_transform_fn);
    //png_set_user_transform_info(read_ptr, NULL, 4, 4); // FIXME, limited by pngrtran.c
    png_init_io(read_ptr, rfp);
    png_read_png(read_ptr, read_info_ptr, PNG_TRANSFORM_IDENTITY, NULL);
    switch (png_get_color_type(read_ptr, read_info_ptr)) {
        ENUM2DESC(PNG_COLOR_TYPE_GRAY);
        ENUM2DESC(PNG_COLOR_TYPE_PALETTE);
        ENUM2DESC(PNG_COLOR_TYPE_RGB);
        ENUM2DESC(PNG_COLOR_TYPE_RGB_ALPHA);
        ENUM2DESC(PNG_COLOR_TYPE_GRAY_ALPHA);
    default: desc = "PNG_COLOR_UNKNOWN"; break;
    }
    printf("%s: COLOR_TYPE = [%s]\n", pngfname, desc);
    printf("%s: SIZE = %u x %u, BIT_DEPTH = %u\n", pngfname,
           (unsigned)png_get_image_width(read_ptr, read_info_ptr),
           (unsigned)png_get_image_height(read_ptr, read_info_ptr),
           (unsigned)png_get_bit_depth(read_ptr, read_info_ptr));
    png_destroy_read_struct(&read_ptr, &read_info_ptr, &end_info_ptr);
    fclose(rfp);
    return 0;
}
