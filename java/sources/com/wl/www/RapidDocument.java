package com.wl.www;

public class RapidDocument {
    static { System.loadLibrary("freeze"); }

    private long self;
    private native long _Init(String docstr);
    private native void _Free(long self);
    private native long _GetAllocator(long self);

    public RapidDocument(long self) { this.self = self; }
    public RapidDocument(String docstr) { self = _Init(docstr); }
    protected void finalize() { if (self != 0); _Free(self); }

    public long GetAllocator() { return _GetAllocator(self); }
}
