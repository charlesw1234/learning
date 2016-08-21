package com.wl.www;

import java.io.IOException;
import java.io.Serializable;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class FreezeJson8Refer implements Serializable {
    static { System.loadLibrary("freeze"); }

    private FreezeJson8Holder holder;
    public int pos;

    public void writeObject(ObjectOutputStream stream) throws IOException { stream.write(pos); }
    public void readObject(ObjectInputStream stream) throws IOException { pos = stream.read(); }
    public void setHolder(FreezeJson8Holder holder) { this.holder = holder; }

    private native boolean _IsNull(FreezeJson8Holder holder, int pos);
    private native boolean _IsFalse(FreezeJson8Holder holder, int pos);
    private native boolean _IsTrue(FreezeJson8Holder holder, int pos);
    private native boolean _IsInt(FreezeJson8Holder holder, int pos);
    private native boolean _IsUint(FreezeJson8Holder holder, int pos);
    private native boolean _IsDouble(FreezeJson8Holder holder, int pos);
    private native boolean _IsString(FreezeJson8Holder holder, int pos);
    private native boolean _IsArray(FreezeJson8Holder holder, int pos);
    private native boolean _IsObject(FreezeJson8Holder holder, int pos);

    private native char _GetType(FreezeJson8Holder holder, int pos);
    private native long _GetInt(FreezeJson8Holder holder, int pos);
    private native long _GetUint(FreezeJson8Holder holder, int pos);
    private native double _GetDouble(FreezeJson8Holder holder, int pos);
    private native String _GetString(FreezeJson8Holder holder, int pos);
    private native int _GetArraySize(FreezeJson8Holder holder, int pos);
    private native int _GetArray(FreezeJson8Holder holder, int pos, int idx);
    private native int _GetObjectSize(FreezeJson8Holder holder, int pos);
    private native String _GetObjectKey(FreezeJson8Holder holder, int pos, int idx);
    private native int _GetObject(FreezeJson8Holder holder, int pos, int idx);
    private native int _SearchObject(FreezeJson8Holder holder, int pos, String key);

    private native int _Locate(FreezeJson8Holder holder, int pos, String path);

    public boolean IsNull(int pos) { return _IsNull(holder, pos); }
    public boolean IsFalse(int pos) { return _IsFalse(holder, pos); }
    public boolean IsTrue(int pos) { return _IsTrue(holder, pos); }
    public boolean IsInt(int pos) { return _IsInt(holder, pos); }
    public boolean IsUint(int pos) { return _IsUint(holder, pos); }
    public boolean IsDouble(int pos) { return _IsDouble(holder, pos); }
    public boolean IsString(int pos) { return _IsString(holder, pos); }
    public boolean IsArray(int pos) { return _IsArray(holder, pos); }
    public boolean IsObject(int pos) { return _IsObject(holder, pos); }

    public char GetType(int pos) { return _GetType(holder, pos); }
    public long GetInt(int pos) { return _GetInt(holder, pos); }
    public long GetUint(int pos) { return _GetUint(holder, pos); }
    public double GetDouble(int pos) { return _GetDouble(holder, pos); }
    public String GetString(int pos) { return _GetString(holder, pos); }
    public int GetArraySize(int pos) { return _GetArraySize(holder, pos); }
    public int GetArray(int pos, int idx) { return _GetArray(holder, pos, idx); }
    public int GetObjectSize(int pos) { return _GetObjectSize(holder, pos); }
    public String GetObjectKey(int pos, int idx) { return _GetObjectKey(holder, pos, idx); }
    public int GetObject(int pos, int idx) { return _GetObject(holder, pos, idx); }
    public int SearchObject(int pos, String key) { return _SearchObject(holder, pos, key); }

    public int Locate(int pos, String path) { return _Locate(holder, pos, path); }
}
