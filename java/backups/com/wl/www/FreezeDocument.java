package com.wl.www;

public class FreezeDocument {
    static { System.loadLibrary("FreezeDocument"); }

    private long cxxobject;
    private native long _Init(String docstr);
    private native long _Init(FreezeDocument fdoc, int pos);
    private native void _Free(long self);
    private native int _BodySize(long self);
    private native boolean _IsNull(long self, int pos);
    private native boolean _IsFalse(long self, int pos);
    private native boolean _IsTrue(long self, int pos);
    private native boolean _IsInt(long self, int pos);
    private native boolean _IsUint(long self, int pos);
    private native boolean _IsDouble(long self, int pos);
    private native boolean _IsString(long self, int pos);
    private native boolean _IsArray(long self, int pos);
    private native boolean _IsObject(long self, int pos);

    private native char _GetType(long self, int pos);
    private native long _GetInt(long self, int pos);
    private native long _GetUint(long self, int pos);
    private native double _GetDouble(long self, int pos);
    private native String _GetString(long self, int pos);
    private native int _GetArraySize(long self, int pos);
    private native int _GetArray(long self, int pos, int idx);
    private native int _GetObjectSize(long self, int pos);
    private native String _GetObjectKey(long self, int pos, int idx);
    private native int _GetObject(long self, int pos, int idx);
    private native int _SearchObject(long self, int pos, String key);

    private native int _Locate(long self, int pos, String path);

    public FreezeDocument() { cxxobject = 0; }
    public FreezeDocument(String docstr) { cxxobject = _Init(docstr); }
    public FreezeDocument(FreezeDocument fdoc, int pos) { cxxobject = _Init(fdoc, pos); }
    protected void finalize() { if (cxxobject != 0) _Free(cxxobject); }
    public int BodySize() { return _BodySize(cxxobject); }
    public boolean IsNull(int pos) { return _IsNull(cxxobject, pos); }
    public boolean IsFalse(int pos) { return _IsFalse(cxxobject, pos); }
    public boolean IsTrue(int pos) { return _IsTrue(cxxobject, pos); }
    public boolean IsInt(int pos) { return _IsInt(cxxobject, pos); }
    public boolean IsUint(int pos) { return _IsUint(cxxobject, pos); }
    public boolean IsDouble(int pos) { return _IsDouble(cxxobject, pos); }
    public boolean IsString(int pos) { return _IsString(cxxobject, pos); }
    public boolean IsArray(int pos) { return _IsArray(cxxobject, pos); }
    public boolean IsObject(int pos) { return _IsObject(cxxobject, pos); }

    public char GetType(int pos) { return _GetType(cxxobject, pos); }
    public long GetInt(int pos) { return _GetInt(cxxobject, pos); }
    public long GetUint(int pos) { return _GetUint(cxxobject, pos); }
    public double GetDouble(int pos) { return _GetDouble(cxxobject, pos); }
    public String GetString(int pos) { return _GetString(cxxobject, pos); }
    public int GetArraySize(int pos) { return _GetArraySize(cxxobject, pos); }
    public int GetArray(int pos, int idx) { return _GetArray(cxxobject, pos, idx); }
    public int GetObjectSize(int pos) { return _GetObjectSize(cxxobject, pos); }
    public String GetObjectKey(int pos, int idx) { return _GetObjectKey(cxxobject, pos, idx); }
    public int GetObject(int pos, int idx) { return _GetObject(cxxobject, pos, idx); }
    public int SearchObject(int pos, String key) { return _SearchObject(cxxobject, pos, key); }

    public int Locate(int pos, String path) { return _Locate(cxxobject, pos, path); }
}
