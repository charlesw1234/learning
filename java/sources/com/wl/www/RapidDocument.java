package com.wl.www;

public class RapidDocument {
    static { System.loadLibrary("freeze"); }

    private long self;
    private native long _Init(String docstr);
    private native void _Free(long self);

    protected void finalize() { if (self != 0); _Free(self); }
}
