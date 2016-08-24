package com.wl.www;

import java.io.IOException;
import java.io.Serializable;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class FreezeJson8 implements Serializable {
    static { System.loadLibrary("freeze"); }

    private long self;
    private native long _Init(String docstr);
    private native long _Init(FreezeJson4 other, int pos);
    private native void _Free(long self);
    private native void _writeObject(long self, ObjectOutputStream stream);
    private native long _readObject(ObjectInputStream stream);
    private native int _BodySize(long self);
    private native String _Render(long self, int pos);

    private void writeObject(ObjectOutputStream stream) throws IOException
    {   _writeObject(self, stream); }
    private void readObject(ObjectInputStream stream) throws IOException
    {   if (self != 0) _Free(self); self = _readObject(stream); }

    private native boolean _IsRemoved(long self, int pos);
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
    private native int _GetArraySpace(long self, int pos);
    private native int _GetArraySize(long self, int pos);
    private native int _GetArray(long self, int pos, int idx);
    private native int _GetObjectSpace(long self, int pos);
    private native int _GetObjectSize(long self, int pos);
    private native String _GetObjectKey(long self, int pos, int idx);
    private native int _GetObject(long self, int pos, int idx);
    private native int _SearchObject(long self, int pos, String key);

    private native int _Locate(long self, int pos, String path);

    private native void _Remove(long self, int pos);
    private native void _SetNull(long self, int pos);
    private native void _SetFalse(long self, int pos);
    private native void _SetTrue(long self, int pos);
    private native void _SetInt(long self, int pos, int value);
    private native void _SetUint(long self, int pos, int value);
    private native void _SetDouble(long self, int pos, double value);

    public FreezeJson8() { self = 0; }
    public FreezeJson8(String docstr) { self = _Init(docstr); }
    public FreezeJson8(FreezeJson4 other, int pos) { self = _Init(other, pos); }
    protected void finalize() { if (self != 0) _Free(self); }
    public boolean Ready() { return self != 0; }
    public int BodySize() { return _BodySize(self); }
    public String Render(int pos) { return _Render(self, pos); }

    public boolean IsRemoved(int pos) { return _IsRemoved(self, pos); }
    public boolean IsNull(int pos) { return _IsNull(self, pos); }
    public boolean IsFalse(int pos) { return _IsFalse(self, pos); }
    public boolean IsTrue(int pos) { return _IsTrue(self, pos); }
    public boolean IsInt(int pos) { return _IsInt(self, pos); }
    public boolean IsUint(int pos) { return _IsUint(self, pos); }
    public boolean IsDouble(int pos) { return _IsDouble(self, pos); }
    public boolean IsString(int pos) { return _IsString(self, pos); }
    public boolean IsArray(int pos) { return _IsArray(self, pos); }
    public boolean IsObject(int pos) { return _IsObject(self, pos); }

    public char GetType(int pos) { return _GetType(self, pos); }
    public long GetInt(int pos) { return _GetInt(self, pos); }
    public long GetUint(int pos) { return _GetUint(self, pos); }
    public double GetDouble(int pos) { return _GetDouble(self, pos); }
    public String GetString(int pos) { return _GetString(self, pos); }
    public int GetArraySpace(int pos) { return _GetArraySpace(self, pos); }
    public int GetArraySize(int pos) { return _GetArraySize(self, pos); }
    public int GetArray(int pos, int idx) { return _GetArray(self, pos, idx); }
    public int GetObjectSpace(int pos) { return _GetObjectSpace(self, pos); }
    public int GetObjectSize(int pos) { return _GetObjectSize(self, pos); }
    public String GetObjectKey(int pos, int idx) { return _GetObjectKey(self, pos, idx); }
    public int GetObject(int pos, int idx) { return _GetObject(self, pos, idx); }
    public int SearchObject(int pos, String key) { return _SearchObject(self, pos, key); }

    public int Locate(int pos, String path) { return _Locate(self, pos, path); }

    public void Remove(int pos) { _Remove(self, pos); }
    public void SetNull(int pos) { _SetNull(self, pos); }
    public void SetFalse(int pos) { _SetFalse(self, pos); }
    public void SetTrue(int pos) { _SetTrue(self, pos); }
    public void SetInt(int pos, int value) { _SetInt(self, pos, value); }
    public void SetUint(int pos, int value) { _SetUint(self, pos, value); }
    public void SetDouble(int pos, double value) { _SetDouble(self, pos, value); }
}
