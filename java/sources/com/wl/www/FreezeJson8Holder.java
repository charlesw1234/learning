package com.wl.www;

import java.io.IOException;
import java.io.Serializable;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class FreezeJson8Holder implements Serializable {
    static { System.loadLibrary("freeze"); }

    private long self;
    private native long _Init(String docstr);
    private native long _Init(FreezeJson4Holder other, int pos);
    private native void _Free(long self);
    private native void _writeObject(long self, ObjectOutputStream stream);
    private native long _readObject(ObjectInputStream stream);
    private native int _BodySize(long self);

    public FreezeJson8Holder() { self = 0; }
    public FreezeJson8Holder(String docstr) { self = _Init(docstr); }
    public FreezeJson8Holder(FreezeJson4Holder other, int pos) { self = _Init(other, pos); }
    protected void finalize() { if (self != 0) _Free(self); }
    public void writeObject(ObjectOutputStream stream) throws IOException
    {   _writeObject(self, stream); }
    public void readObject(ObjectInputStream stream) throws IOException
    {   if (self != 0) _Free(self); self = _readObject(stream); }
    public int BodySize() { return _BodySize(self); }
}
