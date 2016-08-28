package com.wl.www;

public class FreezeJson4 {
    private int pos;
    private FreezeDocument4 doc;

    FreezeJson4(FreezeDocument4 doc) { pos = 0; this.doc = doc; }
    FreezeJson4(int pos, FreezeDocument4 doc) { this.pos = 0; this.doc = doc; }

    public boolean IsRemoved() { return doc.IsRemoved(pos); }
    public boolean IsNull() { return doc.IsNull(pos); }
    public boolean IsFalse() { return doc.IsFalse(pos); }
    public boolean IsTrue() { return doc.IsTrue(pos); }
    public boolean IsInt() { return doc.IsInt(pos); }
    public boolean IsUint() { return doc.IsUint(pos); }
    public boolean IsDouble() { return doc.IsDouble(pos); }
    public boolean IsString() { return doc.IsString(pos); }
    public boolean IsArray() { return doc.IsArray(pos); }
    public boolean IsObject() { return doc.IsObject(pos); }

    public char GetType() { return doc.GetType(pos); }
    public long GetInt() { return doc.GetInt(pos); }
    public long GetUint() { return doc.GetUint(pos); }
    public double GetDouble() { return doc.GetDouble(pos); }
    public String GetString() { return doc.GetString(pos); }
    public int GetArraySpace() { return doc.GetArraySpace(pos); }
    public int GetArraySize() { return doc.GetArraySize(pos); }
    public FreezeJson4 GetArray(int idx)
    {   return new FreezeJson4(doc.GetArray(pos, idx), doc); }
    public int GetObjectSpace() { return doc.GetObjectSpace(pos); }
    public int GetObjectSize() { return doc.GetObjectSize(pos); }
    public String GetObjectKey(int idx) { return doc.GetObjectKey(pos, idx); }
    public FreezeJson4 GetObject(int idx)
    {   return new FreezeJson4(doc.GetObject(pos, idx), doc); }
    public FreezeJson4 SearchObject(String key)
    {   return new FreezeJson4(doc.SearchObject(pos, key), doc); }

    public FreezeJson4 Locate(String path)
    {   return new FreezeJson4(doc.Locate(pos, path), doc); }

    public void Remove() { doc.Remove(pos); }
    public void SetNull() { doc.SetNull(pos); }
    public void SetFalse() { doc.SetFalse(pos); }
    public void SetTrue() { doc.SetTrue(pos); }
    public void SetBoolean(boolean value) { doc.SetBoolean(pos, value); }
    public void SetInt(long value) { doc.SetInt(pos, value); }
    public void SetUint(long value) { doc.SetUint(pos, value); }
    public void SetDouble(double value) { doc.SetDouble(pos, value); }
}
