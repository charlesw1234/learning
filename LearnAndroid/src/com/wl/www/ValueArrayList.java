package com.wl.www;

import java.util.ArrayList;

public class ValueArrayList
{
    private int offset;
    private double vMax;
    private double vMin;
    private ArrayList<Double[]> valist;

    public ValueArrayList()
    {
	super();
	offset = 0;
	valist = new ArrayList<Double[]>();
    }

    public void setOffset(int _offset)
    {
	offset = _offset;
    }

    public void append(Double[] varray)
    {
	int col;
	if (valist.size() > 0) {
	    col = 0;
	} else {
	    vMax = vMin = varray[0];
	    col = 1;
	}
	while (col < varray.length) {
	    if (vMax < varray[col]) vMax = varray[col];
	    if (vMin > varray[col]) vMin = varray[col];
	    ++col;
	}
	valist.add(varray);
    }

    public boolean in(int index)
    {
	return index >= offset && index < offset + valist.size();
    }
    public double get(int index, int col) { return valist.get(index - offset)[col]; }
    public int size() { return valist.size(); }
    public double getMax() { return vMax; }
    public double getMin() { return vMin; }
}
