/* File : example.i */
%module example

%{
#include "example.hxx"
%}

/* Let's just grab the original header file here */
%include "example.hxx"
