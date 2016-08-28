package com.wl.www;

public class RapidDocument {
    static { System.loadLibrary("freeze"); }

    private long self;
    private native long _Init(String docstr);
    private native void _Free(long self);
    private native long _Freeze4(long self, long pos);
    private native long _Freeze8(long self, long pos);
    private native String _Render(long self, long pos);
    private native long _GetAllocator(long self);

    private native boolean _IsNull(long self, long pos);
    private native boolean _IsFalse(long self, long pos);
    private native boolean _IsTrue(long self, long pos);
    private native boolean _IsInt(long self, long pos);
    private native boolean _IsUint(long self, long pos);
    private native boolean _IsDouble(long self, long pos);
    private native boolean _IsString(long self, long pos);
    private native boolean _IsArray(long self, long pos);
    private native boolean _IsObject(long self, long pos);

    private native char _GetType(long self, long pos);
    private native long _GetInt(long self, long pos);
    private native long _GetUint(long self, long pos);
    private native double _GetDouble(long self, long pos);
    private native String _GetString(long self, long pos);
    private native long _GetArraySize(long self, long pos);
    private native long _GetArray(long self, long pos, long idx);
    private native long _GetObjectSize(long self, long pos);
    private native String _GetObjectKey(long self, long pos, long idx);
    private native long _GetObject(long self, long pos, long idx);
    private native long _SearchObject(long self, long pos, String key);

    private native long _Locate(long self, long pos, String path);

    private native void _Remove(long self, long pos);
    private native void _SetNull(long self, long pos);
    private native void _SetFalse(long self, long pos);
    private native void _SetTrue(long self, long pos);
    private native void _SetInt(long self, long pos, long value);
    private native void _SetUint(long self, long pos, long value);
    private native void _SetDouble(long self, long pos, double value);

    public RapidDocument(long self) { this.self = self; }
    public RapidDocument(String docstr) { self = _Init(docstr); }
    protected void finalize() { if (self != 0); _Free(self); }
    public FreezeDocument4 Freeze4(long pos)
    {   return new FreezeDocument4(_Freeze4(self, pos)); }
    public FreezeDocument8 Freeze8(long pos)
    {   return new FreezeDocument8(_Freeze8(self, pos)); }
    public String Render(long pos) { return _Render(self, pos); }
    public long GetAllocator() { return _GetAllocator(self); }

    public boolean IsRemoved(long pos) { return false; }
    public boolean IsNull(long pos) { return _IsNull(self, pos); }
    public boolean IsFalse(long pos) { return _IsFalse(self, pos); }
    public boolean IsTrue(long pos) { return _IsTrue(self, pos); }
    public boolean IsInt(long pos) { return _IsInt(self, pos); }
    public boolean IsUint(long pos) { return _IsUint(self, pos); }
    public boolean IsDouble(long pos) { return _IsDouble(self, pos); }
    public boolean IsString(long pos) { return _IsString(self, pos); }
    public boolean IsArray(long pos) { return _IsArray(self, pos); }
    public boolean IsObject(long pos) { return _IsObject(self, pos); }

    public char GetType(long pos) { return _GetType(self, pos); }
    public long GetInt(long pos) { return _GetInt(self, pos); }
    public long GetUint(long pos) { return _GetUint(self, pos); }
    public double GetDouble(long pos) { return _GetDouble(self, pos); }
    public String GetString(long pos) { return _GetString(self, pos); }
    public long GetArraySpace(long pos) { return _GetArraySize(self, pos); }
    public long GetArraySize(long pos) { return _GetArraySize(self, pos); }
    public long GetArray(long pos, long idx) { return _GetArray(self, pos, idx); }
    public long GetObjectSpace(long pos) { return _GetObjectSize(self, pos); }
    public long GetObjectSize(long pos) { return _GetObjectSize(self, pos); }
    public String GetObjectKey(long pos, long idx) { return _GetObjectKey(self, pos, idx); }
    public long GetObject(long pos, long idx) { return _GetObject(self, pos, idx); }
    public long SearchObject(long pos, String key) { return _SearchObject(self, pos, key); }

    public long Locate(long pos, String path) { return _Locate(self, pos, path); }

    public void Remove(long pos) { _Remove(self, pos); }
    public void SetNull(long pos) { _SetNull(self, pos); }
    public void SetFalse(long pos) { _SetFalse(self, pos); }
    public void SetTrue(long pos) { _SetTrue(self, pos); }
    public void SetBoolean(long pos, boolean value)
    {   if (value) _SetTrue(self, pos); else _SetFalse(self, pos); }
    public void SetInt(long pos, long value) { _SetInt(self, pos, value); }
    public void SetUint(long pos, long value) { _SetUint(self, pos, value); }
    public void SetDouble(long pos, double value) { _SetDouble(self, pos, value); }
}
