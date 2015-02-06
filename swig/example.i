%module example
%{
    extern double myvar;
    extern int fact(int n);
    extern int my_mod(int x, int y);
    extern char *get_time(void);
%}

extern double myvar;
extern int fact(int n);
extern int my_mod(int x, int y);
extern char *get_time(void);

%init %{
%}
