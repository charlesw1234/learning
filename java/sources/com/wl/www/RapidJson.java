package com.wl.www;

public class RapidJson {
    static { System.loadLibrary("freeze"); }

    private long self;
    private RapidDocument doc;

    private native boolean _IsNull(long self);
    private native boolean _IsFalse(long self);
    private native boolean _IsTrue(long self);
    private native boolean _IsInt(long self);
    private native boolean _IsUint(long self);
    private native boolean _IsDouble(long self);
    private native boolean _IsString(long self);
    private native boolean _IsArray(long self);
    private native boolean _IsObject(long self);

    private native char _GetType(long self);
    private native long _GetInt(long self);
    private native long _GetUint(long self);
    private native double _GetDouble(long self);
    private native String _GetString(long self);
    private native int _GetArraySize(long self);
    private native long _GetArray(long self, int idx);
    private native int _GetObjectSize(long self);
    private native String _GetObjectKey(long self, int idx);
    private native long _GetObject(long self, int idx);
    private native long _SearchObject(long self, String key);

    private native long _Locate(long self, String path);

    private native long _InitNull(RapidDocument doc);
    private native long _InitFalse(RapidDocument doc);
    private native long _InitTrue(RapidDocument doc);
    private native long _InitInt(long value, RapidDocument doc);
    private native long _InitUint(long value, RapidDocument doc);
    private native long _InitDouble(double value, RapidDocument doc);
    private native long _InitString(String value, RapidDocument doc);
    private native long _InitArray(RapidDocument doc);
    private native long _InitObject(RapidDocument doc);

    private native long _Freeze4(long self);
    private native long _Freeze8(long self);
            
    private native void _SetNull(long self, RapidDocument doc);
    private native void _SetFalse(long self, RapidDocument doc);
    private native void _SetTrue(long self, RapidDocument doc);
    private native void _SetInt(long self, long value, RapidDocument doc);
    private native void _SetUint(long self, long value, RapidDocument doc);
    private native void _SetDouble(long self, double value, RapidDocument doc);
    private native void _SetString(long self, String value, RapidDocument doc);

    public RapidJson(long self, RapidDocument doc) { this.self = self; this.doc = doc; }
    public RapidJson(RapidDocument doc, boolean value)
    {   this.self = value ? _InitTrue(doc): _InitFalse(doc); this.doc = doc; }
    public RapidJson(RapidDocument doc, long value)
    {   this.self = _InitInt(value, doc); this.doc = doc; }
    public RapidJson(RapidDocument doc, double value)
    {   this.self = _InitDouble(value, doc); this.doc = doc; }
    public RapidJson(RapidDocument doc, String value)
    {   this.self = _InitString(value, doc); this.doc = doc; }
    protected void finalize() {}

    public FreezeDocument4 Freeze4() { return new FreezeDocument4(_Freeze4(self)); }
    public FreezeDocument8 Freeze8() { return new FreezeDocument8(_Freeze8(self)); }

    public boolean IsNull() { return _IsNull(self); }
    public boolean IsFalse() { return _IsFalse(self); }
    public boolean IsTrue() { return _IsTrue(self); }
    public boolean IsInt() { return _IsInt(self); }
    public boolean IsUint() { return _IsUint(self); }
    public boolean IsDouble() { return _IsDouble(self); }
    public boolean IsString() { return _IsString(self); }
    public boolean IsArray() { return _IsArray(self); }
    public boolean IsObject() { return _IsObject(self); }

    public char GetType() { return _GetType(self); }
    public long GetInt() { return _GetInt(self); }
    public long GetUint() { return _GetUint(self); }
    public double GetDouble() { return _GetDouble(self); }
    public String GetString() { return _GetString(self); }
    public int GetArraySize() { return _GetArraySize(self); }
    public RapidJson GetArray(int idx) { return new RapidJson(_GetArray(self, idx), doc); }
    public int GetObjectSize() { return _GetObjectSize(self); }
    public String GetObjectKey(int idx) { return _GetObjectKey(self, idx); }
    public RapidJson GetObject(int idx) { return new RapidJson(_GetObject(self, idx), doc); }
    public RapidJson SearchObject(String key)
    {   return new RapidJson(_SearchObject(self, key), doc); }

    public RapidJson Locate(String path) { return new RapidJson(_Locate(self, path), doc); }
}
