package com.wl.www;

public class FreezeDocument {
    static { System.loadLibrary("FreezeDocument.so"); }

    public native int BodySize();
    public native boolean IsNull(int pos);
    public native boolean IsFalse(int pos);
    public native boolean IsTrue(int pos);
    public native boolean IsInt(int pos);
    public native boolean IsUint(int pos);
    public native boolean IsDouble(int pos);
    public native boolean IsString(int pos);
    public native boolean IsArray(int pos);
    public native boolean IsObject(int pos);

    public native char GetType(int pos);
    public native long GetInt(int pos);
    public native long GetUint(int pos);
    public native double GetDouble(int pos);
    public native String GetString(int pos);
    public native int GetArraySize(int pos);
    public native int GetArray(int pos, int idx);
    public native int GetObjectSize(int pos);
    public native String GetObjectKey(int pos, int idx);
    public native int GetObject(int pos, int idx);
    public native int SearchObject(int pos, String key);

    public native int Locate(int pos, String path);
}
